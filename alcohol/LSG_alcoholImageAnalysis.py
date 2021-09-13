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

# main
def main():
<<<<<<< HEAD:alcohol/LSG_alcoholImageAnalysis.py
    img_path = "C:\\codeImage\\lisa.jpg"     # the image path 
    img_bgr = roi_anyRange(img_path)            # select the any range
    getHSV(img_bgr)                             # convert image to HSV and get h,s,v

    cv2.waitKey(0)                              # wait exit

# select the any range 
def roi_anyRange(img_path):
    img_org = cv2.imread(img_path)              # load original image
=======
    gui()
>>>>>>> 9cf041791542249b9b96548e1bab140f20ba9d81:alcoholImageAnalysis.py

#gui
def gui():
    mainWindow = createWindow('mainWindow', '500x500')
    ButtonGUIs(mainWindow)
    mainWindow.mainloop()

# Processing image
def ProcessingImage():
    imagePath = selectFile()            # Select picture from path
    
<<<<<<< HEAD:alcohol/LSG_alcoholImageAnalysis.py
    cv2.imshow("img_roi", img_roi)                              # show the roi image
    cv2.imwrite("img_roi.jpg", img_roi)       # save the roi image
=======
    if imagePath == "": return          # if cancel the selection, then return
>>>>>>> 9cf041791542249b9b96548e1bab140f20ba9d81:alcoholImageAnalysis.py
    
    imageROI = roi_anyRange(imagePath)  # select the interesting of the image
    getHSV(imageROI)                    # get the H, S, V values of the image respective.

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

<<<<<<< HEAD:alcohol/LSG_alcoholImageAnalysis.py
=======
# plotting the trend graph
def trendGraph():
    return


>>>>>>> 9cf041791542249b9b96548e1bab140f20ba9d81:alcoholImageAnalysis.py
if __name__ == '__main__':
    main()