from matplotlib import pyplot as plt
import xlrd
import argparse	

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True,
	help="path to input excel file")
ap.add_argument("-d", "--detail", action="store_true",
	help="Enter details like title and units")
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
	x_unit = "("+input("Unit of X axis: ") + ")"
	print("<<<===============================================>>>")
	print("")
	y_label = input("Y axis label: ")
	print("<<<===============================================>>>")
	print("")
	y_unit = "("+input("Unit of Y axis: ") + ")"
	print("<<<===============================================>>>")
	print("")
	
wb = xlrd.open_workbook(args["file"])
sheet = wb.sheet_by_index(0)

# x axis values
x_ax = [] 

# constant parameter
lines = []

for i in range(1,sheet.nrows):
    x_ax.append(sheet.cell_value(i,0))


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
	plt.plot(x_ax, yval[i], label = str(lines[i]), marker= "o")
    
# naming the x axis 
plt.xlabel(x_label + x_unit) 
# naming the y axis 
plt.ylabel(y_label + y_unit) 
# giving a title to my graph 
plt.title(title) 
  
# show a legend on the plot 
plt.legend() 
  
# function to show the plot 
plt.show() 