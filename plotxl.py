from matplotlib import pyplot as plt
import xlrd
import argparse	


ap = argparse.ArgumentParser()

ap.add_argument("-g", "--grid", action = "store_true",
	help = "enable grid")

ap.add_argument("-d", "--detail", action = "store_true",
	help = "enter details like title and units")
ap.add_argument("-x", "--xval", action = "store_true", 
	help = "every x value in the input file will be shown on x-axis.")

ap.add_argument("-f", "--file", required = True,
	help = "path to input excel file")

args = vars(ap.parse_args())

x_unit = ""
y_unit = ""
title = "Plot"

x_label = "X-axis"
y_label = "Y-axis"

if args['detail']:
	print("<<<===============================================>>>")
	print("")

	title = input("Enter title of the graph: ")
	print("<<<===============================================>>>")
	print("")
	
	x_label = input("X axis label: ")
	print("<<<===============================================>>>")
	print("")
	
	x_unit = input("Unit of X axis: ")
	if x_unit != '':
		x_unit = "(" + x_unit + ")"
	print("<<<===============================================>>>")
	print("")
	
	y_label = input("Y axis label: ")
	print("<<<===============================================>>>")
	print("")
	
	y_unit = input("Unit of Y axis: ")
	if y_unit != '':
		y_unit = "(" + y_unit + ")"
	print("<<<===============================================>>>")
	print("")
	
wb = xlrd.open_workbook(args["file"])
sheet = wb.sheet_by_index(0)

# x axis values
xval = [] 

# constant parameter
lines = []

for i in range(1,sheet.nrows):
    xval.append(sheet.cell_value(i,0))


for i in range(1,sheet.ncols):
		lines.append(sheet.cell_value(0, i))


yval = []
for k in range(1, sheet.ncols):
    yval.append([])

index = 0    
for i in range(1,sheet.ncols):
    for j in range(1,sheet.nrows):
        yval[index].append(sheet.cell_value(j,i))
    index = index + 1


for i in range(0, len(yval)):
	plt.plot(xval, yval[i], label = str(lines[i]), marker= "o")

if args["xval"]:
	plt.xticks(xval)

# naming the x axis 
plt.xlabel(x_label + x_unit) 
# naming the y axis 
plt.ylabel(y_label + y_unit) 
# giving a title to my graph 
plt.title(title) 

# show a legend on the plot 
if lines != ['']:
	plt.legend() 
if args["grid"]:
	plt.grid()  
# function to show the plot 
plt.show() 