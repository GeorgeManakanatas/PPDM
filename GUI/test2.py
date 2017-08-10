import Tkinter as tk
import time
import threading

class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.frame = tk.Frame(self)
        self.frame.pack(side="top", fill = "both", expand=True)

        self.label = tk.Label(self, text = "Hello, world")
        button1text = "Start process"
        button1 = tk.Button(self, text = button1text,
                                  command = self.button1Process)
        self.label.pack(in_=self.frame)
        button1.pack(in_=self.frame)

    def button1Process(self):
        startTime=time.time()
        working = True
        time.sleep(5)
        while working:
            elapsedTime = int(time.time() - startTime)
            displayText = 'Working for: '+str(elapsedTime)+' secs'
            self.label.config(text = displayText)
            self.label.update_idletasks()
            time.sleep(1)

        self.label.config(text = "Finished")

def main():

    app = SampleApp()
    app.mainloop()

    return 0

if __name__ == '__main__':
    main()
