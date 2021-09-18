import math
from tkinter import *        #Importo tkinter, * para todas sus funciones

#Metodo --> set --> para asignar un valor, Ej: dato.set(23)
#Metodo --> get --> para obtener un valor, Ej: dato.get()

#Creo ventana

ventana =Tk()

ventana.title("Calculadora")            #Titulo de la ventana
ventana.geometry("320x400")             #Geometria de la ventana

#Funciones Botones Numericos

operador=""
texto_pantalla =StringVar()
r=""
texto_pantalla.set("0")

def cambiarSigno():
    global r
    global operador
    if r != "":
        r = float(r)*(-1)
        r=str(r)
        texto_pantalla.set(r)
    else:
        operador=float(operador)*(-1)
        operador = str(operador)
        texto_pantalla.set(operador)

def delete():
    global operador
    if r!="":
        clear()
    else:
        operador = operador[:-1]
        texto_pantalla.set(operador)

def fraccion():                 #Divide el numero 1/
    global operador
    global r

    if r!="":
        try:
            r=1/float(r)
            r = str(r)
            texto_pantalla.set(r)
        except:
            r = "ERROR"
            texto_pantalla.set(r)
    else:
        try:
            operador = 1/float(operador)
            operador = str(operador)
            texto_pantalla.set(operador)
        except:
            operador = "ERROR"
            texto_pantalla.set(operador)

def exponente():
    global operador
    global r
    if r!="":
        r=float(r)*float(r)
        r = str(r)
        texto_pantalla.set(r)
    else:
        operador = float(operador)*float(operador)
        operador = str(operador)
        texto_pantalla.set(operador)

def raiz():
    global operador
    global r
    if r!="":
        try:
            r = math.sqrt(float(r))
            texto_pantalla.set(r)
        except:
            r = "ERROR"
            texto_pantalla.set(r)
    else:
        try:
            operador = math.sqrt(float(operador))
            texto_pantalla.set(operador)
        except:
            r = "ERROR"
            texto_pantalla.set(r)

def clear():                #Se activa cuando da click en C
    global operador
    global r
    operador=""
    r=""
    texto_pantalla.set("0")


def click(b):           #b el contenido del boton a pantalla
    global operador
    global r
    if r=="ERROR" or operador=="ERROR":
        clear()
    elif r!="":
        r=r+str(b)
        texto_pantalla.set(r)           #Cada vez que se unda un boton el texto_pantalla será operador
    else:
        operador = operador + str(b)
        texto_pantalla.set(operador)        #Cada vez que se unda un boton el texto_pantalla será operador

def resultado ():           #Se activa cuando da click en =
    global operador
    global r
    if r!="":
        try:
            r = str(eval(r))
        except:
            r = "ERROR"
        texto_pantalla.set(r)
    else:
        try:
            r = str(eval(operador))
        except:
            r="ERROR"
        texto_pantalla.set(r)

#Entrada de texto       #width-> ancho, height->Altura, justify=comience a la derecha

entradaNumero=Entry(ventana,font = ('Times New Roman',30,"roman"),textvariable=texto_pantalla).place(x= 25, y =20, width=270, height=60)
                                                                                 #Que se muestre lo que sea texto_pantalla

#Botones

#Numeros            #width-> ancho, height->Altura
                    #bg --> color del boton (fondo)
                    # fg --> Color del texto del boton

boton0=Button(ventana,text="0",command=lambda:click(0),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=80,y=335, width=50 , heigh=50 )
boton1=Button(ventana,text="1",command=lambda:click(1),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=25,y=280, width=50 , heigh=50 )
boton2=Button(ventana,text="2",command=lambda:click(2),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=80,y=280, width=50 , heigh=50 )
boton3=Button(ventana,text="3",command=lambda:click(3),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=135,y=280, width=50 , heigh=50 )
boton4=Button(ventana,text="4",command=lambda:click(4),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=25,y=225, width=50 , heigh=50 )
boton5=Button(ventana,text="5",command=lambda:click(5),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=80,y=225, width=50 , heigh=50 )
boton6=Button(ventana,text="6",command=lambda:click(6),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=135,y=225, width=50 , heigh=50 )
boton7=Button(ventana,text="7",command=lambda:click(7),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=25,y=170, width=50 , heigh=50 )
boton8=Button(ventana,text="8",command=lambda:click(8),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=80,y=170, width=50 , heigh=50 )
boton9=Button(ventana,text="9",command=lambda:click(9),font = ('Times New Roman',15),bg="#000000",fg="#FFFFFF").place(x=135,y=170, width=50 , heigh=50 )


botonComa=Button(ventana,text=",",command=lambda:click("."),font = ('Times New Roman',15),bg="#494949",fg="#FFFFFF").place(x=135,y=335, width=50 , heigh=50 )
botonPositivoNegativo=Button(ventana,text="+/-",command=cambiarSigno,font = ('Times New Roman',15),bg="#494949",fg="#FFFFFF").place(x=25,y=335, width=50 , heigh=50 )
botonExponenteCuadrado=Button(ventana,text="x²",command=exponente,font = ('Times New Roman',15),bg="#494949",fg="#FFFFFF").place(x=80,y=115, width=50 , heigh=50 )
botonRaiz=Button(ventana,text="√x",command=raiz,font = ('Times New Roman',15),bg="#494949",fg="#FFFFFF").place(x=135,y=115, width=50 , heigh=50 )
boton1fraccion=Button(ventana,text="1/x",command=fraccion,font = ('Times New Roman',15),bg="#494949",fg="#FFFFFF").place(x=25,y=115, width=50 , heigh=50 )
botonLimpiaC=Button(ventana,text="C",command=clear,font = ('Times New Roman',15,"bold"),bg="#494949",fg="#FFFFFF").place(x=190,y=115, width=50 , heigh=50 )

#OPERACIONES BOTONES
botonDivision=Button(ventana,text="÷",command=lambda:click("/"),font = ('Times New Roman',20,"bold"),bg="#494949",fg="#FFFFFF").place(x=190,y=170, width=50 , heigh=50 )
botonMultiplicacion=Button(ventana,text="*",command=lambda:click("*"),font = ('Times New Roman',15,"bold"),bg="#494949",fg="#FFFFFF").place(x=190,y=225, width=50 , heigh=50 )
botonResta=Button(ventana,text="-",command=lambda:click("-"),font = ('Times New Roman',20,"bold"),bg="#494949",fg="#FFFFFF").place(x=190,y=280, width=50 , heigh=50 )
botonSuma=Button(ventana,text="+",command=lambda:click("+"),font = ('Times New Roman',20,"bold"),bg="#494949",fg="#FFFFFF").place(x=190,y=335, width=50 , heigh=50 )
botonIgual=Button(ventana,text="=",command=resultado,font = ('Times New Roman',20,"bold"),bg="#DD667A",fg="#000000").place(x=245,y=335, width=50 , heigh=50 )

#BotonBorrar
botonBorrar=Button(ventana,text="⇦",command = delete, font = ('Times New Roman',20,"bold"),bg="#494949",fg="#FFFFFF").place(x=245,y=115, width=50 , heigh=50 )

#Parentesis
botonIzquierdo=Button(ventana,text="(",command=lambda:click("("),font = ('Times New Roman',15,"bold"),bg="#494949",fg="#FFFFFF").place(x=245,y=170, width=50 , heigh=50 )
botonDerecho=Button(ventana,text=")",command=lambda:click(")"),font = ('Times New Roman',15,"bold"),bg="#494949",fg="#FFFFFF").place(x=245,y=225, width=50 , heigh=50 )

ventana.mainloop()