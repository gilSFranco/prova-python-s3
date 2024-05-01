import tkinter as tk
import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo

os.system('cls')

tela = Tk()

tela.title('Controle das Notas')
tela.configure(background='#c0c0c0')
tela.geometry('500x500')

conexao = pymongo.MongoClient('mongodb://localhost:27017/')
bancoDeDados = conexao["revisao"]
alunos = bancoDeDados["Aluno"]

lblNota01 = Label(tela, text='Nota 01: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=30)
txtNota01 = Entry(tela, width=20, fg='#000000')
txtNota01.place(x=130, y=37)

lblNota02 = Label(tela, text='Nota 02: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=70)
txtNota02 = Entry(tela, width=20, fg='#000000')
txtNota02.place(x=130, y=77)

lblNota03 = Label(tela, text='Nota 03: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=110)
txtNota03 = Entry(tela, width=20, fg='#000000')
txtNota03.place(x=130, y=117)

lblNota04 = Label(tela, text='Nota 04: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=150)
txtNota04 = Entry(tela, width=20, fg='#000000')
txtNota04.place(x=130, y=157)

lblNota05 = Label(tela, text='Nota 05: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=190)
txtNota05 = Entry(tela, width=20, fg='#000000')
txtNota05.place(x=130, y=197)

lblIdade = Label(tela, text='Idade: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=230)
txtIdade = Entry(tela, width=20, fg='#000000')
txtIdade.place(x=110, y=237)

lblNome = Label(tela, text='Nome: ', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=270)
txtNome = Entry(tela, width=20, fg='#000000')
txtNome.place(x=110, y=277)

def salvarBanco():
    idade = int(txtIdade.get())
    media = (float(txtNota01.get()) + float(txtNota02.get()) + float(txtNota03.get()) + float(txtNota04.get()) + float(txtNota05.get())) / 5
    nome = txtNome.get()

    Aluno = {
        "idade": idade,
        "media": media,
        "nome": nome
    }

    alunos.insert_one(Aluno)

    messagebox.showinfo('Mensagem', f'O aluno {nome} foi cadastrado com sucesso.')

    txtIdade.delete(0, tk.END)
    txtNome.delete(0, tk.END)
    txtNota01.delete(0, tk.END)
    txtNota02.delete(0, tk.END)
    txtNota03.delete(0, tk.END)
    txtNota04.delete(0, tk.END)
    txtNota05.delete(0, tk.END)

def calcularMedia():
    idade = txtIdade.get()
    nome = txtNome.get()
    media = (float(txtNota01.get()) + float(txtNota02.get()) + float(txtNota03.get()) + float(txtNota04.get()) + float(txtNota05.get())) / 5

    if media >= 5:
        lblResultado = Label(tela, text='O Aluno ' + nome + ' (' + idade + ' anos) foi aprovado!', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=350)
        txtResultado.delete(0, tk.END)
        txtResultado.insert(0, 'O Aluno ' + nome + ' (' + idade + ' anos) foi aprovado!')
    else:
        lblResultado = Label(tela, text='O Aluno ' + nome + ' (' + idade + ' anos) foi reprovado!', font='Arial 16', fg='#000000', bg='#c0c0c0').place(x=30, y=350)
        txtResultado.delete(0, tk.END)
        txtResultado.insert(0, 'O Aluno ' + nome + ' (' + idade + ' anos) foi reprovado!')


btnCalcular = Button(tela, text='Calcular média', width=20, command=calcularMedia).place(x=30, y=310)
btnSalvar = Button(tela, text='Salvar no banco', width=20, command=salvarBanco).place(x=200, y=310)
txtResultado = Entry(tela, width=40, fg='#000000')
txtResultado.insert(0, 'Aguardando resultado...')
txtResultado.place(x=30, y=390)

tela.mainloop()