# Graph Interpolation
This project is a console application that allows you to interpolate a function. Interpolation is the search for unknown intermediate values of some function from the available discrete set of its known values in a certain way. The plot of the interpolated function looks smoother. It is a **pet project** to get experience with **Python**.

This app **can**:
* Interpolate the function
* Find the extrema of the function
* Plot the function

## Requirements
* Python 3.10.8

## Install
**Step 1**. Install [Python](https://www.python.org/downloads/).
**Step 2**. Install Python libraries.
For this application to work, you need to download several libraries. To install, use the pip package installer.
1. Install **scipy** to implement interpolation in Python.
```
pip install scipy
```
2. Install **matplotlib** to plot the function in Python.
```
pip install matplotlib
```
**Step 3**. Clone this repository to your local computer.
```
git clone https://github.com/SpaceLacuna/graph-interpolation.git
```
## Running
Since this is a console application, you need to work on the command line.
**Step 1**. Run cmd.exe.
**Step 2**. Navigate to the root folder of this project.
```
cd ...\graph-interpolation
```
**Step 3**. Run file inter.py.
```
python inter.py
```
## Usage Example
If you did everything correctly, the program will ask you to enter the name of the file in which the values are stored. Based on these values, a chart will be built and extrema will be found. Each number in this file **must** start on a new line, as shown in the example below. It is advisable to use the .txt extension.

![image](https://user-images.githubusercontent.com/115897935/196065344-38da4756-94c3-4c15-ae1c-a6873f23c1d6.png)

As a result, a window will open in which the graph of the function for the given numbers and the graph of the interpolated function will be plotted, and the extrema of the function will also be found.

![image](https://user-images.githubusercontent.com/115897935/196065522-f910f433-a8cd-45e0-99e6-397c09252a09.png)
