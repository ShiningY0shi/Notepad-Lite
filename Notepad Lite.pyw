from tkinter import *
import getpass
import os

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create some widgets"""

        #label will never change, so i don't have to set this to anything
        #other than the master

        #name label, row 0 column 0
        Label(self,
              text = "Name:"
              ).grid(row = 0, column = 0, sticky = W)

        #name entry box, row 0 column 1
        self.name_entry = Entry(self)
        self.name_entry.grid(row = 0, column = 1, sticky = W)

        #path label, row 0 column 2
        Label(self,
              text = "Save to:"
              ).grid(row = 0, column = 2, sticky = W)

        #path entry box, row 0 column 3
        self.path_entry = Entry(self, width = 26)
        self.path_entry.insert(END, "C:\\Users\\" + getpass.getuser() + "\\Desktop")
        self.path_entry.grid(row = 0, column = 3, sticky = W)
        
        #open button, row 1 column 0
        self.open_button = Button(self, text = "Open", command = self.open)
        self.open_button.grid(row = 1, column = 0, sticky = E, ipadx = 2)

        #save button, row 2 column 0
        self.save_button = Button(self, text = "Save", command = self.save)
        self.save_button.grid(row = 2, column = 0, sticky = E, ipadx = 4.3)

        #delete button, row 3 column 0
        self.delete_button = Button(self, text = "Delete", command = self.delete)
        self.delete_button.grid(row = 3, column = 0, sticky = E)

        #clear button, row 4 column 0
        self.clear_button = Button(self, text = "Clear", command = self.clear)
        self.clear_button.grid(row = 4, column = 0, sticky = E, ipadx = 2.5)

        #text entry box, row 1-4 column 1-3
        self.text_entry = Text(self, width = 41, height = 12, wrap = WORD)
        self.text_entry.grid(row = 1, column = 1, rowspan = 4, columnspan = 3, sticky = W)

        #status display box, row 5 column 0-4
        self.status_display = Label(self, text = "Ready.")
        self.status_display.grid(row = 5, column = 0, columnspan = 4, sticky = W)

    def open(self):
        name = self.name_entry.get()
        path = self.path_entry.get()

        try:
            text_file = open(path + "\\" + name + ".txt", "r")
            contents = text_file.read()
            self.text_entry.delete(0.0, END)
            self.text_entry.insert(0.0, contents)
            self.status_display["text"] = path + "\\" + name + ".txt opened."
        except:
            if not os.path.exists(path):
                self.status_display["text"] = "\"" + path + "\" is not a valid path!"
            else:
                self.status_display["text"] = "Error trying to open " + name + ".txt, file does not exist!"

    def save(self):
        name = self.name_entry.get()
        path = self.path_entry.get()

        if os.path.exists(path):
            contents = self.text_entry.get('1.0', END)
            try:
                text_file = open(path + "\\" + name + ".txt", "w")
                text_file.write(contents)
                text_file.close()
                self.status_display["text"] = name + ".txt successfully saved to " + path
            except:
                self.status_display["text"] = name + ".txt is an invalid filename!"
        else:
            self.status_display["text"] = "Cannot save to \"" + path + "\" because it does not exist!" 
        
        #legacy code that doesn't implement the path entry object
        """
        contents = self.text_entry.get('1.0', END)
        try:
            text_file = open(self.name_entry.get() + ".txt", "w")
            text_file.write(contents)
            text_file.close()
            self.status_display["text"] = self.name_entry.get() + ".txt \
successfully saved."
        except:
            self.status_display["text"] = "Error while trying to save " + self.name_entry.get() + ".txt"
        """

        
    def delete(self):
        name = self.name_entry.get()
        path = self.path_entry.get()

        if os.path.exists(path):
            try:
                text_file = open(path + "\\" + name + ".txt", "r")
                text_file.close()
                os.remove(path + "\\" + name + ".txt")
                self.status_display["text"] = name + ".txt successfully deleted from " + path
            except:
                self.status_display["text"] = "Cannot delete " + name + ".txt; not found at " + path
        else:
            self.status_display["text"] = "The specified path does not exist!"
            
        #also legacy code.
        """
        try:
            os.remove(self.name_entry.get() + ".txt")
            self.status_display["text"] = self.name_entry.get() + ".txt \
successfully deleted."
        except:
            self.status_display["text"] = "Error trying to delete " + self.name_entry.get() + ".txt"
        """

    def clear(self):
        self.text_entry.delete(0.0, END)
        self.status_display["text"] = "Textbox cleared."

#main
root = Tk()
root.title("Notepad Lite 2")
root.geometry("380x240")
root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()
