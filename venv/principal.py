from tkinter import *
import juros

def comando():
    juros.JurosSimples(int(valor.get()),int(tempo.get()), int(perc.get()))


j = Tk()
j.geometry('800x600')
j['bg'] = 'gray'
Label(j, text='Valor', fg="#FFF", bg='gray').place(x=50,y=50)
valor = Entry(j, fg='blue')
valor.place(x=130,y=50)
Label(j, text='Tempo', fg="#FFF", bg='gray').place(x=50,y=100)
tempo = Entry(j, fg='blue')
tempo.place(x=130,y=100)
Label(j, text="Porcentagem", fg="white", bg='gray').place(x=50,y=150)
perc = Entry(j, fg='blue')
perc.place(x=130,y=150)
Label(j, text="%", fg='white', bg='gray').place(x=260,y=150)
fValor= Entry(j)
fValor.place(x=130,y=200)

Button(j, text="Calcular", command=comando).place(x=100,y=300)

j.mainloop()