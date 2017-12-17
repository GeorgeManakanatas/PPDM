import tkinter as tk
from PIL import Image
from PIL import ImageTk

class Program(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        container = tk.Frame(self)
        container.pack(side='top',fill='both', expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
        Frames = (LoginPage, StartPage)
        for F in Frames:
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky="nsew")

        self.ShowF(LoginPage)

    def ShowF(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self,parent,controller):
        self.controller = controller
        #background = Image.open('GUI/images/free-abstract-background-25.jpeg')
        #tkimage = ImageTk.PhotoImage(background)
        tk.Frame.__init__(self,parent, bg='#a1dbcd')
        stats = tk.Label(self, text = 'Insira os dados para a validação', bg='#a1dbcd')
        stats.pack()
        lab = tk.Label(self, text = ('Usuário'), bg='#a1dbcd')
        lab.pack()
        self.ent = tk.Entry(self)
        self.ent.pack()
        lab2 = tk.Label(self, text = ('Senha'), bg='#a1dbcd')
        lab2.pack()
        self.ent2 = tk.Entry(self, show='*')
        self.ent2.pack()
        but = tk.Button(self, text = 'Validar', bg='#a1dbcd', command = self.Validacao)
        but.pack()
        self.lab3 = tk.Label(self, text = '', bg='#a1dbcd')
        self.lab3.pack()

    def Validacao(self):
        user = self.ent.get()
        passw = self.ent2.get()
        print ('user: ',user,' passw ',passw)
        self.lab3['text'] = ('Validação concluída!')
        self.controller.ShowF(StartPage) #The problem is here(I think)
                

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Button1")
        button.pack()
        buttona = tk.Button(self, text="Button2")
        buttona.pack()

app = Program()
app.mainloop()