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

        # Labels and Entry
        self.title_label = Label(self, text="TransVoiceTube", bg="#38454c", font="Unispace 18", fg="#7b999c")
        self.title_label.pack(pady=(0, 0))
        self.frame = Frame(self, bg="#445760")
        self.frame.pack()
        self.label_url = Label(self.frame, text="Insert the YouTube video link here:", font="Unispace 14", bg="#445760",
                               fg="#a9babc")
        self.label_url.pack(pady=(20, 0))
        self.label_url_error = Label(self.frame, text="", font="Unispace 12", bg="#445760", fg="red")
        self.label_url_error.pack()
        self.entry_url = Entry(self.frame, font="Unispace 14", bg="#38454c", fg="#a9babc", width=40)
        self.entry_url.pack(padx=20)
        self.label_select_language = Label(self.frame, text="Select the languages:", font="Unispace 14", bg="#445760",
                                           fg="#a9babc")
        self.label_select_language.pack()
        self.label_select_language_error = Label(self.frame, text="", font="Unispace 12", bg="#445760", fg="red")
        self.label_select_language_error.pack(pady=(0, 160))
        self.label_translate_from = Label(self.frame, text="From:", font="Unispace 12", bg="#445760", fg="#a9babc")
        self.label_translate_from.place(x=100, y=150)
        self.label_translate_from_error = Label(self.frame, text="", font="Unispace 12", bg="#445760", fg="red")
        self.label_translate_from_error.place(x=45, y=170)

        # Defined the OptionMenus
        self.languages = {
            "English": "en-US",
            "French": "fr-FR",
            "German": "de-DE",
            "Italian": "it-IT",
            "Japanese": "ja-JP",
            "Romanian": "ro-RO",
            "Spanish": "es-ES",
            "Portuguese": "pt-PT",
            "Russian": "ru-RU"
        }

        self.clicked1 = StringVar()
        self.clicked1.set("Select")
        self.drop_menu_translate_from = OptionMenu(self.frame, self.clicked1, *self.languages)
        self.drop_menu_translate_from.config(width=15, bg="#38454c",
                                             fg="#a9babc",
                                             font="Unispace 14",
                                             activebackground="#283f5b",
                                             activeforeground="white")
        self.drop_menu_translate_from["highlightthickness"] = 0
        self.drop_menu_translate_from["menu"].config(bg="#38454c", fg="#a9babc", font="Unispace 14")
        self.drop_menu_translate_from.place(x=20, y=195)

        self.label_translate_to = Label(self.frame, text="To:", font="Unispace 12", bg="#445760", fg="#a9babc")
        self.label_translate_to.place(x=350, y=150)
        self.label_translate_to_error = Label(self.frame, text="", font="Unispace 12", bg="#445760", fg="red")
        self.label_translate_to_error.place(x=285, y=170)
        self.clicked2 = StringVar()
        self.clicked2.set("Select")
        self.drop_menu_translate_to = OptionMenu(self.frame, self.clicked2, *self.languages)
        self.drop_menu_translate_to.config(width=15, bg="#38454c",
                                           fg="#a9babc",
                                           font="Unispace 14",
                                           activebackground="#283f5b",
                                           activeforeground="white")
        self.drop_menu_translate_to["highlightthickness"] = 0
        self.drop_menu_translate_to["menu"].config(bg="#38454c", fg="#a9babc", font="Unispace 14")
        self.drop_menu_translate_to.place(x=260, y=195)

        # Defined Convert button and Quit button
        self.convert_button = Button(text="Convert",
                                     font="Unispace 14",
                                     background="#38454c",
                                     foreground="#a9babc",
                                     activebackground="#283f5b",
                                     activeforeground="white",
                                     width=10)
        self.convert_button.place(x=110, y=290)

        self.quit_button = Button(text="Quit",
                                  font="Unispace 14",
                                  background="#38454c",
                                  foreground="#a9babc",
                                  activebackground="#283f5b",
                                  activeforeground="white",
                                  width=10,
                                  command=self.destroy)
        self.quit_button.place(x=260, y=290)
App().mainloop()