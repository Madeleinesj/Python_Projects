import tkinter as tk
from tkinter import *
import webbrowser


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")        

        #Creates button for Default HTML Page
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=3, padx=(10, 10), pady=(200,15))

        #Customtext button created
        self.customtext_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        #Customtext button placement
        self.customtext_btn.grid(row=2, column=1, padx=(50, 50), pady=(200, 15))

        #Creates textbox for custom text
        self.entry = Entry(master, width= 42)
        self.entry.grid(row=2, column=2, padx=(10, 40), pady=(10,15))
        label= Label(root, text="Enter custom text or click the Default HTML page button", font=("Helvetica 13"))
        label.grid(row=1, column=2, padx=(10, 40), pady=(10,15))
        #Label is not rendering on the window
        L1 = Label(master, text="Enter custom text or click the Default HTML page button")
        
        
        
    #function for default text and opens html page.
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

        #customtext function
    def customHTML(self):
        entry = self.entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + entry + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    


            

    


if __name__=="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()


