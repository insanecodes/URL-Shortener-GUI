from tkinter import *
from tkinter import messagebox
import pyshorteners


class urlshortner_window:
    def __init__(self, root):
        self.root = root
        # Change the title
        self.root.title("Url Shortner")
        # Change the window size
        self.root.geometry("500x200")
        # no resize for both directions
        self.root.resizable(False, False)
        # Change icon
        self.root.iconbitmap('icon.ico')

        # set gui widgets
        self.title = Label(self.root, text="URL Shortner", font=(
            'verdana', 16, 'bold'), fg="blue")
        self.title.place(x=180, y=5)

        Label(self.root, text="Paste Your Url Here ..", font=(
            'verdana', 10, 'bold'), fg="blue").place(x=50, y=55)

        self.input = Entry(self.root, width=34, font="14", bg="lightgrey",
                           relief=GROOVE, borderwidth=2)
        self.input.place(x=50, y=85, height=30)

        btn_short = Button(self.root, relief=GROOVE, text="Create", font=(
            'verdana', 10, 'bold'), bg="blue", fg="white", command=self.create)
        btn_short.place(x=383, y=85, width=65, height=30)

    def create(self):
        '''takes input from entry widget, Short the url and display output '''
        if self.input.get() == "":
            messagebox.showerror("Error", "Please Enter an URL")
        else:
            self.urls = self.input.get()
            self.s = pyshorteners.Shortener()
            self.short_url = self.s.tinyurl.short(self.urls)
            self.output = Entry(self.root, font=(
                'verdana', 11), fg="blue", width=30, relief=GROOVE, borderwidth=2, border=2)
            self.output.insert(END, self.short_url)
            self.output.place(x=100, y=140)


# driver code
if __name__ == "__main__":
    root = Tk()
    obj = urlshortner_window(root)
    root.mainloop()
