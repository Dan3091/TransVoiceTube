from tkinter import *
import customtkinter


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("TransVoiceTube")
        self.resizable(False, False)
        self.configure(bg='#38454c')
        self.overrideredirect(True)

        # Calculation of the main window position
        posx = str(self.winfo_screenwidth() // 2 - 500 // 2)
        posy = str(self.winfo_screenheight() // 2 - 380 // 2)
        self.geometry(f"500x380+{posx}+{posy}")

App().mainloop()