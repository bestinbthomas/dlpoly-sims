from inputs import inputs
import os

ROOT = "C:\\Users\\Navneet\\Documents\\MD-MC_FYP\\dlpoly-sims-main"
# print(inputs)

i = 5

while (i<40):
    input_dir = ROOT + "\\" +inputs[i]
    print(input_dir)
    os.system(f"cd {input_dir} && DLPOLY.Z")
    i+= 1
