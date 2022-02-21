from tkinter import *
from tkinter import ttk
import tkinter as tk

import Tela_inicial


class retirada_veiculo:

    def __init__(self):

        master3=Toplevel()
        master3.title("Retirada do Veículo")
        master3.geometry("800x1200")

        # Menu
        self.barra_menu = Label(master3, bg='#c4c4c4')
        self.barra_menu.place(relx=0.0, rely=0.0, relwidth=0.22, relheight=0.999)

        self.bt_sair = Button(master3, text="Sair", font='arial 10')
        self.bt_sair.place(relx=0.06, rely=0.8, relwidth=0.1, relheight=0.03)

        # barra em cima
        self.retangulo = Label(master3, bg='#1c86a8')
        self.retangulo.place(relx=0.22, rely=0.0, relwidth=0.9999, relheight=0.03)

        self.texto = Label(master3, width=2, height=2, text='Sistema de Gerenciamento de Aluguel de Veículos',
                           fg='#ffffff',font=('Arial 10 bold'), bg='#1c86a8')
        self.texto.place(relx=0.22, rely=0.0, relwidth=0.78, relheight=0.03)

        # label formulário

        self.ret_veiculo = Label(master3, text="Registro de Retirada do Veículo", font='arial 15 bold')
        self.ret_veiculo.place(relx=0.38, rely=0.047,relwidth=0.5, relheight=0.03)

        self.text_cpf = Label(master3, text="CPF", font='arial 9')
        self.text_cpf.place(relx=0.36, rely=0.10, relwidth=0.1, relheight=0.02)
        self.cpf = Entry(master3)
        self.cpf.pack()
        self.cpf.place(relx=0.44, rely=0.10, relwidth=0.25, relheight=0.024)

        self.bt_buscar = Button(master3, text="Buscar", font='arial 9')
        self.bt_buscar.place(relx=0.7, rely=0.10, relwidth=0.1, relheight=0.026)

        self.cliente = Label(master3, width=5, height=5, text='Dados do cliente',
                             font='Arial 10 bold', fg='#ffffff', bg='#1c86a8')
        self.cliente.place(relx=0.222, rely=0.14, relwidth=0.77, relheight=0.026)

        self.text_nome = Label(master3, text="Nome", font='arial 9')
        self.text_nome.place(relx=0.22, rely=0.18, relwidth=0.1, relheight=0.02)
        self.nome = Entry(master3)
        self.nome.pack()
        self.nome.place(relx=0.31, rely=0.18, relwidth=0.25, relheight=0.024)

        self.text_idade = Label(master3, text="Idade", font='arial 9')
        self.text_idade.place(relx=0.587, rely=0.18, relwidth=0.06, relheight=0.019)
        self.idade = Entry(master3)
        self.idade.pack()
        self.idade.place(relx=0.65, rely=0.18, relwidth=0.08, relheight=0.024)

        self.text_cnh = Label(master3, text="CNH", font='arial 9')
        self.text_cnh.place(relx=0.74, rely=0.18, relwidth=0.05, relheight=0.02)
        self.cnh = Entry(master3)
        self.cnh.pack()
        self.cnh.place(relx=0.8, rely=0.18, relwidth=0.17, relheight=0.024)

        self.text_email = Label(master3, text="E-mail", font='arial 9')
        self.text_email.place(relx=0.22, rely=0.22, relwidth=0.1, relheight=0.02)
        self.email = Entry(master3)
        self.email.pack()
        self.email.place(relx=0.31, rely=0.22, relwidth=0.29, relheight=0.024)

        self.text_telefone = Label(master3, text="Telefone", font='arial 9')
        self.text_telefone.place(relx=0.62, rely=0.22, relwidth=0.1, relheight=0.019)
        self.telefone = Entry(master3)
        self.telefone.pack()
        self.telefone.place(relx=0.72, rely=0.22, relwidth=0.18, relheight=0.024)

        self.text_endereco = Label(master3, text="Endereço", font='arial 9')
        self.text_endereco.place(relx=0.231, rely=0.26, relwidth=0.1, relheight=0.02)
        self.endereco = Entry(master3)
        self.endereco.pack()
        self.endereco.place(relx=0.33, rely=0.26, relwidth=0.64, relheight=0.024)

        self.text_estado = Label(master3, text="Estado", font='arial 9')
        self.text_estado.place(relx=0.221, rely=0.3, relwidth=0.1, relheight=0.02)
        self.estado = Entry(master3)
        self.estado.pack()
        self.estado.place(relx=0.314, rely=0.3, relwidth=0.22, relheight=0.024)

        self.text_cidade = Label(master3, text="Cidade", font='arial 9')
        self.text_cidade.place(relx=0.54, rely=0.3, relwidth=0.1, relheight=0.02)
        self.cidade = Entry(master3)
        self.cidade.pack()
        self.cidade.place(relx=0.63, rely=0.3, relwidth=0.34, relheight=0.024)

        self.reserva = Label(master3, width=5, height=5, text='Dados da Reserva',
                             font=('Arial 10 bold'),fg='#ffffff',bg='#1c86a8')
        self.reserva.place(relx=0.222, rely=0.34, relwidth=0.77, relheight=0.024)

        self.text_reserva = Label(master3, text="Número da reserva", font='arial 9')
        self.text_reserva.place(relx=0.22, rely=0.38, relwidth=0.18,relheight=0.017)
        self.id_reserva = Entry(master3)
        self.id_reserva.pack()
        self.id_reserva.place(relx=0.39, rely=0.38, relwidth=0.24, relheight=0.024)

        self.retirada = Label(master3, width=5, height=5, text='DETALHES DA RETIRADA',
                              font=('Arial 9 bold'))
        self.retirada.place(relx=0.239, rely=0.42, relwidth=0.18, relheight=0.016)

        self.devolucao = Label(master3, width=5, height=5, text='DETALHES DA DEVOLUÇÃO',
                               font=('Arial 9 bold'))
        self.devolucao.place(relx=0.62, rely=0.42, relwidth=0.2, relheight=0.015)

        self.text_data_ret = Label(master3, text="Data", font='arial 9')
        self.text_data_ret.place(relx=0.23, rely=0.46, relwidth=0.06, relheight=0.017)
        self.data_retirada = Entry(master3)
        self.data_retirada.pack()
        self.data_retirada.place(relx=0.29, rely=0.46, relwidth=0.12, relheight=0.024)

        self.text_hora_ret = Label(master3, text="Hora", font='arial 9')
        self.text_hora_ret.place(relx=0.42, rely=0.46, relwidth=0.06, relheight=0.017)
        self.hora_retirada = Entry(master3)
        self.hora_retirada.pack()
        self.hora_retirada.place(relx=0.48, rely=0.46, relwidth=0.11, relheight=0.024)

        self.text_sede = Label(master3, text="Sede", font='arial 9')
        self.text_sede.place(relx=0.23, rely=0.5, relwidth=0.06, relheight=0.017)
        self.sede_retirada = Entry(master3)
        self.sede_retirada.pack()
        self.sede_retirada.place(relx=0.29, rely=0.5, relwidth=0.3, relheight=0.024)

        self.text_endereco = Label(master3, text="Endereço", font='arial 9')
        self.text_endereco.place(relx=0.224, rely=0.54, relwidth=0.1, relheight=0.02)
        self.endereco_retirada = Entry(master3)
        self.endereco_retirada.pack()
        self.endereco_retirada.place(relx=0.32, rely=0.54, relwidth=0.27, relheight=0.024)

        self.text_estado = Label(master3, text="Estado", font='arial 9')
        self.text_estado.place(relx=0.224, rely=0.58, relwidth=0.08, relheight=0.02)
        self.estado_retirada = Entry(master3)
        self.estado_retirada.pack()
        self.estado_retirada.place(relx=0.31, rely=0.58, relwidth=0.28, relheight=0.024)

        self.text_cidade = Label(master3, text="Cidade", font='arial 9')
        self.text_cidade.place(relx=0.234, rely=0.62, relwidth=0.06, relheight=0.02)
        self.cidade_retirada = Entry(master3)
        self.cidade_retirada.pack()
        self.cidade_retirada.place(relx=0.31, rely=0.62, relwidth=0.28, relheight=0.024)

        self.text_data_dev = Label(master3, text="Data", font='arial 9')
        self.text_data_dev.place(relx=0.61, rely=0.46, relwidth=0.06, relheight=0.017)
        self.data_devolucao = Entry(master3)
        self.data_devolucao.pack()
        self.data_devolucao.place(relx=0.67, rely=0.46, relwidth=0.12, relheight=0.024)

        self.text_hora_dev = Label(master3, text="Hora", font='arial 9')
        self.text_hora_dev.place(relx=0.8, rely=0.46, relwidth=0.06, relheight=0.017)
        self.hora_devolucao = Entry(master3)
        self.hora_devolucao.pack()
        self.hora_devolucao.place(relx=0.86, rely=0.46, relwidth=0.11, relheight=0.024)

        self.text_sede_dev= Label(master3, text="Sede", font='arial 9')
        self.text_sede_dev.place(relx=0.61, rely=0.5, relwidth=0.06, relheight=0.017)
        self.sede_devolucao = Entry(master3)
        self.sede_devolucao.pack()
        self.sede_devolucao.place(relx=0.67, rely=0.5, relwidth=0.3, relheight=0.024)

        self.text_endereco_dev = Label(master3, text="Endereço", font='arial 9')
        self.text_endereco_dev.place(relx=0.606, rely=0.54, relwidth=0.1, relheight=0.02)
        self.endereco_devolucao = Entry(master3)
        self.endereco_devolucao.pack()
        self.endereco_devolucao.place(relx=0.71, rely=0.54, relwidth=0.26, relheight=0.024)

        self.text_estado_dev = Label(master3, text="Estado", font='arial 9')
        self.text_estado_dev.place(relx=0.598, rely=0.58, relwidth=0.1, relheight=0.02)
        self.estado_devolucao = Entry(master3)
        self.estado_devolucao.pack()
        self.estado_devolucao.place(relx=0.69, rely=0.58, relwidth=0.28, relheight=0.024)

        self.text_cidade_dev = Label(master3, text="Cidade", font='arial 9')
        self.text_cidade_dev.place(relx=0.615, rely=0.62, relwidth=0.06, relheight=0.02)
        self.cidade_devolucao = Entry(master3)
        self.cidade_devolucao.pack()
        self.cidade_devolucao.place(relx=0.69, rely=0.62, relwidth=0.28, relheight=0.024)

        self.veiculo = Label(master3, width=5, height=5, text='DETALHES DO VEÍCULO',
                             font=('Arial 9 bold'))
        self.veiculo.place(relx=0.224, rely=0.66, relwidth=0.19, relheight=0.018)

        self.text_categoria = Label(master3, text="Categoria", font='arial 9')
        self.text_categoria.place(relx=0.22, rely=0.7, relwidth=0.1, relheight=0.02)
        self.categoria = Entry(master3)
        self.categoria.pack()
        self.categoria.place(relx=0.32, rely=0.7, relwidth=0.12, relheight=0.024)

        self.text_modelo = Label(master3, text="Modelo", font='arial 9')
        self.text_modelo.place(relx=0.46, rely=0.7, relwidth=0.06, relheight=0.02)
        self.modelo = Entry(master3)
        self.modelo.pack()
        self.modelo.place(relx=0.53, rely=0.7, relwidth=0.2, relheight=0.024)

        self.text_ano = Label(master3, text="Ano", font='arial 9')
        self.text_ano.place(relx=0.74, rely=0.7, relwidth=0.06, relheight=0.02)
        self.ano = Entry(master3)
        self.ano.pack()
        self.ano.place(relx=0.8, rely=0.7, relwidth=0.17, relheight=0.024)

        self.text_nome_veiculo = Label(master3, text="Nome do Veículo", font='arial 9')
        self.text_nome_veiculo.place(relx=0.224, rely=0.74, relwidth=0.14, relheight=0.02)
        self.nome_veiculo = Entry(master3)
        self.nome_veiculo.pack()
        self.nome_veiculo.place(relx=0.36, rely=0.74, relwidth=0.23, relheight=0.024)

        self.text_placa = Label(master3, text="Placa", font='arial 9')
        self.text_placa.place(relx=0.6, rely=0.74, relwidth=0.06, relheight=0.02)
        self.placa = Entry(master3)
        self.placa.pack()
        self.placa.place(relx=0.66, rely=0.74, relwidth=0.1, relheight=0.024)

        self.text_portas = Label(master3, text="Qutda. de Portas", font='arial 9')
        self.text_portas.place(relx=0.78, rely=0.74, relwidth=0.12, relheight=0.02)
        self.portas = Entry(master3)
        self.portas.pack()
        self.portas.place(relx=0.91, rely=0.74, relwidth=0.06, relheight=0.024)

        self.text_combustivel = Label(master3, text="Combustível", font='arial 9')
        self.text_combustivel.place(relx=0.226, rely=0.78, relwidth=0.1, relheight=0.02)
        self.combustivel = Entry(master3)
        self.combustivel.pack()
        self.combustivel.place(relx=0.33, rely=0.78, relwidth=0.15, relheight=0.024)

        self.text_transmissao = Label(master3, text="Transmissão", font='arial 9')
        self.text_transmissao.place(relx=0.49, rely=0.78, relwidth=0.1, relheight=0.02)
        self.transmissao = Entry(master3)
        self.transmissao.pack()
        self.transmissao.place(relx=0.6, rely=0.78, relwidth=0.17, relheight=0.024)

        self.text_km = Label(master3, text="KM/L", font='arial 9')
        self.text_km.place(relx=0.78, rely=0.78, relwidth=0.06, relheight=0.02)
        self.quilometragem = Entry(master3)
        self.quilometragem.pack()
        self.quilometragem.place(relx=0.84, rely=0.78, relwidth=0.13, relheight=0.024)

        self.text_diarias = Label(master3, text="Diárias", font='arial 9')
        self.text_diarias.place(relx=0.227, rely=0.82, relwidth=0.06, relheight=0.02)
        self.diaria = Entry(master3)
        self.diaria.pack()
        self.diaria.place(relx=0.3, rely=0.82, relwidth=0.06, relheight=0.024)

        self.text_valor_diaria = Label(master3, text="Valor da Diária", font='arial 9')
        self.text_valor_diaria.place(relx=0.37, rely=0.82, relwidth=0.12, relheight=0.02)
        self.valor_diaria = Entry(master3)
        self.valor_diaria.pack()
        self.valor_diaria.place(relx=0.49, rely=0.82, relwidth=0.07, relheight=0.024)

        self.text_pagamento = Label(master3, text="Pagamento", font='arial 9')
        self.text_pagamento.place(relx=0.57, rely=0.82, relwidth=0.08, relheight=0.02)
        self.box = ttk.Combobox(master3, values=[ "Cartão de Crédito", "Cartão de Débito","Dinheiro"])
        self.box.place(relx=0.66, rely=0.82, relwidth=0.13, relheight=0.024)

        self.text_valor_total = Label(master3, text="Valor Total", font='arial 9')
        self.text_valor_total.place(relx=0.8, rely=0.82, relwidth=0.08, relheight=0.02)
        self.valor_total = Entry(master3)
        self.valor_total.pack()
        self.valor_total.place(relx=0.89, rely=0.82, relwidth=0.08, relheight=0.024)

        #Botão de Check

        self.chkValue1 = tk.BooleanVar()
        self.chkValue1.set(True)

        self.chkValue2 = tk.BooleanVar()
        self.chkValue2.set(True)

        self.chkValue3 = tk.BooleanVar()
        self.chkValue3.set(True)

        self.chkValue4 = tk.BooleanVar()
        self.chkValue4.set(True)

        self.chkValue5 = tk.BooleanVar()
        self.chkValue5.set(True)

        self.chkValue6 = tk.BooleanVar()
        self.chkValue6.set(True)

        self.serv_adicional = Label(master3, text="Serviço Adicional", font='arial 9')
        self.serv_adicional.place(relx=0.224, rely=0.86, relwidth=0.13, relheight=0.02)

        self.servico_adicional1 = tk.Checkbutton(master3, font= 'arial 6',text='Seguro Veicular Acidente  R$30,00',
                                                 var=self.chkValue1)
        self.servico_adicional1.place(relx=0.35, rely=0.86, relwidth=0.19, relheight=0.02)

        self.servico_adicional2 = tk.Checkbutton(master3, font= 'arial 6',text='Seguro Veicular Roubo e furto  R$40,00',
                                                 var=self.chkValue2)
        self.servico_adicional2.place(relx=0.336, rely=0.88, relwidth=0.24, relheight=0.02)

        self.servico_adicional3 = tk.Checkbutton(master3, font= 'arial 6',text='Seguro Veicular Completo  R$50,00',
                                                 var=self.chkValue3)
        self.servico_adicional3.place(relx=0.53, rely=0.86, relwidth=0.24, relheight=0.02)

        self.servico_adicional4 = tk.Checkbutton(master3, font= 'arial 6',text='Cadeira de bebê  R$20,00',
                                                 var=self.chkValue4)
        self.servico_adicional4.place(relx=0.562, rely=0.88, relwidth=0.13, relheight=0.02)

        self.servico_adicional5 = tk.Checkbutton(master3, font= 'arial 6',text='Bebê conforto  R$20,00',
                                                 var=self.chkValue5)
        self.servico_adicional5.place(relx=0.76, rely=0.86, relwidth=0.13, relheight=0.02)

        self.servico_adicional6 = tk.Checkbutton(master3, font= 'arial 6',text='Condutor extra  R$40,00',
                                                 var=self.chkValue6)
        self.servico_adicional6.place(relx=0.72, rely=0.88, relwidth=0.21, relheight=0.02)

        #Botões

        self.bt_salvar = Button(master3, text="Salvar", font='arial 10', bg="#1c86a8", fg="#ffffff")
        self.bt_salvar.place(relx=0.82, rely=0.92, relwidth=0.14, relheight=0.038)

        self.bt_cancelar = Button(master3, text="Cancelar", font='arial 10', bg="#70706e", fg="#ffffff",
                                  command=Tela_inicial.tela_inicial)
        self.bt_cancelar.place(relx=0.25, rely=0.92, relwidth=0.14, relheight=0.038)

        self.bt_alterar = Button(master3, text="Alterar Veículo", font='arial 10', bg="#f21111", fg="#ffffff")
        self.bt_alterar.place(relx=0.63, rely=0.92, relwidth=0.15, relheight=0.038)

        self.bt_upgrade = Button(master3, text="Upgrade do Veículo", font='arial 10', bg="#10ad02", fg="#ffffff")
        self.bt_upgrade.place(relx=0.44, rely=0.92, relwidth=0.16, relheight=0.038)
