import pymysql.cursors
from contextlib import contextmanager
from pymysql import Error


@contextmanager

def conexaoBanco():

    conexao = None

    try:
        conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='locar',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
)
    except Error as ex:
        print(ex)
    return conexao

def dql(query):#select

    conect = conexaoBanco()
    c=conect.cursor()
    c.execute(query)
    resultado = c.fetchall()
    conect.close()
    return resultado

def dml (query):

    try:
        conect = conexaoBanco()
        c = conect.cursor()
        c.execute(query)
        conect.commit()
        conect.close()

    except Error as ex:
        print(ex)
