from os import execle
import mysql.connector
from PyQt5 import uic,QtWidgets
from mysql.connector import cursor
from time import sleep
import keyboard

def entrarprograma():
    nome = telalogin.lineEdit.text()
    senha = telalogin.lineEdit_2.text()

    con = mysql.connector.connect(host='localhost',database='login',user='root',password='')
    consulta = "select usuario_id, usuario from usuario where usuario = '{}' and senha = md5('{}')".format(nome, senha)
    cursor = con.cursor()
    cursor.execute(consulta)
    linhas = cursor.fetchall()
    if len(linhas)!= 0:
        telalogin.close()
        bemvind.show()
        telabemvindo()
    else:
        telalogin.label_2.setText('Verifique Seus Dados !!!')

def trocartelacadastro():
    telalogin.close()
    cadastra.show()

def voltartelalogin():
    cadastra.close()
    bemvind.close()
    telalogin.show()

def telabemvindo():
    tecla = input('')
    if tecla == 0:
        voltartelalogin()
    else:
        None

def entrarcadastro():
    nome = cadastra.lineEdit.text()
    senha = cadastra.lineEdit_2.text()
    if len(nome) != 0 and len(senha) != 0:
        try:
            con = mysql.connector.connect(host='localhost',database='login',user='root',password='')
            inserir = "insert into usuario(usuario, senha) values ('{}',md5('{}'))".format(nome, senha)
            cursor = con.cursor()
            cursor.execute (inserir)
            cadastra.label_2.setText('Registrado com sucesso !!')
        except mysql.connector.Error as err:
            cadastra.label_2.setText('Erro ', err)  

    if len(nome) == 0:
        cadastra.label_2.setText("Usuario nao pode estar vazio !!!")
    else:
        print()
    if len(senha) == 0:
        cadastra.label_2.setText("Senha nao pode estar vazia !!!")
    else:
        print()
    if len(senha) == 0 and len(nome) == 0:
        cadastra.label_2.setText("Preencha os campos !!!")
        

app = QtWidgets.QApplication([])
telalogin = uic.loadUi('Telalogin.ui')
bemvind = uic.loadUi('bemvindo.ui')
cadastra = uic.loadUi('cadastro.ui')
entrar = telalogin.pushButton.clicked.connect(entrarprograma)
cadastro = telalogin.pushButton_2.clicked.connect(trocartelacadastro)
entrarcadastroa = cadastra.pushButton.clicked.connect(entrarcadastro)
voltarlogin = bemvind.pushButton_4.clicked.connect(voltartelalogin)
voltarlogin2 = cadastra.pushButton_2.clicked.connect(voltartelalogin)



telalogin.show()
app.exec()