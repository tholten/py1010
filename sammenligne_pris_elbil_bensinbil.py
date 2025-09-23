#!/usr/bin/env python
# coding: utf-8

# # Sammenligne pris på elbil og bensinbil

# In[31]:


# Author: Thomas Holten Enstad
# Date: 23.09.2025
# Course: PY1010

# Årlig kjørelengde
kilometer_arlig = 8500 # [km]

# Pris for forsikring pr. år
forsikring_el = 5000 # [kr]
forsikring_bensin = 7500 # [kr]

# Pris på trafikkforsikringsavgift pr. år
trafikkforsikringsavgift = 8.38 * 365 # [kr]

# Årlig drivstoffbruk
drivstoffbruk_el = (0.2 * 2) * kilometer_arlig # [kr]
drivstoffbruk_bensin = 1 * kilometer_arlig # [kr]

# Årlig bomavgift
bom_el = 0.1 * kilometer_arlig # [kr]
bom_bensin = 0.3 * kilometer_arlig # [kr]

# Pris pr. år
arlig_kostnad_el = forsikring_el + trafikkforsikringsavgift + drivstoffbruk_el + bom_el
arlig_kostnad_bensin = forsikring_bensin + trafikkforsikringsavgift + drivstoffbruk_bensin + bom_bensin

# Kostnadsdifferanse pr. år.
# Funksjonen tar høyde for at elbiblkostnader kan overstige bensinbilkostnader
def arlig_kostnadsdifferanse():
    if arlig_kostnad_bensin > arlig_kostnad_el:
        return arlig_kostnad_bensin - arlig_kostnad_el
    else:
        return arlig_kostnad_el - arlig_kostnad_bensin

# Print informasjon til konsollen
# Gjør om float til string, og rund tallene til nærmeste hele tall
print("Elbil kostnad pr. år: " + str(round(arlig_kostnad_el)) + " kr")
print("Bensinbil kostnad pr. år: " + str(round(arlig_kostnad_bensin)) + " kr")
print("Kostnadsdifferanse: " + str(round(arlig_kostnadsdifferanse())) + " kr")


# In[ ]:





# In[ ]:





# In[ ]:




