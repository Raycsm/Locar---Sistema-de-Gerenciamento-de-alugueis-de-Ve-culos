from tkinter import *

import Buscar_reserva
import Buscar_veiculo
import Devolucao_do_veiculo
import Registrar_multa
import Retirada_do_veiculo


class tela_inicial:

    def __init__(self):

        master2 = Toplevel()
        master2.title("Sistema de Gerenciamento de aluguel de veículo")
        master2.geometry("1000x800")

        # Menu
        self.barra_menu = Label(master2, bg='#c4c4c4')
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=0.999)

        self.bt_sair = Button(master2, text="Sair", font='arial 10')
        self.bt_sair.place(relx=0.06, rely=0.8, relwidth=0.1, relheight=0.03)

        # barra em cima
        self.retangulo = Label(master2, bg='#1c86a8')
        self.retangulo.place(relx=0.22, rely=0.0, relwidth=0.9999, relheight=0.03)

        self.texto = Label(master2, width=2, height=2, text='Sistema de Gerenciamento de Aluguel de Veículos',
                           fg='#ffffff', font=('Arial 10 bold'), bg='#1c86a8')
        self.texto.place(relx=0.22, rely=0.0, relwidth=0.78, relheight=0.03)

        #Botões da Tela Inicial

        self.botao1 = Button(master2, text="Retirada do Veículo", fg='#fffcfc', bg='#1c86a8', font=('15'),
                             command=Retirada_do_veiculo.retirada_veiculo)
        self.botao1.place(relx=0.26, rely=0.19, relwidth=0.2, relheight=0.2)

        self.botao2 = Button(master2, text="Devolução do Veículo", fg='#fffcfc', bg='#1c86a8', font=('15'),
                             command=Devolucao_do_veiculo.devolucao_veiculo)
        self.botao2.place(relx=0.50, rely=0.19, relwidth=0.2, relheight=0.2)

        self.botao3 = Button(master2, text="Buscar Veículo", fg='#fffcfc', bg='#1c86a8', font=('15'),
                             command= Buscar_veiculo.application)
        self.botao3.place(relx=0.74, rely=0.19, relwidth=0.2, relheight=0.2)

        self.botao4 = Button(master2, text="Registrar Multa", fg='#fffcfc', bg='#1c86a8', font=('15'),
                             command=Registrar_multa.multa)
        self.botao4.place(relx=0.38, rely=0.50, relwidth=0.2, relheight=0.2)

        self.botao5 = Button(master2, text="Buscar Reserva", fg='#fffcfc', bg='#1c86a8', font=('15'),
                             command= Buscar_reserva.buscar_reserva)
        self.botao5.place(relx=0.63, rely=0.50, relwidth=0.2, relheight=0.2)


