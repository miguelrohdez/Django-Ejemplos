from typing import ContextManager
from django.http import HttpResponse
from django.template import Template, Context
import datetime
from django.shortcuts import render
from django.template import loader

#Primera vista que devuleve una respuesta
def HolaMundo(request):
    fecha_act = datetime.datetime.now().year
    documento= '''
    <html>
        <head>
            <title> Hola </title>
        </head>
        <body>
            <h1> Hola Mundo </h1>
            <h2>La hora es: <span>%s</span> </h2>
        </body>
    </html>''' %fecha_act
    return HttpResponse(documento)

def edadFutura(request, anio, edadAct):
    direfencia = anio - datetime.datetime.now().year
    edadFutura = edadAct + direfencia
    pagina = '''
        <html>
        <head>
            <title> Calcular edad </title>
        </head>
        <body>
            <center>
                <h1> Calcula tu edad en el Futuro </h1>
                <h2>En el año %s tendras %s años </h2>
            </center>
        </body>
    </html>''' %(anio, edadFutura)
    return HttpResponse(pagina)

#Cargador manual
def edadFuturaTemplate(request, anio, edadAct):
    direfencia = anio - datetime.datetime.now().year
    edadFutura = edadAct + direfencia
    #Ruta donde esta la plantilla
    doc_externo = open("Proyecto1\Templates\PlantillaEdad.html")
    #Se lee la plantilla
    plt = Template(doc_externo.read())
    #Se cierra el documento
    doc_externo.close()
    #Se establece el contexto y las variables en caso de tener -> {"clave":valor}
    contexto = Context({"anioAct":anio,"edadFutura":edadFutura})
    #Se renderiza la pagina con el contexto
    pagina = plt.render(contexto)
    return HttpResponse(pagina)

#Cargador con Loader
def edadFuturaTemplateWtLoader(request, anio, edadAct):
    direfencia = anio - datetime.datetime.now().year
    edadFutura = edadAct + direfencia
    #Primero importar Templates.loader
    #Dentro de settings establecer la ruta donde estan las plantillas
    #Crear una varibles y cargar la plantilla con loader
    doc_externo = loader.get_template('PlantillaEdad.html') #loader devuelve un Template diferente
    #Pasar el contexto directamente como un diccionario
    pagina = doc_externo.render({"anioAct":anio,"edadFutura":edadFutura})
    return HttpResponse(pagina)

#Shortcuts
def edadFuturaTemplateShortcuts(request, anio, edadAct):
    direfencia = anio - datetime.datetime.now().year
    edadFutura = edadAct + direfencia
    #Request, Template, Diccionario
    return render(request, "PlantillaEdad.html",{"anioAct":anio,"edadFutura":edadFutura})

#Plantillas Incrustadas