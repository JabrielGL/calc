from tkinter import *
import juros

def comando():
    result.delete(0,END)
    if v == "simples":
        result.insert(0,juros.JurosSimples(float(valor.get()),float(tempo.get()), float(perc.get())))
    else:
        result.insert(0,juros.JurosComposto(float(valor.get()),float(tempo.get()), float(perc.get())))

j = Tk()
j.geometry('300x400')
Label(j, text='Valor').place(x=50,y=50)
valor = Entry(j, fg='blue')
valor.place(x=130,y=50)
Label(j, text='Tempo').place(x=50,y=100)
tempo = Entry(j, fg='red')
tempo.place(x=130,y=100)
Label(j, text="Porcentagem").place(x=50,y=150)
perc = Entry(j, fg='#006400')
perc.place(x=130,y=150)
Label(j, text="%").place(x=260,y=150)
Label(j, text="Resultado").place(x=50,y=200)
result = Entry(j, fg='#FF8C00')
result.place(x=130,y=200)
v = StringVar()
simples = Radiobutton(j, text="Simples", variable=v, value="simples").place(x=70, y=250)
composto = Radiobutton(j, text="Composto", variable=v, value="composto").place(x=140,y=250)
v.set('simples')

Button(j, text="Calcular", command=comando).place(x=100,y=300)

j.mainloop()