#####################################################################
# 1. select the ROI in RGB-------------get                          #
# 2. RGB->HSV--------------------------get                          #
# 3. output the ROI :H, S, V-----------get                          #
# 4. GUI-------------------------------get                          #
# 4. plot the diagram------------------                             #
#####################################################################

# import pack
import cv2
import numpy
import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import glob

# main
def main():
    gui()

#gui
def gui():
    mainWindow = createWindow('mainWindow', '500x500')
    ButtonGUIs(mainWindow)
    
    mainWindow.mainloop()

# Processing image
def ProcessingImage():
    imagePath = selectFile()            # Select picture from path

    if imagePath == "": return          # if cancel the selection, then return
    
    imageROI = roi_anyRange(imagePath)  # select the interesting of the image
    HSVarray = getHSV(imageROI)         # get the H, S, V values of the image respective.

    image_time = int(imagePath.split('/')[-1].replace('.jpg',''))
    print(image_time)
    trendGraph(image_time, HSVarray[0], HSVarray[1], HSVarray[2])

# create a window
def createWindow(windowName, windowSize):
    myWindow = tk.Tk()                  # instantiate an object and create a window
    myWindow.title(windowName)          # naming the window    
    myWindow.geometry(windowSize)       # setting the window size
    return myWindow

# create a button
def ButtonGUIs(mainWindow):
    openFile = tk.Button(mainWindow, text = 'openFile', command = ProcessingImage)
    quitWindow = tk.Button(mainWindow, text = 'quit', command = mainWindow.quit)
    openFile.pack(expand = True)
    quitWindow.pack(expand = True)

#def exitWindows(): 

# select File
def selectFile():
    fileTypes = (('jpeg files','*.jpg'), ('png files','*.png'), ('All files', '*.*'))
    filePath = fd.askopenfilename(title = 'Open a file', initialdir = '.\\', filetypes = fileTypes) # allows a single fileselection
    return filePath

# select the any range 
def roi_anyRange(img_path):
    img_org = cv2.imread(img_path)
    roi_range = cv2.selectROI('img_org', img_org, False, False);        
    img_roi = img_org[int(roi_range[1]) : int(roi_range[1]+roi_range[3]), 
                      int(roi_range[0]) : int(roi_range[0]+roi_range[2]), :]    # (x_min, y_min, w, h)
    cv2.imshow("img_roi", img_roi)
    # cv2.imwrite("img_roi.jpg", img_roi)

    return img_roi

# convert image to HSV and get h,s,v
def getHSV(img_bgr):
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                  # Convert the BGR image to HSV
    h, s, v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]      # parse HSV
    print("the image H:", numpy.mean(h))
    print("the image V:", numpy.mean(v))
    print("the image S:", numpy.mean(s))
    HSVarray = [numpy.mean(h), numpy.mean(v), numpy.mean(s)]
    return HSVarray

# plotting the trend graph
def trendGraph(image_time, H_value, S_value, V_value):
    time_axis = image_time
    print(time_axis)
    H_values = H_value
    S_values = S_value
    V_values = V_value

    plt.xlabel('Time')
    plt.ylabel('HSV_value')
    plt.title('the HSV trend graph')
    plt.plot(time_axis, H_values, label = 'H')
    plt.plot(time_axis, S_values, label = 'S')
    plt.plot(time_axis, V_values, label = 'V')
    plt.legend()
    plt.plot(time_axis, H_value, color = 'blue', linestyle = 'dashed', linewidth = 3,
            marker = 'o', markerfacecolor = 'blue', markersize = 12)
    plt.plot(time_axis, S_value, color = 'red', linestyle = 'dashed', linewidth = 3,
            marker = 'o', markerfacecolor = 'red', markersize = 12)
    plt.plot(time_axis, V_value, color = 'green', linestyle = 'dashed', linewidth = 3,
            marker = 'o', markerfacecolor = 'green', markersize = 12)
    plt.xlim(0)
    plt.ylim(0)
    plt.show()

if __name__ == '__main__':
    #inputs = glob.glob(r'D:\Code\ALLDOWN\ALLDOWN\alcoholImage\*.jpg')
   #for i in inputs:
        #print(i.split('\\')[-1].replace('.jpg',''))
    
    main()