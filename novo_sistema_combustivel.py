import tkinter as tk
from tkinter import ttk

lista_combustiveis = {'gasolina':5.15, 'alcool':3.79, 'diesel':5.59}
lista_armazenamento = {'gasolina':200, 'alcool':200, 'diesel':200}


class Abastecimento():


#venda gasolina
    def pegar_litros_gasolina():
        valor = int(label_combustivel_litro.get())
        armazenamento = lista_armazenamento['gasolina'] - valor
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=0, columnspan=2)
        else:
            label_abastecimento = ttk.Label(text=f'Total a pagar: R${lista_combustiveis["gasolina"] * valor :.2f} reais')
            label_abastecimento.grid(row=6, column=0, columnspan=2)
            botao_abastecer_valor_gasolina.destroy()
            botao_abastecer_litro_gasolina.destroy()
        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7,column=1,columnspan=3)


    def pegar_valordinheiro_gasolina():
        valor = int((label_valorentrada.get()))
        armazenamento = lista_armazenamento['gasolina'] - valor/ lista_combustiveis['gasolina']
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=0, columnspan=2)
        else:
            label_abastecimento = tk.Label(text=f'Você abasteceu {valor / lista_combustiveis["gasolina"] :.2f} litros')
            label_abastecimento.grid(row=6, column=0, columnspan=2)
            botao_abastecer_litro_gasolina.destroy()
            botao_abastecer_valor_gasolina.destroy()
        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7, column=1, columnspan=3)

#venda alcool

    def pegar_litro_alcool ():
        valor = int(label_combustivel_litro_alcool.get())
        armazenamento = lista_armazenamento['alcool'] - valor
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=3, columnspan=2)
        else:
            label_abastecimento = tk.Label(text=f'Total a pagar: R${lista_combustiveis["alcool"] * valor :.2f} reais')
            label_abastecimento.grid(row=6, column=3, columnspan=2)
            botao_abastecer_litro_alcool.destroy()
            botao_abastecer_valor_alcool.destroy()
        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7,column=3,columnspan=3)


    def pegar_valordinheiro_alcool():
        valor = int((label_valorentrada2.get()))
        armazenamento = lista_armazenamento['alcool'] - valor/ lista_combustiveis['alcool']
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=3, columnspan=2)
        else:
            label_abastecimento = tk.Label(text=f'Você abasteceu {valor / lista_combustiveis["alcool"] :.2f} litros')
            label_abastecimento.grid(row=6, column=3, columnspan=2)
            botao_abastecer_litro_alcool.destroy()
            botao_abastecer_valor_alcool.destroy()

        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7, column=4, columnspan=3)

#diesel

    def pegar_litro_diesel ():
        valor = int(label_combustivel_litro_diesel.get())
        armazenamento = lista_armazenamento['diesel'] - valor
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=6, columnspan=2)
        else:
            label_abastecimento = tk.Label(text=f'Total a pagar: R${lista_combustiveis["diesel"] * valor :.2f} reais')
            label_abastecimento.grid(row=6, column=6, columnspan=2)
            botao_abastecer_litro_diesel.destroy()
            botao_abastecer_valor_diesel.destroy()
        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7,column=6,columnspan=3)

        valor = (label_combustivel_litro_diesel.select_clear)




    def pegar_valordinheiro_diesel():
        valor = int((label_valorentrada3.get()))
        armazenamento = lista_armazenamento['diesel'] - valor/ lista_combustiveis['diesel']
        if armazenamento <= 1:
            label = tk.Label(text='Não foi possivel abastecer!Combustivel insuficiente na bomba')
            label.grid(row=8,column=6, columnspan=2)
        else:
            label_abastecimento = tk.Label(text=f'Você abasteceu {valor / lista_combustiveis["diesel"] :.2f} litros')
            label_abastecimento.grid(row=6, column=6, columnspan=2)
            botao_abastecer_litro_diesel.destroy()
            botao_abastecer_valor_diesel.destroy()

        if armazenamento < 50:
            label_armazenamento = tk.Label(text=f'Só há {armazenamento}litros armazenados, favor reabastercer o armazém!')
            label_armazenamento.grid(row=7, column=7, columnspan=3)






root = tk.Tk()
root.title('Posto JAÚ')

titulo1 = tk.Label(text='Posto JAÚ')
titulo1.config(font=('Currier', 25))
titulo1.grid(row=1,column=1, columnspan=4, padx=15,pady=15, sticky='nwes')

label_valor = tk.Label(text='Valor:')
label_valor.grid(row=4,column=0,sticky='nsew')
label_valorentrada = tk.Entry()
label_valorentrada.grid(row=4, column=1)

label1 = tk.Label(text='Litros:')
label1.grid(row=5, column=0, sticky='nsew')
label_combustivel_litro = tk.Entry()
label_combustivel_litro.grid(row=5, column=1)

label_valor_alcool = tk.Label(text='Valor:')
label_valor_alcool.grid(row=4,column=3,sticky='nswe')
label_valorentrada2 = tk.Entry()
label_valorentrada2.grid(row=4, column=4)

label_2 = tk.Label(text='Litros:')
label_2.grid(row=5, column=3, sticky='nswe')
label_combustivel_litro_alcool = tk.Entry()
label_combustivel_litro_alcool.grid(row=5, column=4)


label_valor3 = tk.Label(text='Valor:')
label_valor3.grid(row=4,column=6)
label_valorentrada3 = tk.Entry()
label_valorentrada3.grid(row=4, column=7)

label_3 = tk.Label(text='Litros:')
label_3.grid(row=5, column=6)
label_combustivel_litro_diesel = tk.Entry()
label_combustivel_litro_diesel.grid(row=5, column=7)



abastecerGasolina = ttk.Label( text='Gasolina')
abastecerGasolina.config(font=('Currier', 12))
abastecerGasolina.grid(row=3, column=0, padx=50, pady=50, sticky='nswe')

abastecerAlcool = ttk.Label( text='Alcool' )
abastecerAlcool.config(font=('Currier', 12))
abastecerAlcool.grid(row=3, column=3, padx=50, pady=50, sticky='nswe')

abastecerDiesel = ttk.Label(text='Diesel')
abastecerDiesel.config(font=('Currier', 12))
abastecerDiesel.grid(row=3, column=6, padx=50, pady=50, sticky='nswe')
#botões gasolina
botao_abastecer_valor_gasolina = ttk.Button(text='Abastecer por litro',command=Abastecimento.pegar_litros_gasolina )
botao_abastecer_valor_gasolina.grid(row=8, column=0)

botao_abastecer_litro_gasolina = ttk.Button(text='Abastecer por valor',command=Abastecimento.pegar_valordinheiro_gasolina)
botao_abastecer_litro_gasolina.grid(row=8,column=1)
#botões alcool

botao_abastecer_valor_alcool = ttk.Button(text='Abastecer por litro',command=Abastecimento.pegar_litro_alcool )
botao_abastecer_valor_alcool.grid(row=8, column=3)

botao_abastecer_litro_alcool = ttk.Button(text='Abastecer por valor',command=Abastecimento.pegar_valordinheiro_alcool)
botao_abastecer_litro_alcool.grid(row=8,column=4)
#botões diesel
botao_abastecer_valor_diesel = ttk.Button(text='Abastecer por litro',command=Abastecimento.pegar_litro_diesel)
botao_abastecer_valor_diesel.grid(row=8, column=6)

botao_abastecer_litro_diesel = ttk.Button(text='Abastecer por valor',command=Abastecimento.pegar_valordinheiro_diesel)
botao_abastecer_litro_diesel.grid(row=8,column=7)


botao_fechar = ttk.Button(text='Fechar', command=root.quit)
botao_fechar.grid(row=10, column=3, pady=20,padx=20, sticky='nwes')


root.mainloop()