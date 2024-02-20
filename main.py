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

def data_processing():
    pass

if __name__ == "__main__":
    app = App(data_processing)
    app.mainloop()