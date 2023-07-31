import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.withdraw()

messagebox.showwarning("Calculadora IMC!", "Olá! Seja bem vindo a versão 2.0 da calculadora IMC. Precione OK para continuar...")

nome = simpledialog.askstring("Passo 1..." , "Para começar, nos informe seu nome...")

peso = simpledialog.askfloat("Passo 2", "Agora, nos informe seu peso...")

altura = simpledialog.askfloat("Passo 3", "Por fim, nos informe sua altura em METROS...")

imc = peso / (altura * altura)

if imc < 18.5:
    messagebox.showwarning("Resultado", "Olá " + nome + " você está abaixo do peso!")
elif imc >= 18.5 and imc < 25.0:
    messagebox.showinfo("Resultado", "Olá " + nome + " você está no peso ideal!")
elif imc >= 25.0 and imc < 30.0:
    messagebox.showwarning("Resultado", "Olá " + nome + " você está com sobrepeso!")
elif imc >= 30.0 and imc < 35.0:
    messagebox.showerror("Resultado", "Olá " + nome + " você está com Obesidade Nível I!")
elif imc >= 35.0 and imc < 40.0:
    messagebox.showerror("Resultado", "Olá " + nome + " você está com Obesidade Nível II!")
else:
    messagebox.showerror("Resultado", "Olá " + nome + " você está com Obesidade Nível III!")
