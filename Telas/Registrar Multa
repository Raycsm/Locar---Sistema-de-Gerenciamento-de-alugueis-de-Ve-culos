from tkinter import *
from tkinter import ttk
from tkinter import Text
import Tela_inicial

class multa:

    def __init__(self):

        master5 = Toplevel()
        master5.title("Registrar Multa")
        master5.geometry("800x900")

        # Menu

        self.barra_menu = Label(master5, bg='#c4c4c4')
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=0.999)

        self.bt_sair = Button(master5, text="Sair", font='arial 10')
        self.bt_sair.place(relx=0.06, rely=0.8, relwidth=0.1, relheight=0.03)

        # barra em cima
        self.retangulo = Label(master5, bg='#1c86a8')
        self.retangulo.place(relx=0.22, rely=0.0, relwidth=0.9999, relheight=0.03)

        self.texto = Label(master5, width=2, height=2, text='Sistema de Gerenciamento de Aluguel de Veículos',
                           fg='#ffffff',font=('Arial 10 bold'), bg='#1c86a8')
        self.texto.place(relx=0.22, rely=0.0, relwidth=0.78, relheight=0.03)

        # Entradas

        self.registrar_multa = Label (master5, text="Registrar Multa", font='arial 15 bold')
        self.registrar_multa.place(relx=0.38, rely=0.047,relwidth=0.5, relheight=0.03)

        self.text_nome = Label(master5, text="Nome", font='arial 9')
        self.text_nome.place(relx=0.22, rely=0.1, relwidth=0.1, relheight=0.02)
        self.nome_multa = Entry(master5)
        self.nome_multa.pack()
        self.nome_multa.place(relx=0.31, rely=0.1, relwidth=0.38, relheight=0.024)

        self.text_cpf = Label(master5, text="CPF", font='arial 9')
        self.text_cpf.place(relx=0.7, rely=0.102, relwidth=0.04, relheight=0.019)
        self.cpfMulta = Entry(master5)
        self.cpfMulta.pack()
        self.cpfMulta.place(relx=0.76, rely=0.1, relwidth=0.21, relheight=0.024)

        self.text_cnh = Label(master5, text="CNH", font='arial 9')
        self.text_cnh.place(relx=0.79, rely=0.14, relwidth=0.05, relheight=0.02)
        self.cnh_multa = Entry(master5)
        self.cnh_multa.pack()
        self.cnh_multa.place(relx=0.85, rely=0.14, relwidth=0.12, relheight=0.024)

        self.text_email = Label(master5, text="E-mail", font='arial 9')
        self.text_email.place(relx=0.22, rely=0.14, relwidth=0.1, relheight=0.02)
        self.email = Entry(master5)
        self.email.pack()
        self.email.place(relx=0.31, rely=0.14, relwidth=0.25, relheight=0.024)

        self.tex_tel = Label(master5, text="Telefone", font='arial 9')
        self.tex_tel.place(relx=0.57, rely=0.141, relwidth=0.07, relheight=0.019)
        self.telefone = Entry(master5)
        self.telefone.pack()
        self.telefone.place(relx=0.65, rely=0.14, relwidth=0.13, relheight=0.024)

        self.text_end =Label(master5, text="Endereço", font='arial 9')
        self.text_end.place(relx=0.231, rely=0.18, relwidth=0.1, relheight=0.02)
        self.endereco = Entry(master5)
        self.endereco.pack()
        self.endereco.place(relx=0.33, rely=0.18, relwidth=0.64, relheight=0.024)

        self.text_estado = Label(master5, text="Estado", font='arial 9')
        self.text_estado.place(relx=0.221, rely=0.22, relwidth=0.1, relheight=0.02)
        self.estado = Entry(master5)
        self.estado.pack()
        self.estado.place(relx=0.314, rely=0.22, relwidth=0.22, relheight=0.024)

        self.text_cidade = Label(master5, text="Cidade", font='arial 9')
        self.text_cidade.place(relx=0.54, rely=0.22, relwidth=0.1, relheight=0.02)
        self.cidade = Entry(master5)
        self.cidade.pack()
        self.cidade.place(relx=0.63, rely=0.22, relwidth=0.34, relheight=0.024)

        self.text_data = Label(master5, text="Data", font='arial 9')
        self.text_data.place(relx=0.236, rely=0.26, relwidth=0.05, relheight=0.02)
        self.data_multa = Entry(master5)
        self.data_multa.pack()
        self.data_multa.place(relx=0.29, rely=0.26, relwidth=0.12, relheight=0.024)

        self.text_hora = Label(master5, text="Hora", font='arial 9')
        self.text_hora.place(relx=0.42, rely=0.26, relwidth=0.05, relheight=0.02)
        self.hora_multa = Entry(master5)
        self.hora_multa.pack()
        self.hora_multa.place(relx=0.48, rely=0.26, relwidth=0.07, relheight=0.024)

        self.text_local = Label(master5, text="Local", font='arial 9')
        self.text_local.place(relx=0.56, rely=0.261, relwidth=0.05, relheight=0.019)
        self.local_multa = Entry(master5)
        self.local_multa.pack()
        self.local_multa.place(relx=0.62, rely=0.26, relwidth=0.35, relheight=0.024)

        self.text_descricao = Label(master5, text="Descrição", font='arial 9')
        self.text_descricao.place(relx=0.236, rely=0.3, relwidth=0.08, relheight=0.02)
        self.descricao_multa = Text(master5)
        self.descricao_multa.pack()
        self.descricao_multa.place(relx=0.33, rely=0.3, relwidth=0.64, relheight=0.1)

        self.text_modelo = Label(master5, text="Modelo do Veículo", font='arial 9')
        self.text_modelo.place(relx=0.237, rely=0.422, relwidth=0.13, relheight=0.02)
        self.modelo_veiculo = Entry(master5)
        self.modelo_veiculo.pack()
        self.modelo_veiculo.place(relx=0.38, rely=0.42, relwidth=0.16, relheight=0.024)

        self.text_ano = Label(master5, text="Ano do Veículo", font='arial 9')
        self.text_ano.place(relx=0.54, rely=0.422, relwidth=0.12, relheight=0.02)
        self.ano_veiculo = Entry(master5)
        self.ano_veiculo.pack()
        self.ano_veiculo.place(relx=0.66, rely=0.42, relwidth=0.07, relheight=0.024)

        self.text_placa = Label(master5, text="Placa do Veículo", font='arial 9')
        self.text_placa.place(relx=0.74, rely=0.422, relwidth=0.13, relheight=0.019)
        self.placa_veiculo = Entry(master5)
        self.placa_veiculo.pack()
        self.placa_veiculo.place(relx=0.87, rely=0.42, relwidth=0.1, relheight=0.024)

        self.text_vencimento = Label(master5, text="Vencimento da Multa", font='arial 9')
        self.text_vencimento.place(relx=0.236, rely=0.47, relwidth=0.15, relheight=0.02)
        self.vencimento_multa = Entry(master5)
        self.vencimento_multa.pack()
        self.vencimento_multa.place(relx=0.4, rely=0.47, relwidth=0.1, relheight=0.024)

        self.text_pgto =Label(master5, text="Forma de Pgto", font='arial 9')
        self.text_pgto.place(relx=0.504, rely=0.47, relwidth=0.12, relheight=0.02)
        self.forma_pgto = ttk.Combobox(master5, values=[ "Cartão de Crédito", "Cartão de Débito","Dinheiro"])
        self.forma_pgto.pack()
        self.forma_pgto.place(relx=0.62, rely=0.47, relwidth=0.15, relheight=0.024)

        self.text_valor = Label(master5, text="Valor Total", font='arial 9')
        self.text_valor.place(relx=0.78, rely=0.47, relwidth=0.08, relheight=0.019)
        self.valor_total = Entry(master5)
        self.valor_total.pack()
        self.valor_total.place(relx=0.87, rely=0.47, relwidth=0.1, relheight=0.024)

        self.mensagem = Label(master5, text="", font=' arial 11')
        self.mensagem.place(relx=0.87, rely=0.47, relwidth=0.1, relheight=0.024)
        self.mensagem.pack()

        # Botões

        self.bt_salvar = Button(master5, text="Salvar", font='arial 10', bg="#1c86a8", fg="#ffffff")
        self.bt_salvar.place(relx=0.82, rely=0.55, relwidth=0.14, relheight=0.038)

        self.bt_cancelar = Button(master5, text="Cancelar", font='arial 10', bg="#70706e", fg="#ffffff")
        self.bt_cancelar["command"] = Tela_inicial.tela_inicial
        self.bt_cancelar.place(relx=0.25, rely=0.55, relwidth=0.14, relheight=0.038)

