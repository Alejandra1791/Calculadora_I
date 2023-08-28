from PyQt5 import QtWidgets
from Controlador.controladorCalculadora import Controlador_Calculadora
import sys

if __name__ == "__main__":
    #creamos nuestra aplicacion
    app = QtWidgets.QApplication(sys.argv)
    #creamos nuestra ventana
    windowExample = Controlador_Calculadora()
    #nombre a la pantalla titulo de la aplicacion 
    windowExample.setWindowTitle("Calculadora")
    #se muestra lo anterior o toda la aplicacion 
    windowExample.show()
    #se cierra la aplicacion
    sys.exit(app.exec_())

