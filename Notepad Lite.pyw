from tkinter import *
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

        #name label
        Label(self,
              text = "Name:"
              ).grid(row = 0, column = 0, sticky = W)

        #row 0
        #name entry box
        self.name_entry = Entry(self)
        self.name_entry.grid(row = 0, column = 1, sticky = W)

        #save button
        self.save_button = Button(self, text = "Save", command = self.save)
        self.save_button.grid(row = 0, column = 2, sticky = W)

        #delete button
        self.delete_button = Button(self, text = "Delete", command = self.delete)
        self.delete_button.grid(row = 0, column = 3, sticky = W)

        #row 1
        #text entry box
        self.text_entry = Text(self, width = 35, height = 10, wrap = WORD)
        self.text_entry.grid(row = 1, column = 0, columnspan = 4, sticky = W)

        #row 2
        #status display box
        self.status_display = Label(self, text = "Ready.")
        self.status_display.grid(row = 2, column = 0, columnspan = 3, sticky = W)

    def save(self):
        contents = self.text_entry.get('1.0', END)
        try:
            text_file = open(self.name_entry.get() + ".txt", "w")
            text_file.write(contents)
            text_file.close()
            self.status_display["text"] = self.name_entry.get() + ".txt \
successfully saved."
        except:
            self.status_display["text"] = "Error while trying to save " + self.name_entry.get() + ".txt"

    def delete(self):
        try:
            os.remove(self.name_entry.get() + ".txt")
            self.status_display["text"] = self.name_entry.get() + ".txt \
successfully deleted."
        except:
            self.status_display["text"] = "Error trying to delete " + self.name_entry.get() + ".txt"

#main
root = Tk()
root.title("Notepad Lite")
root.geometry("286x215")
root.resizable(width=False, height=False)
app = Application(root)
root.mainloop()
