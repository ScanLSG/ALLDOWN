# Open a picture in the selected path
# open file:  https://www.pythontutorial.net/tkinter/tkinter-open-file-dialog/

# import pack
import tkinter as tk
from tkinter import filedialog as fd    # open file dialog
# from tkinter.messagebox import showinfo

# main
def main():
    gui()

# gui
def gui():
    mainWindow = createWindow('mainWindow', '500x500')
    ButtonGUI(mainWindow)
    mainWindow.mainloop()

# create a window
def createWindow(windowName, windowSize):
    myWindow = tk.Tk()                  # instantiate an object and create a window
    myWindow.title(windowName)          # naming the window    
    myWindow.geometry(windowSize)       # setting the window size
    return myWindow

# create a button
def ButtonGUI(mainWindow):
    myButton = tk.Button(mainWindow, text = 'openFile', command = selectFile)
    myButton.pack(expand = True)  

# select File
def selectFile():
    fileTypes = (('jpeg files','*.jpg'), ('png files','*.png'), ('All files', '*.*'))
    fileName = fd.askopenfilename(title = 'Open a file', initialdir = '.\\', filetypes = fileTypes) # allows a single fileselection
    # showinfo(title = 'Selected File', message = fileName)

if __name__ == '__main__':
    main()