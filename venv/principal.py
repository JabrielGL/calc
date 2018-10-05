from tkinter import *
import juros

def comando():

    if v.get() == "Simples":
        if valor.get() =="" and result.get()!="" and perc.get()!="" and tempo.get()!="":
            valor.delete(0,END)
            valor.insert(0, juros.SimplesInicial(float(result.get()), float(perc.get()), float(tempo.get())))
        elif tempo.get()=="" and result.get()!="" and perc.get()!="" and valor.get()!="":
            tempo.delete(0,END)
            tempo.insert(0, juros.SimplesTempo(float(result.get()), float(valor.get()) ,float(perc.get())))
        elif perc.get()=="" and result.get()!="" and tempo.get()!="" and valor.get()!="":
            perc.delete(0,END)
            perc.insert(0, juros.SimplesJuros(float(result.get()), float(valor.get()) ,float(tempo.get())))
        elif result.get() =="" and valor.get()!="" and perc.get()!="" and tempo.get()!="":
            result.delete(0, END)
            result.insert(0, juros.JurosSimples(float(valor.get()), float(perc.get()), float(tempo.get())))
        else:
            toplevel = Toplevel()
            Label(toplevel, text="Por favor, informe 3 campos!").pack()
    elif v.get() == "Composto":
        if valor.get() =="" and result.get()!="" and perc.get()!="" and tempo.get()!="":
            valor.delete(0, END)
            valor.insert(0, juros.CompostoInicial(float(result.get()), float(perc.get()), float(tempo.get())))
        elif tempo.get() == "" and result.get() != "" and perc.get() != "" and valor.get() != "":
            tempo.delete(0, END)
            tempo.insert(0, juros.CompostoTempo(float(result.get()), float(valor.get()), float(perc.get())))
        elif perc.get() == "" and result.get() != "" and tempo.get() != "" and valor.get() != "":
            perc.delete(0,END)
            perc.insert(0, juros.CompostoJuros(float(result.get()), float(valor.get()) ,float(tempo.get())))
        elif result.get() == "" and valor.get() != "" and perc.get() != "" and tempo.get() != "":
            result.insert(0, juros.JurosComposto(float(valor.get()), float(perc.get()), float(tempo.get())))
        else:
            toplevel = Toplevel()
            Label(toplevel, text="Por favor, informe 3 campos!").pack()

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
simples = Radiobutton(j, text="Simples", variable=v, value="Simples").place(x=70, y=250)
composto = Radiobutton(j, text="Composto", variable=v, value="Composto").place(x=140,y=250)
v.set("Simples")

Button(j, text="Calcular", command=comando).place(x=100,y=300)

j.mainloop()