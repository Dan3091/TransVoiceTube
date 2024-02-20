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

def data_processing():
    pass

if __name__ == "__main__":
    app = App(data_processing)
    app.mainloop()