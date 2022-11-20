from tkinter import Tk, ttk, W

class UI:
    def __init__(self, root):
        self._root = root


    def handle_button_click(self,event):
        print("button clicked", event)



    def start(self):
        heading_l = ttk.Label(master=self._root, text="Login", foreground="white",  background="black")

        email_l = ttk.Label(master=self._root, text="Email")
        email_e = ttk.Entry(master=self._root)

        username_l = ttk.Label(master=self._root, text="Username")
        username_e = ttk.Entry(master=self._root)

        password_l = ttk.Label(master=self._root, text="Password")
        password_e = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Button")

        heading_l.grid(row=0, column=0, columnspan=2, sticky =W)
    
        email_l.grid(row =1, column=0)
        email_e.grid(row=1, column =1)


        username_l.grid(row=3, column=0)
        username_e.grid(row=3, column=1)

        password_l.grid(row=5, column=0)
        password_e.grid(row=5, column=1)

        button.grid(row=7, column=0, columnspan=2)
        
        self._root.grid_columnconfigure(1, weight=1)
        button.bind("<Button-1>", self.handle_button_click)
