# plotxl
plotxl is a python program that helps you plot linear line graphs from the values stored in an excel file.
It can be used to create plots for the same inputs under various conditions in a single graph.

## Prerequisites
Make sure you have ```matplotlib```, ```xlrd``` and ```argparse``` python libraries installed.

## Usage
The program takes values stored in an excel in a specific format and generates line graphs.

### Preparation of excel file 
The general format of the excel file should be as shown below. The image shown is for 2 conditions. You can add as many conditions as you want.

1. Always keep the first cell (A1) empty.
2. Enter the x coordinates one by one in the cells below A1.
3. Enter the labels of the conditions one by one in the cells to the right of A1.
4. Enter the y coordinates against the corresponding x coordinate under the appropriate condition label.

![format](https://user-images.githubusercontent.com/49730342/81736342-078e1e80-94b4-11ea-87fe-1c9aaa778492.png)

For example,
Let ```y = mx```. The aim is to plot 5 values of ```y``` against ```x``` for the conditions ```m = 1``` and ```m = 2```.
The value of x is varied from 1 to 5. The excel file for the plot will be as shown.

![example](https://user-images.githubusercontent.com/49730342/81736378-1674d100-94b4-11ea-87da-657af4c0c54f.png)


### Plotting
To plot the graph using plotxl, run the following command.

```bash 
    python3 plotxl.py -f path_to_file
```
And the obtained plot is shown below.

![plot](https://user-images.githubusercontent.com/49730342/81736695-9733cd00-94b4-11ea-9d50-833ce519eff9.png)

The path to the file along with .xlsx extension is required by the program to plot the graph.
 
 ### Command line arguments
 ```
  -h, --help            show this help message and exit

  -g, --grid            Enable grid

  -d, --detail          Enter details like title and units

  -x, --xval            Every x value in the input file will be shown on x-axis. By default, 
  						the program decides the points to be displayed on the axes.

  -t, --transpose       take transpose of excel sheet

  -i, --inside			show legends inside plot, by default it is shown outside the plot
  
  -f FILE, --file FILE  Eath to input excel file
```


