from inputs import inputs
import os
import csv

dc = {}
msd = {}
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
    dc[sigma] = {"sigma": sigma,'001': 0,'011': 0,'111': 0}
    msd[sigma] = {"sigma": sigma,'001': 0,'011': 0,'111': 0}

for inp in inputs:
    d_s = inp.split("_")
    direction = d_s[1]
    sigma = d_s[2]
    if(os.path.exists(f"{inp}/OUTPUT")):
        with open(f"{inp}/OUTPUT") as f:
            lines = f.readlines()
            try:
                i = lines.index("Approximate 3D Diffusion Coefficients and square root of MSDs:\n")
                i += 2
                count += 1
                vals = lines[i].split()

                dc[sigma][direction] = vals[1]

                msd[sigma][direction] = vals[2]

            except:
                print(inp, "oombi output")

with open('dc.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headings)
    writer.writeheader()
    for d in dc:
        # print(dc[d])
        writer.writerow(dc[d])

with open('msd.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=headings)
    writer.writeheader()
    for m in msd:
        # print(dc[d])
        writer.writerow(msd[m])
print(count)