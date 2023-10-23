import numpy as np
import pandas as pd

proteins = []
lines = []
for line in open("spec_proteins.txt"):
    line_split = line.strip().split(" ")
    lines.append(line_split)

for line in lines:
    line = line.remove(line[0])
    


lines_up = []
for line in lines:
    lines_up.append(list(filter(None,line)))



for line in lines_up:
    for val in line:
        proteins.append(val)

for val in proteins:
    val.strip('"')

print(proteins)
