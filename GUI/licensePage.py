# from .../packages import getDataInfo
import tkinter as tk
from tkinter import ttk
import json
import os

"""
Initialising typefonts and vals list
"""
LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

vals = []
for position in range(7):
    vals.append(position)
    # print vals

class start_gui_window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # print "initialising frames"
        self.frames = {}
        frame = licensePage(container, self)
        self.frames[licensePage] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        # print "showing the startpage"
        self.show_frame(licensePage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def pop_up_msg(msg):
    popup = tk.Tk()

    def leave_mini():
        popup.destroy()

    popup.wm_title("!!!")
    label = ttk.Label(popup, text=msg, font=NORMAL_FONT)
    label.pack(side="top", fill="x", pady=10)
    exit_button = ttk.Button(popup, text="OK", command=leave_mini)
    exit_button.pack()
    popup.mainloop()


class licensePage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        """
        changes the state of the button according to the state of the checkbox
        """
        def printvalue(check_var):
            if check_var.get() == 1:
                button1.configure(state="enabled")
            else:
                button1.configure(state="disabled")
        """
        initialise variables and text for window
        """
        check_var = tk.IntVar()
        license_text = "Copyright (c) 2015 George Manakanatas\n\n" \
                       "Permission is hereby granted, free of charge, to any person obtaining a copy\n" \
                       "of this software and associated documentation files (the \"Software\"), to deal\n" \
                       "in the Software without restriction, including without limitation the rights\n" \
                       "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n" \
                       "copies of the Software, and to permit persons to whom the Software is\n" \
                       "furnished to do so, subject to the following conditions:\n\n" \
                       "The above copyright notice and this permission notice shall be included in\n" \
                       "all copies or substantial portions of the Software.\n\n" \
                       "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n" \
                       "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n" \
                       "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE\n" \
                       "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n" \
                       "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n" \
                       "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN\n" \
                       "THE SOFTWARE."
        """
        Initialising widgets
        """

        label = ttk.Label(self, text="The MIT License (MIT)", font=LARGE_FONT,
                          anchor="center")
        txt = tk.Text(self, padx=10, pady=10, width=80)

        txt.insert(tk.INSERT, license_text)

        chk = tk.Checkbutton(self, text='I agree', variable=check_var,
                             onvalue=1, offvalue=0,
                             command=lambda: printvalue(check_var))
        chk.deselect()
        button1 = ttk.Button(self, text="Accept", state="disabled",
                             command=lambda: licensePage.quit(self))
        """
        Placing the widgets using the grid method in 3xROWS & 3xCOLUMNS
        """
        label.grid(row=0, column=0, columnspan=2, sticky="nsew")
        txt.grid(row=1, column=0, columnspan=2, sticky="nsew")
        chk.grid(row=3, column=0, rowspan=2, sticky="nsw")
        button1.grid(row=3, column=1, rowspan=2, sticky="nse")

if __name__ == "__main__":
    app = start_gui_window()
    # app.geometry("640x420")
    app.mainloop()
