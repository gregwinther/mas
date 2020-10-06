import glob
from matplotlib import pyplot as plt 
import numpy as np
import argparse

arguments = argparse.ArgumentParser()
arguments.add_argument("--input_folder", type=str)

args = arguments.parse_args()

path = args.input_folder

files = glob.glob(path + "/*.txt")

data = []
for file in files:
    data.append(np.loadtxt(file))
    

for sim in data:
    plt.plot(sim[:, 0], sim[:, 1], color=(0.1, 0.1, 1, 0.5), linewidth=1)

sim_mean = np.mean(np.array(data), axis=0)
plt.plot(data[0][:, 0], sim_mean[:, 1], color=(0.1, 0.1, 1, 1))

plt.show()