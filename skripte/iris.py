import csv

import math


def ucitaj_datoteku("iris.data", "r"):
"""
Ucitavanje datoteke konstruktom with .
"""
    with open("iris.data", "r") as f :
        data = []
            for line in f :
                line = line . strip ()
# ako je linija prazna
                    if len(line) == 0:
                        continue
                parts = line.split(",")
# parsiraj podatke
                data.append(
                               (
                            float ( parts [0]) ,
                            float ( parts [1]) ,
                            float ( parts [2]) ,
                            float ( parts [3]) ,
                            parts [4]
                            )
                        )
    return data
def return_list ( index , data ) :
"""
Vracanje liste podataka .
"""
return[d[index] for d in data]