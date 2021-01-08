#This code is used to create Stokes Curve from our Converted folder
#The Converted folder contains 37 measurements (from 0 degree to 360 degree) in form of *.asc
#This code will return a file containing the maximum value from those 37 files
#To make it work in Origin: Create a workbook and add the first column is angle (must be in radians)

yourpath = r'C:\Users\hangu\OneDrive\Desktop\Test\Converted'

import os
 
def number_name(file_name):
     return int(file_name[0:-4])

stokes_curve = []

for root, dirs, files in os.walk(yourpath, topdown=False):
    files = sorted(files, key=number_name)
    for name in files:
        #print(name)
        md = open(os.path.join(root, name), 'r')

        intensity_lst = []
        for line in md:
            line = line.split()
            intensity_lst.append(int(line[1]))

        stokes_curve.append(max(intensity_lst))

md.close()       

#Create a new file containing the stokes_curve:
new_file = open("stokes_curve.txt", "w")
for item in stokes_curve:
    print(item)
    new_file.write(str(item)+'\n')
new_file.close() 

