from modules.screen import cleanScreen as clean, pauseScreen as pause
from modules.files import *



def addActives():
    clean()
    checkFile('actives.json')
    actives = {
        "codTransaccion" : "",
        "nroFormulario" : "",
        "codCampus" : "",
        "marca" : "",
        "categoria" : "",
        "tipo" : "",
        "valorUnitario" : 0,
        "proveedor" : "",
        "nroSerial" : "",
        "empresaResponsable" : "",
        "estado" : "",
        "historial" : [],
    }
    

