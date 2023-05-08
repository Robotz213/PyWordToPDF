from PySide2.QtWidgets import(QApplication, QWidget)
from PyQt5 import QtWidgets
import os
import sys
import openpyxl
from subprocess import Popen
from Scripts.ui_uploadfiles import Ui_Upload
import os
import openpyxl
from subprocess import Popen
import comtypes.client
from pathlib import *
from checkword import checkdir
from termcolor import colored
import sys
from tkinter.messagebox import showinfo




class Uploadfiles(QWidget, Ui_Upload):

    def __init__(self) -> None:
        super(Uploadfiles, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Convert To PDF")
        self.BuscarPlanilha.clicked.connect(lambda: self.openfile())
        self.listfiles = []
        self.IniciarUpload.clicked.connect(lambda: self.initbot(input_filename=self.listfiles))
    
    def openfile(self):
        input_filename = QtWidgets.QFileDialog.getOpenFileNames(
                filter="Arquivo DOCX (*.docx)")[0]
        for filename in input_filename:
            self.listfiles.append(filename)
        input_filenames_str = "\n".join(input_filename)
        self.lineEndr.setText(input_filenames_str)           

    def initbot(self, input_filename):
            
            
            for filename in input_filename:
                self.p = filename
                docx_name = filename

                self.pdfinsoffice(namefile=docx_name)


    def pdfinsoffice(self, namefile):

        path = 'c:\\Program Files\\'
        name = 'soffice.exe'
        
        print(colored('Convertendo arquivo "{a}"...'.format(a=namefile), 'yellow'))
        if sys.platform == 'linux':
            currentdir = Path(self.p).parent.resolve()
            arquivo_de_entrada = os.path.join(currentdir, '{infile}'.format(infile=namefile))
            outfile = os.path.join(currentdir)
            
            print(colored('Convertendo arquivo "{a}"...'.format(a=namefile), 'blue'))
            
            try:
                p = Popen(['soffice', '--headless', '--convert-to', 'pdf', '--outdir', outfile , arquivo_de_entrada])
                p.communicate()
                print(colored('Documento Convertido com Sucesso!', 'green'))
            except:
                print(colored('Não foi possível converter o arquivo "{b}"'.formar(b=namefile), 'red'))
        else:
            LIBRE_OFFICE = ''
            for root, dirs, files in os.walk(path):
                if name in files:
                    LIBRE_OFFICE = os.path.join(root, name)

            currentdir = Path(self.p).parent.resolve()
            arquivo_de_entrada = namefile
            outfile = os.path.join(currentdir)
            
            try:
                p = Popen([LIBRE_OFFICE, '--headless', '--convert-to', 'pdf', '--outdir', outfile , arquivo_de_entrada])
                p.communicate()
                print(colored('Documento Convertido com Sucesso!', 'green'))
            except:
                print(colored('Não foi possível converter o arquivo "{b}"'.formar(b=namefile), 'red'))
  
if __name__ == "__main__":
    
    
    app = QApplication(sys.argv)
    window = Uploadfiles()
    window.show()
    app.exec_()
    