from inputs import inputs
from angles import anglemap
import os
import csv
from ovito.io import *
from ovito.modifiers import *
from ovito.data import *

mins = []
maxs = []
count = 0

for inp in inputs:
    d_s = inp.split("_",1)[1]
    angle = anglemap[d_s]
    if(os.path.exists(f"{inp}/REVCON")):
        try:
            node = import_file(f"{inp}/REVCON")
            data = node.compute(0)
            data.apply(AtomicStrainModifier(cutoff=9))
            data.apply(ColorCodingModifier(property='Shear Strain',))
            print(data.attributes['ColorCoding.RangeMin'])

            mins.append(f"{angle},{data.attributes['ColorCoding.RangeMin']}")
            maxs.append(f"{angle},{data.attributes['ColorCoding.RangeMax']}")
        
        except:
            print(inp, "oombi output")

with open('strain_min_angle.csv', 'w') as f:
    f.writelines(mins)

with open('strain_max_angle.csv', 'w') as f:
    f.writelines(maxs)
print(count)