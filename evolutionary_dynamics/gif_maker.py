import glob
import os
import imageio
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", "-P", help="Folder with images", type=str)
parser.add_argument("--outfile", "-O", help="Output file name", type=str)
parser.add_argument(
    "--duration", "-D", help="Time between images", type=float, default=0.2
)
args = parser.parse_args()

path = args.path
files = [file for file in glob.glob(path + "*.png")]
files = sorted(files, key=os.path.getmtime)

print(len(files))

images = []
for file in files:
    images.append(imageio.imread(file))

if args.outfile == None:
    imageio.mimsave("./ani.gif", images, duration=args.duration)
else:
    imageio.mimsave(f"./{args.outfile}", images, duration=args.duration)
