import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
import random

counter = int(0)

print("АСЬ?!")
while counter != 3:
    first = str(input(""))
    compare = first.upper()
    if compare == 'ПОКА!':
        randomvar = random.randint(1929,1950)
        print("НЕТ, НИ РАЗУ С {0} ГОДА!".format(randomvar))
        counter += 1
    elif compare == first:
        randomvar = random.randint(1929, 1950)
        print("НЕТ, НИ РАЗУ С {0} ГОДА!".format(randomvar))
        counter = 0
    else:
        print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        counter = 0
print("ДО СВИДАНИЯ, МИЛОК!")
