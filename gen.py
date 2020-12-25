from opensimplex import OpenSimplex
from perlin_noise import PerlinNoise

import PIL
from PIL import Image

import numpy as np
import math
import random


tmp = OpenSimplex(random.randint(0,10000000000))
noise = PerlinNoise(octaves=5, seed=random.randint(0,10000000000))


def command(coords):
	return("fill " + str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2]) + " " + str(coords[0]) + " " + str(coords[1] - 5) + " " + str(coords[2]) + " " + "oak_planks" + "\n")
	#return("setblock " + str(coords[0]) + " " + str(coords[1]) + " " + str(coords[2]) + " stone" + "\n")


def simplex_gen(map_size=10000):
	f = open('gen.mcfunction', "a")
	length = int(map_size**(0.5))
	for x in range(-1*length, 1+length):
		for y in range(-1*length, 1+length):

			#calculating hight
			hight = tmp.noise2d(x=x, y=y)
			adj_hight = round(((((hight - -1) * (255 - 0)) / (1 - -1)) + 0)/30) + 50

			#writing to file
			f.write(command([x, adj_hight, y]))
	f.close()

def perlin_gen(map_size=20000):
	f = open('gen.mcfunction', "a")
	length = int(map_size**(0.5))
	for x in range(length):
		for y in range(length):

			#calculating hight
			hight = noise([x/length, y/length])
			adj_hight = round(((((hight - -1) * (255 - 0)) / (1 - -1)) + 0))
			#print(hight, adj_hight)

			#writing to file
			f.write(command([x, adj_hight, y]))
	f.close()

def perlin_img_gen(image, map_size=200000):
	f = open('gen.mcfunction', "a")
	length = int(map_size**(0.5))
	data = np.array(Image.open(image).convert('L').resize((length, length)))
	for x in range(length):
		for y in range(length):
			 hight = int(data[x][y]/5) + 20
			 f.write(command([length-x, hight, y]))
	f.close()


#simplex_gen()
#perlin_gen()
perlin_img_gen('perlin-noise.png')
