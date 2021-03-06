from tkinter import *
from PIL import Image, ImageTk
import Tela_inicial

class tela_login:

    def __init__(self, master=None):

        master.title("Tela de Login")
        master.geometry("600x700")
        master.resizable(True, True)

        # Criação de label

        self.login = Label(master, width=5, height=5, text='Login', font=('Arial 18 bold'), fg='#000000')
        self.login.place(relx=0.27, rely=0.22)

        self.retangulo = Label(master, width=5, height=5, text='', font=('Arial 18 bold'), bg= '#1c86a8')
        self.retangulo.place(relx=0.27, rely=0.38, relwidth=0.45, relheight=0.01)

        #criação de imagens

        self.image = Image.open("logo-locar.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.imagem = Label(master, image=self.photo)
        self.imagem.image = self.photo
        self.imagem.pack()

        # Entradas

        self.text_nome = Label(master, text="Nome", font='arial,3')
        self.text_nome.place(relx=0.21, rely=0.43, relwidth=0.2, relheight=0.05)
        self.nome = Entry(master)
        self.nome.pack()
        self.nome.place(relx=0.27, rely=0.5, relwidth=0.45, relheight=0.05)

        self.text_senha = Label(master, text="Senha", font='arial,3')
        self.text_senha.place(relx=0.21, rely=0.58, relwidth=0.2, relheight=0.05)
        self.senha = Entry(master)
        self.senha.pack()
        self.senha.place(relx=0.27, rely=0.65, relwidth=0.45, relheight=0.05)

        # Botão

        self.bt_entrar = Button(master, text="Entrar", fg='#fffcfc', bg='#1c86a8', font=('15'),
                                command=Tela_inicial.tela_inicial)
        self.bt_entrar.place(relx=0.35, rely=0.8, relwidth=0.3, relheight=0.1)


root=Tk()
tela_login(root)
root.mainloop()


