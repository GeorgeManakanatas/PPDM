# from .../packages import get_data_info
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

class start_new_gui_window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: pop_up_msg("Not Supported Yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tk.Tk.config(self, menu=menubar)

        # print "initialising frames"
        self.frames = {}
        for F in (HomePage, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

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


class HomePage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        """
        Nextpage button and input gathering.
        """
        def leave_button():
            global vals
            vals[0] = get_file_name1.get()
            vals[1] = get_file_name2.get()
            vals[2] = self.variable.get()
            vals[3] = self.val.get()
            vals[4] = attribute_list.get()
            vals[5] = self.variable3.get()
            vals[6] = self.variable2.get()
            print ("values are:", vals)
            
            controller.show_frame(PageThree)
        """
        need to replace this with automatic attribute count.
        """
        # attributes = get_data_info.db_columns()
        attributes = 10
        """
        initialising the Option menu variables
        """
        option_list = ('Simple', 'Simple', 'Mondrian', 'Partially distributed', 'Fully distributed')
        self.variable = tk.StringVar()
        self.variable.set(option_list[0])
        self.val = tk.IntVar()
        self.val.set(3)

        option_list3 = ('option1', 'option1', 'option2', 'option3', 'option4')
        self.variable3 = tk.StringVar()
        self.variable3.set(option_list[0])
        option_list2 = ('Python native', 'Python native', 'method2', 'method3', 'method4')
        self.variable2 = tk.StringVar()
        self.variable2.set(option_list2[0])
        """
        Initialising widgets
        """
        label = ttk.Label(self, text="Home page", font=LARGE_FONT)
        text_label1 = ttk.Label(self, text="Please insert the name of the file"
                                " containing the data:", font=NORMAL_FONT)
        text_label2 = ttk.Label(self, text="Please insert your name of choice "
                                "for the results file:", font=NORMAL_FONT)
        get_file_name1 = tk.Entry(self, width=20, bd=3)
        get_file_name1.insert(0, "adultfull.txt")
        get_file_name2 = tk.Entry(self, width=20, bd=3)
        get_file_name2.insert(0, "results.txt")
        button1 = ttk.Button(self, text="Next page", command=leave_button)
        ano_lev_select_text = ttk.Label(self, text="Please select the desired level of k-anonymity:", font=NORMAL_FONT)
        ano_lev_select = tk.Spinbox(self, from_=0, to=20, textvariable=self.val)
        attribute_list_text = ttk.Label(self, text="There are %i attributes in the database please insert the column "
                                                   "\n numbers that you want to have anonymised seperated by "
                                                   "a comma" %attributes, font=NORMAL_FONT)
        attribute_list = tk.Entry(self, width=20, bd=3)
        anon_meth_text = ttk.Label(self, text="Please select the method to be used in the process:", font=NORMAL_FONT)
        anon_meth = ttk.OptionMenu(self, self.variable, *option_list)
        encr_level_text = ttk.Label(self, text="Please select the desired level of encryption:", font=NORMAL_FONT)
        encr_level = ttk.OptionMenu(self, self.variable3, *option_list3)
        encr_method_text = ttk.Label(self, text="Please select the desired method of encryption:", font=NORMAL_FONT)
        encr_method = ttk.OptionMenu(self, self.variable2, *option_list2)
        """
        Placing the widgets using the grid method in 5xROWS & 3xCOLUMNS
        """
        label.grid(row=0, column=0, pady=10, rowspan=2, columnspan=3,)
        text_label1.grid(row=2, column=0, pady=10, sticky="w")
        text_label2.grid(row=3, column=0, pady=10, sticky="w")
        get_file_name1.grid(row=2, column=1, pady=10, sticky="e")
        get_file_name2.grid(row=3, column=1, pady=10, sticky="e")
        ano_lev_select_text.grid(row=6, column=0, pady=10, sticky="w")
        attribute_list_text.grid(row=7, column=0, pady=10, sticky="w")
        anon_meth_text.grid(row=8, column=0, pady=10, sticky="w")
        ano_lev_select.grid(row=6, column=1, pady=10, sticky="e")
        attribute_list.grid(row=7, column=1, pady=10, sticky="e")
        anon_meth.grid(row=8, column=1, pady=10, sticky="e")
        encr_level_text.grid(row=9, column=0, pady=10, sticky="w")
        encr_method_text.grid(row=10, column=0, pady=10, sticky="w")
        encr_level.grid(row=9, column=1, pady=10, sticky="e")
        encr_method.grid(row=10, column=1, pady=10, sticky="e")
        button1.grid(row=11, column=1, columnspan=2, sticky="e")


class PageThree(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        """
        Exit and return data function
        """
        def leave_mini():
            """
            opening config.json and saving the values
            """
            with open('defaultConfig.json', 'r') as json_data_file:
                conf = json.load(json_data_file)

            print ("values are: ", vals)
            conf["kmin"] = vals[3]
            print ("conf is: ", conf)
            newConfigFile = open('temp/config.json', 'w')
            newConfigFile.write(json.dumps(conf))
            newConfigFile.close()

            # os.system('python main.py')

            PageThree.quit(self)
        """
        Initialising widgets
        """
        
        label = ttk.Label(self, text="You have selected the following settings", font=LARGE_FONT)
        data_file = ttk.Label(self, text="The name of the file containing the data is: %s" %vals[0], font=NORMAL_FONT)
        output_file = ttk.Label(self, text="The name of the file containing the result data is: %s" % vals[1], font=NORMAL_FONT)
        anonym_method = ttk.Label(self, text="The anonymisation method selected is: %s" % vals[2], font=NORMAL_FONT)
        anonym_level = ttk.Label(self, text="The level of anonymisation to be applied is: %s" % vals[3], font=NORMAL_FONT)
        anonym_columns = ttk.Label(self, text="The attributes to be anonymised are: %s" % vals[4], font=NORMAL_FONT)
        encryption_level = ttk.Label(self, text="The level of encryption to be applied is: %s" % vals[5], font=NORMAL_FONT)
        encryption_method = ttk.Label(self, text="The method of encryption to be applied is: %s" % vals[6], font=NORMAL_FONT)
        previous_page_button = ttk.Button(self, text="Previous page", command=lambda: controller.show_frame(HomePage))
        start_button = ttk.Button(self, text="Start the process", command=lambda: leave_mini())
        """
        Placing the widgets using the grid method in 10xROWS & 3xCOLUMNS
        """
        label.grid(row=0, column=0, pady=10, rowspan=2, columnspan=3,)
        data_file.grid(row=2, column=0, pady=10, sticky="w")
        output_file.grid(row=3, column=0, pady=10, sticky="w")
        anonym_method.grid(row=4, column=0, pady=10, sticky="w")
        anonym_level.grid(row=5, column=0, pady=10, sticky="w")
        anonym_columns.grid(row=6, column=0, pady=10, sticky="w")
        encryption_level.grid(row=7, column=0, pady=10, sticky="w")
        encryption_method.grid(row=8, column=0, pady=10, sticky="w")
        previous_page_button.grid(row=10, column=0, pady=10, sticky="w")
        start_button.grid(row=10, column=3, pady=10, sticky="w")

if __name__ == "__main__":
    app = start_new_gui_window()
    # app.geometry("640x420")
    app.mainloop()
