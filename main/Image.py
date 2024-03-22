#Programmers: Nived Leju Ramachandran Sonia, Aarez Ansari , Prince Lucky-Worluh and Syed Airaj Hussain
#Date: 2022-04-12

#importing libraries
import os
import pathlib

import time


import matplotlib.pyplot as plt
import numpy
import numpy as np
from PIL import Image

#library for ui
import tkinter as tk
from tkinter import simpledialog


#getting the start time
start = time.time()

#extracting for input dialog
ROOT = tk.Tk()
ROOT.withdraw()

# the input dialog
path = simpledialog.askstring(title="Image prompt", prompt="Please enter the path of the image")


#storing directory path
cwd = os.getcwd()

#storing the image folder path
MNIST_path = os.path.join(cwd, 'MNIST_DS')

#storing sub-folders path
classes = os.listdir(MNIST_path)

#storing starting path
opath = (MNIST_path, 0)

#opening txt files
Ba = open("Barcode.txt", "w")
Ad = open("Address.txt", "w")

#clearing the txt files
Ba.write("")
Ad.write("")
Ba.close()
Ad.close()


#creating var arr to store pixel paths as array
pixel = np.array(Image.open(path))

proj1 = numpy.sum(pixel, axis=1)  # 0 degree projection

# Average for 0 degree projection
proj1avg = sum(proj1) / len(proj1)

# 90 Degree Projection
proj2 = numpy.sum(pixel, axis=0)

proj2avg = sum(proj2) / len(proj2)

# 45 Degree Projection
proj3 = [np.trace(pixel, offset=i) for i in range(-np.shape(pixel)[0] + 2, np.shape(pixel)[1] - 1)]

# 135 Degree projection
proj3avg = numpy.average(proj3)

proj4 = [np.trace(np.fliplr(pixel), offset=i) for i in range(-np.shape(pixel)[0] + 2, np.shape(pixel)[1] - 1)]
proj4avg = numpy.average(proj4)

#projections
P1 = []
P2 = []
P3 = []
P4 = []

#hamming distance
h = []

# Converting to barcode(0 angle project array)
for k in range(len(proj1)):
    if proj1[k] <= proj1avg:
        P1.append(0)
    else:
        P1.append(1)


for r in range(len(proj2)):
    if proj2[r] <= proj2avg:
        P2.append(0)
    else:
        P2.append(1)


for l in range(len(proj3)):
    if proj3[l] <= proj3avg:
        P3.append(0)
    else:
        P3.append(1)


for y in range(len(proj4)):
    if proj4[y] <= proj4avg:
        P4.append(0)
    else:
        P4.append(1)


UserB = P1 + P2 + P3 + P4
print("User image barcode: ", UserB)
print('\n')

possible = []
wantedpath = " "
maxH = 100


for c in classes:

    images_path = os.path.join(MNIST_path, c)


    for image_path in pathlib.Path(images_path).iterdir():
        path = image_path


        pixel = np.array(Image.open(path))

        proj1 = numpy.sum(pixel, axis=1)  # 0 degree projection

        # Average for 0 degree projection
        proj1avg = sum(proj1) / len(proj1)

        # 90 Degree Projection
        proj2 = numpy.sum(pixel, axis=0)

        proj2avg = sum(proj2) / len(proj2)

        # 45 Degree Projection
        proj3 = [np.trace(pixel, offset=i) for i in range(-np.shape(pixel)[0] + 2, np.shape(pixel)[1] - 1)]

        # 135 Degree projection
        proj3avg = numpy.average(proj3)

        proj4 = [np.trace(np.fliplr(pixel), offset=i) for i in range(-np.shape(pixel)[0] + 2, np.shape(pixel)[1] - 1)]
        proj4avg = numpy.average(proj4)

        #projections
        P1 = []
        P2 = []
        P3 = []
        P4 = []

        #hamming distance
        h = []

        Ba = open("Barcode.txt", "a")
        Ad = open("Address.txt", "a")


        # Converting to barcode(0 angle project array)
        for k in range(len(proj1)):
            if proj1[k] <= proj1avg:
                P1.append(0)
            else:
                P1.append(1)


        for r in range(len(proj2)):
            if proj2[r] <= proj2avg:
                P2.append(0)
            else:
                P2.append(1)

        for l in range(len(proj3)):
            if proj3[l] <= proj3avg:
                P3.append(0)
            else:
                P3.append(1)


        for y in range(len(proj4)):
            if proj4[y] <= proj4avg:
                P4.append(0)
            else:
                P4.append(1)


        FileB = P1 + P2 + P3 + P4
        Ba.write(str(FileB) + "\n")
        Ad.write(str(path) + "\n")



        h=0
        for x in range(len(UserB)):

            if(UserB[x]!=FileB[x]):
                    #hamming distance
                    h = h + 1




        #setting max H
        if h!=0:
            if h < maxH:
                maxH = h
                wantedpath = path
            if h == maxH:
                possible.append(str(wantedpath))

#getting the end time
endtime = time.time()

#getting exec time
total_time = endtime - start

#Printing closest path, and possible options to the image

print('\n')
print("Path to CLOSEST IMAGE: ", wantedpath )
print('\n')
print("Possible options could be: ")
m=0

#printing all possible options to inputted image
while(m<len(possible)):
    print(possible[m])
    m+=1

print ('\n','Total Execution time: ', total_time, 'seconds')



