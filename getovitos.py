from inputs import inputs
import os
import csv
from ovito.io import *
from ovito.modifiers import *
from ovito.data import *

mins = {}
maxs = {}
count = 0

headings = ["sigma",'001','011','111']
sigmas = []

for inp in inputs:
    d_s = inp.split("_")
    direction = d_s[1]
    sigma = d_s[2]

    if(sigma not in sigmas):
        sigmas.append(sigma)

for sigma in sigmas:
    mins[sigma] = {"sigma": sigma,'001': 0,'011': 0,'111': 0}
    maxs[sigma] = {"sigma": sigma,'001': 0,'011': 0,'111': 0}


for inp in inputs:
    d_s = inp.split("_")
    direction = d_s[1]
    sigma = d_s[2]
    if(os.path.exists(f"{inp}/REVCON")):
        try:
            node = import_file(f"{inp}/REVCON")
            data = node.compute(0)
            data.apply(AtomicStrainModifier(cutoff=9))
            data.apply(ColorCodingModifier(property='Shear Strain',))
            print(data.attributes['ColorCoding.RangeMin'])

            mins[sigma][direction] = data.attributes['ColorCoding.RangeMin']
            maxs[sigma][direction] = data.attributes['ColorCoding.RangeMax']
        
        except:
            print(inp, "oombi output")

with open('strain_min.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headings)
    writer.writeheader()
    for m in mins:
        # print(dc[d])
        writer.writerow(mins[m])

with open('strain_max.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headings)
    writer.writeheader()
    for m in maxs:
        # print(dc[d])
        writer.writerow(maxs[m])
print(count)