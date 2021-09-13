# gui Sample : https://www.cnblogs.com/shwee/p/9427975.html

import tkinter as tk    # import tkinter

#main
def main():
    myWindow = windowGUI()      # create a window
    #helloGUI(myWindow)         # shwo texts on the window
    ButtonGUI(myWindow)         # create a button on the window

    myWindow.mainloop()         # refresh window

def windowGUI():
    myWindow = tk.Tk()                  # instantiate an object and create a window
    myWindow.title('myWindow')          # naming the window    
    myWindow.geometry('500x300')        # setting the window size
    return myWindow

# show helloWorld on the window
def helloGUI(mainWindow):
    myLabel = tk.Label(mainWindow, text = 'HelloWorld', bg = 'green', font = ('Arial', 12), width = 10, height = 3)  #setting the lable
    myLabel.pack()                      # placing the lable
    

# define a button on the window
# 普通的按钮很容易被创建，仅仅指定按钮的内容（文本、位图、图象）和一个当按钮被按下时的回调函数
def ButtonGUI(mainWindow):
    myButton = tk.Button(mainWindow, text = 'hit me', width=10, height=1, command = mainWindow.quit)
    myButton.pack()  

if __name__ == '__main__':
    main()