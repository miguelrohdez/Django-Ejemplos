from django.http import HttpResponse
import datetime
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
