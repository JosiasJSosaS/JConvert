from tkinter import *

def Split(word):
    return [char for char in word]

def ConvertirABinario(Entrada):
    Salida = []
    SalidaFin = []

    for c in Entrada:
        Salida.append(str(format(ord(c), 'b')))
    
    for i in range(len(Salida)):
        Salida[i] = Split(Salida[i])

    for i in range(len(Salida)):
        while len(Salida[i]) < 8:
            Salida[i].insert(0, "0")

    for i in range(len(Salida)):
        for k in range(len(Salida[0])):
            SalidaFin.append(Salida[i][k])

    for i in range(8,len(SalidaFin) + 1,9):
        if i == 0:
            continue
        SalidaFin.insert(i," ")

    SalidaFin = ''.join(SalidaFin)

    return SalidaFin

def ConvertirAHexadecimal(Entrada):

    Salida = []
    SalidaFin = []

    for c in Entrada:
        Salida.append(str('%x' % ord(c)))

    for i in range(len(Salida)):
        Salida[i] = Split(Salida[i])
    
    for i in range(len(Salida)):
        while len(Salida[i]) < 2:
            Salida[i].insert(0, "0")

    for i in range(len(Salida)):
        for k in range(len(Salida[0])):
            SalidaFin.append(Salida[i][k])

    for i in range(2, len(SalidaFin) * 16, 3):
        if i == 0:
            continue
        SalidaFin.insert(i," ")

    SalidaFin = ''.join(SalidaFin)

    SalidaFin = SalidaFin.strip()

    return SalidaFin

def ConvertirAOctal(Entrada):
    Salida = []
    SalidaFin = []

    for c in Entrada:
        Salida.append(str('%o' % ord(c)))

    for i in range(len(Salida)):
        Salida[i] = Split(Salida[i])
    
    for i in range(len(Salida)):
        while len(Salida[i]) < 3:
            Salida[i].insert(0, "0")

    for i in range(len(Salida)):
        for k in range(len(Salida[0])):
            SalidaFin.append(Salida[i][k])

    for i in range(3, len(SalidaFin) * 16, 4):
        if i == 0:
            continue
        SalidaFin.insert(i," ")

    SalidaFin = ''.join(SalidaFin)

    SalidaFin = SalidaFin.strip()

    return SalidaFin

def ConvertirAAlfanumerico(Entrada, Sel):
    Entrada = Entrada.split()
    Salida = []
    if Sel == "b":
        for Valor in Entrada:
            Salida.append(chr(int(Valor, 2)))
        Salida = ''.join(Salida)

    elif Sel == "o":
        for Valor in Entrada:
            Salida.append(chr(int(Valor, 8)))
        Salida = ''.join(Salida)

    elif Sel == "h":
        for Valor in Entrada:
            Salida.append(chr(int(Valor, 16)))
        Salida = ''.join(Salida)

    elif Sel == "d":
        for Valor in Entrada:
            Salida.append(chr(int(Valor)))
        Salida = ''.join(Salida)

    return Salida

def ConvertirADecimal(Entrada):
    Salida = []
    SalidaFin = []

    for c in Entrada:
        Salida.append(str(ord(c)))

    for i in range(len(Salida)):
        Salida[i] = Split(Salida[i])
    
    for i in range(len(Salida)):
        while len(Salida[i]) < 3:
            Salida[i].insert(0, "0")

    for i in range(len(Salida)):
        for k in range(len(Salida[0])):
            SalidaFin.append(Salida[i][k])

    for i in range(3, len(SalidaFin) * 16, 4):
        if i == 0:
            continue
        SalidaFin.insert(i," ")

    SalidaFin = ''.join(SalidaFin)

    SalidaFin = SalidaFin.strip()

    return SalidaFin

def Convertir():
    Text1["state"] = NORMAL
    Text2["state"] = NORMAL
    Text3["state"] = NORMAL
    Text4["state"] = NORMAL

    Text1.delete(0.0, END)
    Text2.delete(0.0, END)
    Text3.delete(0.0, END)
    Text4.delete(0.0, END)
    IN = TextEntrada.get(0.0, END)

    ConvertirADecimal(str(IN))

    if Seleccion.get() == "a":
        Label1["text"] = "Binario:"
        Text1.insert(0.0, ConvertirABinario(Split(str(IN)))) 
        Label2["text"] = "Hexadecimal:"
        Text2.insert(0.0, ConvertirAHexadecimal(Split(str(IN))))
        Label3["text"] = "Octal:"
        Text3.insert(0.0, ConvertirAOctal(Split(str(IN))))
        Label4["text"] = "Decimal"
        Text4.insert(0.0, ConvertirADecimal(Split(str(IN))))

    elif Seleccion.get() == "b":
        Label1["text"] = "Alfanumerico:"
        Text1.insert(0.0, ConvertirAAlfanumerico(IN, 'b'))
        Label2["text"] = "Hexadecimal:"
        Text2.insert(0.0, ConvertirAHexadecimal(Split(str(ConvertirAAlfanumerico(IN, 'b')))))
        Label3["text"] = "Octal:"
        Text3.insert(0.0, ConvertirAOctal(Split(str(ConvertirAAlfanumerico(IN, 'b')))))
        Label4["text"] = "Decimal:"
        Text4.insert(0.0, ConvertirADecimal(Split(str(ConvertirAAlfanumerico(IN, 'b')))))

    elif Seleccion.get() == "o":
        Label1["text"] = "Alfanumerico:"
        Text1.insert(0.0, ConvertirAAlfanumerico(IN, 'o'))
        Label2["text"] = "Binario:"
        Text2.insert(0.0, ConvertirABinario(Split(str(ConvertirAAlfanumerico(IN, 'o')))))
        Label3["text"] = "Hexadecimal:"
        Text3.insert(0.0, ConvertirAHexadecimal(Split(str(ConvertirAAlfanumerico(IN, 'o')))))
        Label4["text"] = "Decimal:"
        Text4.insert(0.0, ConvertirADecimal(Split(str(ConvertirAAlfanumerico(IN, 'o')))))

    elif Seleccion.get() == "h":
        Label1["text"] = "Alfanumerico:"
        Text1.insert(0.0, ConvertirAAlfanumerico(IN, 'h'))
        Label2["text"] = "Binario:"
        Text2.insert(0.0, ConvertirABinario(Split(str(ConvertirAAlfanumerico(IN, 'h')))))
        Label3["text"] = "Octal:"
        Text3.insert(0.0, ConvertirAOctal(Split(str(ConvertirAAlfanumerico(IN, 'h')))))
        Label4["text"] = "Decimal:"
        Text4.insert(0.0, ConvertirADecimal(Split(str(ConvertirAAlfanumerico(IN, 'h')))))

    elif Seleccion.get() == "d":
        Label1["text"] = "Alfanumerico:"
        Text1.insert(0.0, ConvertirAAlfanumerico(IN, 'd'))
        Label2["text"] = "Binario:"
        Text2.insert(0.0, ConvertirABinario(Split(str(ConvertirAAlfanumerico(IN, 'd')))))
        Label3["text"] = "Octal:"
        Text3.insert(0.0, ConvertirAOctal(Split(str(ConvertirAAlfanumerico(IN, 'd')))))
        Label4["text"] = "Hexadecimal:"
        Text4.insert(0.0, ConvertirAHexadecimal(Split(str(ConvertirAAlfanumerico(IN, 'd')))))

    Text1["state"] = DISABLED
    Text2["state"] = DISABLED
    Text3["state"] = DISABLED
    Text4["state"] = DISABLED

win1 = Tk()
win1.resizable(width=False, height=False)
win1.geometry("365x470")
win1.call('wm', 'iconphoto', win1._w, PhotoImage(file='JConvert!.gif'))
win1.title("JConvert!")

Seleccion = StringVar(value='a')

SeleccionFrame = Frame(win1)
SeleccionFrame.place(x = 10, y = 70, anchor = "nw")
CSFrame = Frame(win1)
CSFrame.place(x = 60, y = 330, anchor = "nw")
SalidasFrame = Frame(win1)
SalidasFrame.place(x = 200, y = 10, anchor = "nw")

ButtonSalir = Button(CSFrame, text = "Salir", command = win1.destroy, fg = "red")
ButtonSalir.pack(side = "bottom")

ButtonConvertir = Button(CSFrame, text = "Convertir", command = Convertir, fg = "blue")
ButtonConvertir.pack(side = "bottom")

LEntrada = Label(win1, text = "Entrada:")
TextEntrada = Text(win1, height = 5, width = 18, bd = 5)
LEntrada.place(x = 20, y = 200, anchor = "nw")
TextEntrada.place(x = 20, y = 230, anchor = "nw")

RadioO = Radiobutton(SeleccionFrame, text = "Convertir de Octal", variable = Seleccion, value = "o")
RadioH = Radiobutton(SeleccionFrame, text = "Convertir de Hexadecimal", variable = Seleccion, value = "h")
RadioB = Radiobutton(SeleccionFrame, text = "convertir de Binario", variable = Seleccion, value = "b")
RadioA = Radiobutton(SeleccionFrame, text = "Convertir de Alfanumerico", variable = Seleccion, value = "a")
RadioD = Radiobutton(SeleccionFrame, text = "Convertir de Decimal", variable = Seleccion, value = "d")
RadioA.pack()
RadioO.pack()
RadioH.pack()
RadioB.pack()
RadioD.pack()

Label1 = Label(SalidasFrame, text = "Binario:")
Text1 = Text(SalidasFrame, height = 5, width = 18, bd = 5, state = DISABLED)
Label2 = Label(SalidasFrame, text = "Hexadecimal:")
Text2 = Text(SalidasFrame, height = 5, width = 18, bd = 5, state = DISABLED)
Label3 = Label(SalidasFrame, text = "Octal:")
Text3 = Text(SalidasFrame, height = 5, width = 18, bd = 5, state = DISABLED)
Label4 = Label(SalidasFrame, text = "Decimal:")
Text4 = Text(SalidasFrame, height = 5, width = 18, bd = 5, state = DISABLED)
Label1.pack()
Text1.pack()
Label2.pack()
Text2.pack()
Label3.pack()
Text3.pack()
Label4.pack()
Text4.pack()

mainloop()