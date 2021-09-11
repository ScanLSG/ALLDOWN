# 1. plotting a line.
# 2. plotting more lines
# 3. plotting a line with customize style
# 4. DOTO: Bar Chart
# 5. DOTO: Histogram
# 6. DOTO: Scatter plot
# 7. DOTO: Pie-chart


import matplotlib.pyplot as plt

#main
def main():
    #aLine()
    #MultLines()
    #customizeLine()
    showLabel()

# show the label
def showLabel():
    plt.xlabel('x-axis')            # naming the x axis
    plt.ylabel('y-axis')            # naming the y axis
    plt.show()                      # show the plot

# plotting a line
def aLine():
    x = [1, 2, 3]   # x axis values
    y = [4, 5, 6]   # y axis values
    plt.plot(x, y)  # plotting the points
    plt.title('the First graph')    # naming the window

# plotting two or more lines on same plot
def MultLines():
    x1 = [1, 2, 3]
    y1 = [2, 4, 1]
    x2 = [1, 2, 3]
    y2 = [3, 6, 2]
    
    plt.plot(x1, y1, label = 'Line1')
    plt.plot(x2, y2, label = 'Line2')
    plt.title('two lines on same graph!')
    plt.legend()    #show a legend of the lines

# customization of plots
def customizeLine():
    x = [1,2,3,4,5,6] 
    y = [2,4,1,5,2,6]

    #plotting the points
    plt.plot(x, y, color = 'green', linestyle = 'dashed', linewidth = 4,
                marker = 'o', markerfacecolor = 'red', markersize = 12)
    
    #setting x and y axis range
    plt.xlim(1, 8)
    plt.ylim(1, 8)

    plt.title('customize style')

if __name__ == '__main__':
    main()