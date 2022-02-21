import banco

class multa_banco (object):

    def __init__(self, cpf= "", nome = "", cnh = "", email = "", telefone= "",
                 endereco= "", cidade= "", estado = "", data_multa = "", hora_multa = "",
                 local_multa= "", descricao = "", modelo_veiculo = "", ano_veiculo = "", placa_veiculo="",
                 venc_multa = "", forma_pgto = "", valor_total = ""):

        self.info = {}
        self.cpf = cpf
        self.nome = nome
        self.cnh = cnh
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.data_multa = data_multa
        self.hora_multa = hora_multa
        self.local_multa = local_multa
        self.descricao = descricao
        self.modelo_veiculo = modelo_veiculo
        self.ano_veiculo = ano_veiculo
        self.placa_veiculo =placa_veiculo
        self.venc_multa = venc_multa
        self.forma_pgto = forma_pgto
        self.valor_total= valor_total

    def inserir_multa(self):

            Banco = banco.conexao
            try:
                conecta = Banco.conexao.cursor()

                conecta.execute("INSERT INTO multa (cpf,nome,cnh, email,telefone,endereco,cidade,"
                                "estado,data_multa,hora_multa,local_multa,descricao,modelo_veiculo,"
                                "ano_veiculo,placa_veiculo,venc_multa,forma_pgto,valor_total values"
                                "( "'+ self.cpf +'" , '" + self.nome + "','" + self.cnh + "','"
                                 + self.email + "','" + self.telefone + "','" + self.endereco + "','"
                                 + self.cidade + "','" + self.estado + "','" + self.data_multa + "','"
                                 + self.hora_multa + "','" + self.local_multa + "','" + self.descricao +
                                 "','" + self.modelo_veiculo + "','" + self.ano_veiculo + "','" + self.placa_veiculo +
                                 "','" + self.venc_multa + "','" + self.forma_pgto + "','" + self.valor_total + "' )")


                banco.conexao.commit()
                conecta.close()

                return "Multa Registrada com Sucesso"

            except:

                return "Ocorreu um erro no registro"
