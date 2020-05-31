from matplotlib import pyplot as plt
import xlrd
import argparse	


def get_Val (sh, t_flag):

	# x-axis values
	x_val = [] 

	# Labels of conditions
	lines = []

	n_lines = sh.ncols
	n_xval = sh.nrows
	
	for i in range(1,n_xval):
		x_val.append(sh.cell_value(i,0))


	for i in range(1,n_lines):
			lines.append(sh.cell_value(0, i))
		
	if t_flag:
		(x_val, lines, n_lines, n_xval) = (lines, x_val, n_xval, n_lines)
			


	y_val = []
	for k in range(1, n_lines):
		y_val.append([])
	
	index = 0    
	for i in range(1, n_lines):
		for j in range(1, n_xval):
			if t_flag:
				y_val[index].append(sh.cell_value(i, j))
			else:
				y_val[index].append(sh.cell_value(j, i))
		index = index + 1
	return x_val, y_val, lines


def plot_graph(xval, yval, lines):

	for i in range(0, len(yval)):
		plt.plot(xval, yval[i], label = (str(lines[i]) + " " + c_unit), marker= "o")

	if args["xval"]:
		plt.xticks(xval)


	plt.xlabel(x_label + x_unit) 
	
	plt.ylabel(y_label + y_unit) 
	
	plt.title(title) 
 
	if lines != ['']:
		if args["inside"]:
			plt.legend()
		else:
			plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	if args["grid"]:
		plt.grid()  
	plt.tight_layout()
 
	plt.show() 


ap = argparse.ArgumentParser()

ap.add_argument("-g", "--grid", action = "store_true",
	help = "enable grid")

ap.add_argument("-d", "--detail", action = "store_true",
	help = "enter details like title and units")

ap.add_argument("-x", "--xval", action = "store_true", 
	help = "every x value in the input file will be shown on x-axis.")

ap.add_argument("-t", "--transpose", action = "store_true",
	help = "take transpose of excel sheet")

ap.add_argument("-i", "--inside", action = "store_true",
	help = "Show legends inside plot boundary")

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
	
	c_unit = input("Unit of condition: ")
	print("<<<===============================================>>>")
	print("")
	
wb = xlrd.open_workbook(args["file"])
sheet = wb.sheet_by_index(0)

xval, yval, lines = get_Val(sheet, args["transpose"])

plot_graph(xval, yval, lines)
