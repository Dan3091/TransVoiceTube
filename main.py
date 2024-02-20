from tkinter import *
from gui_audio_recognition import App
from audio_translate import *
import threading


def url_entry_validation():
    """
    This function validates the url_entry, first checks if there are some text,
    then checks if 'youtube.com' is present inside the text.
    """

    entry_url = app.entry_url.get()
    if len(entry_url) > 0:
        if "youtube.com" in entry_url:
            app.label_url_error.config(text="")
            return True
        else:
            app.label_url_error.config(text="*Insert the YouTube link")
            return False
    else:
        app.label_url_error.config(text="*Insert the link")
        return False

def language_from_validation():
    """
    The function validates the from_language selector, checks if
    the language was selected or not.
    """

    language_from = app.clicked1.get()
    if language_from != "Select":
        app.label_translate_from_error.config(text="")
        return True
    else:
        app.label_translate_from_error.config(text="*Select language")
        return False


def language_to_validation():
    """
    The function validates the to_language selector, checks if
    the language was selected or not.
    """

    language_to = app.clicked2.get()
    if language_to != "Select":
        app.label_translate_to_error.config(text="")
        return True
    else:
        app.label_translate_to_error.config(text="*Select language")
        return False


def language_selector_validation():
    """
    This function checks if the two selected languages are the same.
    """

    language_from = app.clicked1.get()
    language_to = app.clicked2.get()
    if language_from != language_to or language_from == "Select" and language_to == "Select":
        app.label_select_language_error.config(text="")
        return True
    else:
        app.label_select_language_error.config(text="*The languages can't be the same")
        return False

def popup_message(message):
    """
    This function creates a popup window message.
    """

    pop = Tk()
    pop.attributes('-topmost', 1)
    pop.grab_set()
    pop.configure(bg="#242c31")
    pop.resizable(False, False)
    pop.overrideredirect(True)
    pop_label = Label(pop, text=message, font="Italic 16", bg="#242c31", fg="#95b1bc")
    pop_label.pack(pady=(10, 20), padx=10)
    btn = Button(pop,
                 text="OK",
                 font="Unispace 14",
                 background="#38454c",
                 foreground="#a9babc",
                 activebackground="#283f5b",
                 activeforeground="white",
                 width=10,
                 command=lambda:[app.deiconify(), pop.destroy()])
    btn.pack()

    pop_label = Label(pop, text="", bg="#242c31")
    pop_label.pack(pady=(10, 0), padx=10)
    pop.update_idletasks()
    posx = str((pop.winfo_screenwidth() // 2) - (pop.winfo_width() // 2))
    posy = str((pop.winfo_screenheight() // 2) - (pop.winfo_height() // 2))
    pop.geometry(f"{pop.winfo_width()}x{pop.winfo_height()}+{posx}+{posy}")
    pop.mainloop()

def data_processing():
    pass

if __name__ == "__main__":
    app = App(data_processing)
    app.mainloop()