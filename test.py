# import pack
import cv2
import numpy
import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import glob
from numpy.core.shape_base import hstack

from numpy.lib.shape_base import hsplit

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
    imagePaths = selectFile()            # Select picture from path

    #print(type(imagePaths))             # test--------------------------<class 'tuple'>       
    #print(imagePaths)                   # test--------------------------paths

    if imagePaths == "": return          # if cancel the selection, then return
    
    HSV_values = roi_anyRange(imagePaths)  # select the interesting of the images
    # HSVarray = getHSV(imageROI)         # get the H, S, V values of the image respective.

    # image_time = int(imagePath.split('/')[-1].replace('.jpg',''))
    # print(image_time)
    trendGraph(HSV_values)

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
    filePaths = fd.askopenfilenames(title = 'Open a file', initialdir = '.\\', filetypes = fileTypes)
    return filePaths

# select the any range 
def roi_anyRange(img_paths):
    #HSV_values = numpy.array([0, 0, 0, 0])
    HSV_values = []
    orderNum = 0

    for img_path in img_paths:
        img_org = cv2.imread(img_path)
        roi_range = cv2.selectROI('img_org', img_org, False, False);
        img_roi = img_org[int(roi_range[1]) : int(roi_range[1]+roi_range[3]), 
                          int(roi_range[0]) : int(roi_range[0]+roi_range[2]), :]    # (x_min, y_min, w, h)
        #cv2.imshow("img_roi", img_roi)
        #print("./imageROI/"+img_path.split('/')[-1])                               # test

        img_hsv = cv2.cvtColor(img_roi, cv2.COLOR_BGR2HSV)                  # Convert the BGR image to HSV
        h, s, v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]      # parse HSV
        HSV_value = [orderNum, numpy.mean(h), numpy.mean(v), numpy.mean(s)] #list
        #HSV_values = numpy.concatenate((HSV_values, HSV_value))
        HSV_values.append(HSV_value)
        #HSV_values.append(HSV_values, HSV_value, axis = 0)
        print(HSV_values)
        #HSV_values.append(HSV_value)
        cv2.imwrite("./imageROI/"+str(orderNum)+".jpg", img_roi)            # save the image
        orderNum += 1


    return numpy.array(HSV_values)

# convert image to HSV and get h,s,v
# def getHSV(img_bgr):
#     img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)                  # Convert the BGR image to HSV
#     h, s, v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]      # parse HSV
#     print("the image H:", numpy.mean(h))
#     print("the image V:", numpy.mean(v))
#     print("the image S:", numpy.mean(s))
#     HSVarray = [numpy.mean(h), numpy.mean(v), numpy.mean(s)]
#     return HSVarray

# plotting the trend graph
def trendGraph(HSV_values):
    #下一步：將得到的數據畫成點
    print(type(HSV_values))
    print(HSV_values)

    time_axis = HSV_values[:,0]
    H_values = HSV_values[:,1]
    S_values = HSV_values[:,2]
    V_values = HSV_values[:,3]
    print(time_axis)
    print(H_values)
    print(S_values)
    print(V_values)

    # time_axis = list(map(lambda HSV_values: HSV_values[0], list))
    # H_values = list(map(lambda HSV_values: HSV_values[1], list))
    # S_values = list(map(lambda HSV_values: HSV_values[2], list))
    # V_values = list(map(lambda HSV_values: HSV_values[3], list))

    
    plt.xlabel('Time')
    plt.ylabel('HSV_value')
    plt.title('the HSV trend graph')
    plt.plot(time_axis, H_values, label = 'H')
    plt.plot(time_axis, S_values, label = 'S')
    plt.plot(time_axis, V_values, label = 'V')
    plt.xlim(0)
    plt.ylim(0)
    plt.legend()
    # plt.plot(time_axis, H_value, color = 'blue', linestyle = 'dashed', linewidth = 3,
    #         marker = 'o', markerfacecolor = 'blue', markersize = 12)
    # plt.plot(time_axis, S_value, color = 'red', linestyle = 'dashed', linewidth = 3,
    #         marker = 'o', markerfacecolor = 'red', markersize = 12)
    # plt.plot(time_axis, V_value, color = 'green', linestyle = 'dashed', linewidth = 3,
    #         marker = 'o', markerfacecolor = 'green', markersize = 12)
    
    plt.show()

if __name__ == '__main__':

    main()