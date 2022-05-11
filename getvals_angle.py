from inputs import inputs
from angles import anglemap
import os

dc = ["angle,DC\n"]
msd = []
count = 0


for inp in inputs:
    d_s = inp.split("_",1)[1]
    angle = anglemap[d_s]
    if(os.path.exists(f"{inp}/OUTPUT")):
        with open(f"{inp}/OUTPUT") as f:
            lines = f.readlines()
            try:
                i = lines.index("Approximate 3D Diffusion Coefficients and square root of MSDs:\n")
                i += 2
                count += 1
                vals = lines[i].split()

                dc.append(f"{angle},{vals[1]}\n")

                msd.append(f"{angle},{vals[2]}\n")

            except:
                print(inp, "oombi output")

with open('dc_angle.csv', 'w') as f:
    print("hi")
    f.writelines(dc)

with open('msd_angle.csv', 'w') as f:
    f.writelines(msd)
print(count)