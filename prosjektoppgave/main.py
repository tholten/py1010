'''
STYRK - A training program for longevity
Made by Thomas Holten Enstad
Project task, PY1010, USN
Spring of 2026
'''

# Import necessary libraries
import json
from pathlib import Path
import matplotlib.pyplot as plt

'''
The Program class will handles most of the data processing.
It separates concerns, having logic inside the class, and most of the
read/write to file, program flow and plotting outside of the class.
'''
class Program:

    def __init__(self, input_data):
        self.name = input_data["name"] # For readability
        self.start_date = input_data["start_date"]
        self.duration_weeks = int(input_data["duration_weeks"])
        self.progression = input_data["progression"]
        self.sets_main = int(input_data["sets_main"])
        self.sets_supp = int(input_data["sets_supp"])
        self.reps_main = int(input_data["reps_main"])
        self.reps_supp = int(input_data["reps_supp"])
        self.break_main = int(input_data["break_main"])
        self.break_supp = int(input_data["break_supp"])
        self.squat_pr = float(input_data["squat_pr"])
        self.hangups_pr = float(input_data["hangups_pr"])
        self.bench_press_pr = float(input_data["bench_press_pr"])
        self.dips_pr = float(input_data["dips_pr"])
        self.shoulder_press_pr = float(input_data["shoulder_press_pr"])
        self.leg_curl_pr = float(input_data["leg_curl_pr"])
        self.shrugs_pr = float(input_data["shrugs_pr"])
        self.biceps_curl_pr = float(input_data["biceps_curl_pr"])

    '''
    Inside the following method, the vars() function will return a dictionary of
    local properties, the ones in the list above, and is used to regenerate input.json
    '''
    def user_inputs_dictionary(self):
        return vars(self)

    # Turning user input into a float value to calculate weekly progression
    def progression_value(self):
        if (self.progression == "sakte"):
            return 1.01
        elif (self.progression == "middels"):
            return 1.03
        elif (self.progression == "rask"):
            return 1.05
        else:
            return 1.03 # Set medium progression as a fallback value

    '''
    This method trims the starting point down to 40%, 55% or 70% 
    of the users personal best, depending on the provided weight.
    '''
    def reduce_weight(self, weight):
        weight = float(weight)
        if (weight > 25 and weight < 50 ):
            return weight * 0.55
        elif (weight > 50):
            return weight * 0.7
        else:
            return weight * 0.4

    ''' 
    This method will return a dictionary with only main exercises,
    in order to perform specific operations with them. The weight is also
    reduced at this stage. See the reduce_weight method for information.
    '''
    def main_exercises(self):
        squat = []
        hangups = []
        bench_press = []
        squat_pr = self.reduce_weight(self.squat_pr)
        hangups_pr = self.reduce_weight(self.hangups_pr)
        bench_press_pr = self.reduce_weight(self.bench_press_pr)
        progression = self.progression_value()
        duration = self.duration_weeks
        
        for i in range(duration):
            squat_pr = squat_pr * progression
            hangups_pr = hangups_pr * progression
            bench_press_pr = bench_press_pr * progression
            squat.append(squat_pr)
            hangups.append(hangups_pr)
            bench_press.append(bench_press_pr)

        dictionary = {
            "squat": squat,
            "hangups": hangups,
            "bench_press": bench_press
        }
        return dictionary

    ''' 
    This method will return a dictionary with only supplemental exercises,
    in order to perform specific operations with them. The weight is
    made a float in order to perform calculations. The weight is also
    reduced at this stage. See the reduce_weight method for information.
    '''
    def supp_exercises(self):
        dips = []
        shoulder_press = []
        leg_curl = []
        shrugs = []
        biceps_curl = []
        dips_pr = self.reduce_weight(self.dips_pr)
        shoulder_press_pr = self.reduce_weight(self.shoulder_press_pr)
        leg_curl_pr = self.reduce_weight(self.leg_curl_pr)
        shrugs_pr = self.reduce_weight(self.shrugs_pr)
        biceps_curl_pr = self.reduce_weight(self.biceps_curl_pr)
        progression = self.progression_value()
        duration = int(self.duration_weeks)

        for i in range(duration):
            dips_pr = dips_pr * progression
            shoulder_press_pr = shoulder_press_pr * progression
            leg_curl_pr = leg_curl_pr * progression
            shrugs_pr = shrugs_pr * progression
            biceps_curl_pr = biceps_curl_pr * progression
            dips.append(dips_pr)
            shoulder_press.append(shoulder_press_pr)
            leg_curl.append(leg_curl_pr)
            shrugs.append(shrugs_pr)
            biceps_curl.append(biceps_curl_pr)

        dictionary = {
            "dips": dips,
            "shoulder_press": shoulder_press,
            "leg_curl": leg_curl,
            "shrugs": shrugs,
            "biceps_curl": biceps_curl
        }
        return dictionary

    '''
    When the user wishes to overwrite information in the .json-file,
    it's necessary to combine both dictionaries when replacing it.
    '''
    def merging_main_and_supp_exercises(self):
        merged = self.main_exercises() | self.supp_exercises()
        return merged

    # Title of the training program.
    def title(self):
        return "Treningsplan for " + self.name

    '''
    An introduction text in the training program,
    with start date and duration.
    '''
    def intro(self):
        duration_weeks = str(self.duration_weeks)
        start_date = str(self.start_date)
        return duration_weeks + " uker fra og med " + start_date

    # Returns an array of week titles in order to loop it x (duration) times
    def week_title(self):
        titles = []
        i, j = 0, 1
        duration = int(self.duration_weeks)
        while (i < duration):
            titles.append("Week " + str(j))
            i += 1
            j += 1
        return titles

    '''
    This function will clean up the keys inside main_exercises and 
    supp_exercises, so they can be printed directly to the program.
    '''
    def clean_text(self, text):
        text = text.replace("_", " ")
        text = text.capitalize()
        return text

    '''
    The entire program that will either be written to a new file,
    or overwrite any existing content in output.txt.
    '''
    def full(self):
        
        duration = int(self.duration_weeks)

        with open("output.txt", "w", encoding='utf-8') as f:
            f.write(self.title() + "\n") # Writing the title method to file
            f.write(self.intro() + "\n") # Writing the intro method to file
            f.write("\n") # Adding a line break for readability

            ''' 
            First the outer loop will run x amount of times (duration in weeks, f.ex. 8),
            and write the week title for each iteration. Then the inner loop will go through
            each of the exercises inside both main_ and supp_exercises methods, and add a pretty
            name using the clean_text method, then sets, repetitions and break length between sets.
            Lastly, in the outer loop again, a line break is added for readability. 
            '''
            for i in range(duration):
                f.write(self.week_title()[i] + "\n")
                for key, value in self.main_exercises().items():
                    f.write(f"{self.clean_text(key)}: {str(self.sets_main) + 'x' + str(self.reps_main) + ' ' + str(round(value[i])) + 'kg - ' + str(self.break_main) + ' minutter pause \n' }")
                for key, value in self.supp_exercises().items():
                    f.write(f"{self.clean_text(key)}: {str(self.sets_supp) + 'x' + str(self.reps_supp) + ' ' + str(round(value[i]))+ 'kg - ' + str(self.break_supp) + ' minutter pause \n' }")
                f.write("\n")

    '''
    Once the user has given their inputs, we take those
    and overwrite any existing content inside input.json.
    '''
    def write_user_inputs_to_file(self):
        input_data = self.user_inputs_dictionary()
        file_path = "input.json"
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(input_data, file, indent=4)

    # Dictionary with all the statements and questions
    def dialogue(self):
        dictionary = {
            "overwrite": "Ønsker du å overskrive eksisterende input.json? Svar 'ja' eller 'nei'.",
            "no_new_file": "Ingen endringer ble gjort. Programmet ble laget basert på eksisterende input.json og ligger klart i output.txt.",
            "cant_find_input_file": "Programmet finner ikke input.json. Sørg for å ha en fil kalt input.json i samme mappe som denne filen.",
            "wrong_answer": "Beklager, jeg forstår ikke helt hva du mener. Kan du starte programmet på nytt og gi tydeligere instruksjoner?",
            "name": "Ditt navn:",
            "start_date": "Når ønsker du å starte programmet? (f.eks. 1. juni 2026)",
            "duration_weeks": "Hvor mange uker? (anbefalt: 8)",
            "progression": "Progresjon - 'sakte', 'middels' eller 'rask'",
            "sets_main": "Hvor mange sett på hovedøvelser? (anbefalt: 6)",
            "sets_supp": "Hvor mange sett på støtteøvelser (anbefalt: 3)?",
            "reps_main": "Hvor mange repetisjoner på hovedøvelser (anbefalt: 5)?",
            "reps_supp": "Hvor mange repetisjoner på støtteøvelser (anbefalt: 10)?",
            "break_main": "Hvor lange pauser på hovedøvelser, i minutter? (anbefalt: 3)",
            "break_supp": "Hvor lange pauser på støtteøvelser, i minutter? (anbefalt: 1)",
            "squat_pr": "Hva er din knebøy pr i kg? (f.eks. 50)",
            "hangups_pr": "Hvor mange ekstra kg klarer du når du løfter hangups? (f.eks. 5)",
            "bench_press_pr": "Hva er din benkpress pr i kg? (f.eks. 50)",
            "dips_pr": "Hvor mange ekstra kg klarer du når du tar dips? (f.eks. 5)",
            "shoulder_press_pr": "Hva er din skulderpress pr i kg? (f.eks. 15)",
            "leg_curl_pr": "Hva er din leg curl pr i kg? (f.eks. 30)",
            "shrugs_pr": "Hva er din shrugs pr i kg? (f.eks. 15)",
            "biceps_curl_pr": "Hva er din biceps curl pr i kg? (f.eks. 10)",
            "success": "Suksess. Programmet ditt er klart i output.txt. Hvis det virker for tungt eller for lett, kjør programmet en gang til med justerte vekter. Lykke til!"
        }
        return dictionary

    '''
    The speak method combines all the back and forth dialogue
    between the program and the user. It prints statements and
    questions from the dialogue method, and saves user inputs
    into the properties inside __init__.
    '''
    def speak(self):

        dialogue = self.dialogue() # For readability
        
        print(dialogue["name"])
        self.name = str(input())
        print(dialogue["start_date"])
        self.start_date = str(input())
        print(dialogue["duration_weeks"])
        self.duration_weeks = int(input())
        print(dialogue["progression"])
        self.progression = str(input())
        print(dialogue["sets_main"])
        self.sets_main = int(input())
        print(dialogue["sets_supp"])
        self.sets_supp = int(input())
        print(dialogue["reps_main"])
        self.reps_main = int(input())
        print(dialogue["reps_supp"])
        self.reps_supp = int(input())
        print(dialogue["break_main"])
        self.break_main = int(input())
        print(dialogue["break_supp"])
        self.break_supp = int(input())
        print(dialogue["squat_pr"])
        self.squat_pr = float(input())
        print(dialogue["hangups_pr"])
        self.hangups_pr = float(input())
        print(dialogue["bench_press_pr"])
        self.bench_press_pr = float(input())
        print(dialogue["dips_pr"])
        self.dips_pr = float(input())
        print(dialogue["shoulder_press_pr"])
        self.shoulder_press_pr = float(input())
        print(dialogue["leg_curl_pr"])
        self.leg_curl_pr = float(input())
        print(dialogue["shrugs_pr"])
        self.shrugs_pr = float(input())
        print(dialogue["biceps_curl_pr"])
        self.biceps_curl_pr = float(input())

    ''' 
    Initialize dialogue, merge main and supp exercises,
    write the user inputs to input.json and lastly,
    write the program in its entirety to output.txt.
    With a success message at the end.
    '''
    def create_file_based_on_user_inputs(self):        
        self.speak()
        self.merging_main_and_supp_exercises()
        self.write_user_inputs_to_file()
        self.full()
        make_graph()
        print(self.dialogue()["success"])

def make_graph():
    labels = ["Knebøy", "Benkpress", "Hangups"]

    start = [
        float(program.squat_pr), # To not encounter any issues, make sure it's a float.
        float(program.bench_press_pr),
        float(program.hangups_pr)
    ]

    # Values at the end of the training program (hopefully)
    end = [
        float(program.squat_pr) * float(program.progression_value()),
        float(program.bench_press_pr) * float(program.progression_value()),
        float(program.hangups_pr) * float(program.progression_value())
    ]

    # Posisjonen til stolpene (x-akse)
    x = [0, 1, 2]
    width = 0.3 

    # Place the start-bar slightly to the left, and end-bar to the right
    plt.bar([i - width/2 for i in x], start, width = width, label="Start")
    plt.bar([i + width/2 for i in x], end, width = width, label="Slutt")

    plt.xticks(x, labels) # Name under each bar
    plt.ylabel("Personlig rekord")
    plt.title("Styrkeutvikling")
    plt.legend() # Show explanation
    plt.show() # Show the graph


'''
Ask user if they want to overwrite existing input.json
or create program based on existing information.
'''
def check_if_overwrite():
    print(program.dialogue()["overwrite"])
    overwrite = input()

    if (overwrite == "ja"):
        program.create_file_based_on_user_inputs()
    elif (overwrite == "nei"):
        program.full() # Create program based on existing input.json file
        print(program.dialogue()["no_new_file"])
    else:
        print(program.dialogue()["wrong_answer"])

# Getting data from input.json
def input_data():
    file_path = "input.json"
    with open(file_path, "r") as f: # Using 'with open' so there's no need to close the file
        dictionary = json.loads(f.read()) # Turn json into dictionary. Assigned to a dictionary variable for readability
    return dictionary

# Checking if input.json exists
if Path("input.json").is_file():
    program = Program(input_data()) # Initialize Program class with the input.json dictionary
    check_if_overwrite()
else:
    print(program.dialogue()["cant_find_input_file"])
