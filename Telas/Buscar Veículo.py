from tkinter import *
import Tela_inicial


class application:

    def __init__(self):

        master6 = Toplevel()
        master6.title("Retirada do Veículo")
        master6.geometry("800x1200")

        # Menu
        self.barra_menu = Label(master6, bg='#c4c4c4')
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=0.999)

        self.bt_sair = Button(master6, text="Sair", font='arial 10')
        self.bt_sair.place(relx=0.06, rely=0.8, relwidth=0.1, relheight=0.03)

        # barra em cima
        self.retangulo = Label(master6, bg='#1c86a8')
        self.retangulo.place(relx=0.22, rely=0.0, relwidth=0.9999, relheight=0.03)

        self.texto = Label(master6, width=2, height=2, text='Sistema de Gerenciamento de Aluguel de Veículos',
                           fg='#ffffff', font='Arial 10 bold', bg='#1c86a8')
        self.texto.place(relx=0.22, rely=0.0, relwidth=0.78, relheight=0.03)

        # Textos

        self.buscar_veiculo = Label(master6, text="Buscar Veículo", font='arial 15 bold')
        self.buscar_veiculo.place(relx=0.38, rely=0.047, relwidth=0.5, relheight=0.03)

        # Entradas

        self.text_id_veiculo = Label(master6, text="ID do Veículo", font='arial 9')
        self.text_id_veiculo.place(relx=0.36, rely=0.10, relwidth=0.1, relheight=0.02)
        self.id_veiculo = Entry(master6)
        self.id_veiculo.pack()
        self.id_veiculo.place(relx=0.47, rely=0.10, relwidth=0.25, relheight=0.024)

        self.text_categoria = Label(master6, text="Categoria", font='arial 9')
        self.text_categoria.place(relx=0.22, rely=0.16, relwidth=0.1, relheight=0.02)
        self.categoria = Entry(master6)
        self.categoria.pack()
        self.categoria.place(relx=0.32, rely=0.16, relwidth=0.12, relheight=0.024)

        self.text_modelo = Label(master6, text="Modelo", font='arial 9')
        self.text_modelo.place(relx=0.46, rely=0.16, relwidth=0.06, relheight=0.02)
        self.modelo = Entry(master6)
        self.modelo.pack()
        self.modelo.place(relx=0.53, rely=0.16, relwidth=0.2, relheight=0.024)

        self.text_ano = Label(master6, text="Ano", font='arial 9')
        self.text_ano.place(relx=0.74, rely=0.16, relwidth=0.06, relheight=0.02)
        self.ano = Entry(master6)
        self.ano.pack()
        self.ano.place(relx=0.8, rely=0.16, relwidth=0.17, relheight=0.024)

        self.text_nome_veiculo = Label(master6, text="Nome do Veículo", font='arial 9')
        self.text_nome_veiculo.place(relx=0.224, rely=0.2, relwidth=0.14, relheight=0.02)
        self.nome_veiculo = Entry(master6)
        self.nome_veiculo.pack()
        self.nome_veiculo.place(relx=0.36, rely=0.2, relwidth=0.4, relheight=0.024)

        self.text_portas = Label(master6, text="Qutda. de Portas", font='arial 9')
        self.text_portas.place(relx=0.78, rely=0.2, relwidth=0.12, relheight=0.02)
        self.portas = Entry(master6)
        self.portas.pack()
        self.portas.place(relx=0.91, rely=0.2, relwidth=0.06, relheight=0.024)

        self.text_combustivel = Label(master6, text="Combustível", font='arial 9')
        self.text_combustivel.place(relx=0.226, rely=0.24, relwidth=0.1, relheight=0.02)
        self.combustivel = Entry(master6)
        self.combustivel.pack()
        self.combustivel.place(relx=0.33, rely=0.24, relwidth=0.15, relheight=0.024)

        self.text_transmissao = Label(master6, text="Transmissão", font='arial 9')
        self.text_transmissao.place(relx=0.49, rely=0.24, relwidth=0.1, relheight=0.02)
        self.transmissao = Entry(master6)
        self.transmissao.pack()
        self.transmissao.place(relx=0.6, rely=0.24, relwidth=0.17, relheight=0.024)

        self.text_quilometragem = Label(master6, text="KM/L", font='arial 9')
        self.text_quilometragem.place(relx=0.78, rely=0.24, relwidth=0.06, relheight=0.02)
        self.quilometragem = Entry(master6)
        self.quilometragem.pack()
        self.quilometragem.place(relx=0.84, rely=0.24, relwidth=0.13, relheight=0.024)

        self.text_quantidade = Label(master6, text="Quantidade", font='arial 9')
        self.text_quantidade.place(relx=0.221, rely=0.28, relwidth=0.1, relheight=0.02)
        self.quantidade = Entry(master6)
        self.quantidade.pack()
        self.quantidade.place(relx=0.33, rely=0.28, relwidth=0.15, relheight=0.024)

        self.text_valor_diaria = Label(master6, text="Valor Diária", font='arial 9')
        self.text_valor_diaria.place(relx=0.49, rely=0.28, relwidth=0.1, relheight=0.02)
        self.valor_diaria = Entry(master6)
        self.valor_diaria.pack()
        self.valor_diaria.place(relx=0.6, rely=0.28, relwidth=0.12, relheight=0.024)

        self.text_status = Label(master6, text="Status", font='arial 9')
        self.text_status.place(relx=0.74, rely=0.28, relwidth=0.06, relheight=0.02)
        self.status = Entry(master6)
        self.status.pack()
        self.status.place(relx=0.8, rely=0.28, relwidth=0.17, relheight=0.024)

        self.mensagem = Label(master6, text="", font=' arial 11')
        self.mensagem.pack()

        # Botão

        self.bt_buscar = Button(master6, text="Buscar", font='arial 9')
        self.bt_buscar["command"] = self.buscar_veiculo
        self.bt_buscar.place(relx=0.73, rely=0.099, relwidth=0.1, relheight=0.026)

        self.bt_voltar = Button(master6, text="Voltar", font='arial 10', command=Tela_inicial.tela_inicial)
        self.bt_voltar.place(relx=0.53, rely=0.35, relwidth=0.14, relheight=0.038)
