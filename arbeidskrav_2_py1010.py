#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Arbeidskrav 2 i PY1010.
# Thomas Holten Enstad
# 10.11.2025


# In[ ]:


# Oppgave 1: Alder

def calculate_age(age):
    return "Ifølge mine beregninger ble du " + str(year - age) + " i " + str(year)

year = 2024
age = int(input("Hvilket år er du født?"))

if age:
    print(calculate_age(age))


# In[ ]:


# Oppgave 2: Klassefest
# Importerer math-library for å kunne bruke math.ceil()

import math

# Definerer funksjonen og tar antall elever som argument
def calculate_number_of_pizzas(antall_elever):
    pizza = antall_elever / 4
    return math.ceil(pizza) # Rund opp til nærmeste hele tall

antall_elever = int(input( 'Skriv inn antall elever:' ))

if antall_elever:
    print(calculate_number_of_pizzas(antall_elever))


# In[ ]:


# Oppgave 3: Grader til radianer
# Importerer biblioteket Numpy for å bruke PI til utregningen 

import numpy as np

def degree_to_radian(v_grad):
    v_rad = v_grad * np.pi / 180
    return str(v_grad) + " grader omgjort til radianer: " + str(v_rad) # Velger å beholde desimaler for å gjøre svaret mer nøyaktig
    

v_grad = int(input( 'Skriv inn gradtallet:') )

if v_grad:
    print(degree_to_radian(v_grad))


# In[ ]:


# Oppgave 4 a og b: By, hovedstad og folketall

data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
}

def info_om_land(land):
    return data[land][0] + " er hovedstaden i " + land + " og det er " + str(data[land][1]) + " mill. innbyggere i " + data[land][0]

land = str(input( 'Skriv inn et land (Norge, England, Frankrike eller Italia):') )

if land:
    print(info_om_land(land))


# In[ ]:


# Oppgave 4 c: Nytt land
# Bruker dictionaryen fra oppgave 4a

nytt_land = str(input( 'Skriv inn et land du ønsker å legge til i listen:' ) )
ny_hovedstad = str(input( 'Takk. Hva er hovedstaden i ' + nytt_land + '?' ) )
ny_antall_innbyggere = str(input( 'Takk. Hvor mange bor det i ' + ny_hovedstad + '? Tips: Skriv antall millioner i formatet X.XXX' ) )

if nytt_land and ny_hovedstad and ny_antall_innbyggere:
    data.update({nytt_land: [ny_hovedstad, ny_antall_innbyggere]})
    print(data)


# In[ ]:


# Oppgave 5: 
# Importerer numpy for å kunne bruke PI

import numpy as np

def areal_og_omkrets(a, b):
    halvsirkel_areal = (np.pi * (a/2)**2) / 2
    halvsirkel_omkrets = (2 * np.pi * (a/2)) / 2
    trekant_areal = (a * b) / 2
    trekant_omkrets = b + halvsirkel_omkrets
    figur_areal = round(halvsirkel_areal + trekant_areal)
    figur_omkrets = round(halvsirkel_omkrets + trekant_omkrets)
    return "Figuren har areal: " + str(figur_areal) + " og omkrets: " + str(figur_omkrets)
    
a = float(input( 'Trekantens grunnlinje:'))
b = float(input( 'Trekantens høyde:'))

if a and b:
    print(areal_og_omkrets(a, b))


# In[ ]:


# Oppgave 6:

import numpy as np

intervall = np.linspace(-10, 10, 200)

def funksjon(x):
    return -x**2 - 5;

print(intervall)

