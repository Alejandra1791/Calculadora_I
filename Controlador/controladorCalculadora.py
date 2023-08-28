from Vista.calculadora import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
#Crear nuestra clase
class Controlador_Calculadora(QtWidgets.QMainWindow):
#creamos nuestro constructor
    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.InicializarGui()
# Metodos
    def InicializarGui(self):
#label
        self.ui.pantalla.setText("0")
        #botones numericos
        self.ui.cero.clicked.connect(self.ceroOprimido)
        self.ui.uno.clicked.connect(self.unoOprimido)
        self.ui.dos.clicked.connect(self.dosOprimido)
        self.ui.tres.clicked.connect(self.tresOprimido)
        self.ui.cuatro.clicked.connect(self.cuatroOprimido)
        self.ui.cinco.clicked.connect(self.cincoOprimido)
        self.ui.seis.clicked.connect(self.seisOprimido)
        self.ui.siete.clicked.connect(self.sieteOprimido)
        self.ui.ocho.clicked.connect(self.ochoOprimido)
        self.ui.nueve.clicked.connect(self.nueveOprimido)

#operaciones
        self.ui.suma.clicked.connect(self.sumaOprimido)
        self.ui.resta.clicked.connect(self.restaOprimido)
        self.ui.multiplicacion.clicked.connect(self.multiplicarOprimido)
        self.ui.division.clicked.connect(self.divisionOprimido)
        self.ui.igual.clicked.connect(self.realizarOperacion)

        #limpiar
        self.ui.limpiar.clicked.connect(self.limpiarPantalla)
        #Funciones
    def ceroOprimido(self):
        texto = self.ui.pantalla.text()
        if texto != "0":
            self.ui.pantalla.setText(texto + "0")
    
    def unoOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":   
            self.ui.pantalla.setText("1")
        else: 
            self.ui.pantalla.setText(texto + "1")
    
    def dosOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":
            self.ui.pantalla.setText("2")
        else: 
            self.ui.pantalla.setText(texto +"2")

    def tresOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("3")
        else: 
            self.ui.pantalla.setText(texto +"3")

    def cuatroOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("4")
        else: 
            self.ui.pantalla.setText(texto + "4")

    def cincoOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("5")
        else:
            self.ui.pantalla.setText(texto + "5")
    
    def seisOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("6")
        else:
            self.ui.pantalla.setText(texto + "6")
    
    def sieteOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("7")
        else:
            self.ui.pantalla.setText(texto + "7")

    def ochoOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("8")
        else:
            self.ui.pantalla.setText(texto + "8")

    def nueveOprimido(self):
        texto = self.ui.pantalla.text()
        if texto == "0":  
            self.ui.pantalla.setText("9")
        else:
            self.ui.pantalla.setText(texto + "9")
    
    def sumaOprimido(self):
        texto =self.ui.pantalla.text()
        self.ui.pantalla.setText(texto + "+")
    
    def restaOprimido(self):
        texto =self.ui.pantalla.text()
        self.ui.pantalla.setText(texto + "-")

    def multiplicarOprimido(self):
        texto =self.ui.pantalla.text()
        self.ui.pantalla.setText(texto + "*")

    def divisionOprimido(self):
        texto =self.ui.pantalla.text()
        self.ui.pantalla.setText(texto + "/")
    
    def limpiarPantalla(self):
        self.ui.pantalla.setText("0")

    def realizarOperacion(self):
        operacion = self.ui.pantalla.text()
        #eval evaluate =evaluar.coge una operacion matematica de un string y lo convierte en codigo y devuelve resultado
        self.ui.pantalla.setText(str(eval(operacion)))

