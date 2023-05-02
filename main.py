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

        self.IniciarUpload.clicked.connect(lambda: self.initbot(input_filename=self.lineEndr.text()))
    
    def openfile(self):
        input_filename = QtWidgets.QFileDialog.getOpenFileName()[0]
        self.lineEndr.setText(input_filename)
                

    def initbot(self, input_filename):
            self.p = input_filename


            wrkbk_input = openpyxl.load_workbook(filename=self.p)
            sheet_input = wrkbk_input.active
                    

            for i in range(1, sheet_input.max_row+1):
                    cell_obj = sheet_input.cell(row=i, column=1)
                    if cell_obj.value is not None and cell_obj.value != '':
                        docx_name = sheet_input.cell(row=i, column=1).value


                        wordir = checkdir().find_all(
                             exefile='winword.exe', 
                             pathfile=r'c:/Program Files')
                        if wordir is True:
                            try:
                                self.convertpdf(namefile=docx_name)
                            except Exception as e:
                                print(e)
                        else:
                             self.pdfinsoffice(namefile=docx_name)
        
            if i == sheet_input.max_row:
                print('fim do processo')
                showinfo('Sucesso!', 'Todos os documentos foram convertidos com sucesso!')

    def convertpdf(self, namefile):

        wdFormatPDF = 17
        currentdir = Path(self.p).parent.resolve()
        inputfile = os.path.join(currentdir, '{infile}'.format(infile=namefile))
        print(inputfile) 
        removedocx = inputfile.replace(".docx",".pdf")
        outpatch = removedocx
        
        
        # Cria instancia de um objeto COM para manipular Documentos Word
        word = comtypes.client.CreateObject('Word.Application')

        # Carrega Arquivo de entrada (.doc)
        doc = word.Documents.Open(inputfile)
        print(colored('Convertendo arquivo "{a}"...'.format(a=namefile), 'yellow'))

        try:
            
            # Salva arquivo de saida em formato .pdf
            doc.SaveAs(outpatch, FileFormat=wdFormatPDF)

            # Fecha arquivo de Entrada
            doc.Close()

            # Finaliza instancia do Objeto COM criado
            word.Quit()
            print(colored('Documento Convertido com Sucesso!', 'green'))

        except:
            print(colored('Não foi possível converter o arquivo "{b}"'.formar(b=namefile), 'red'))  

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
            arquivo_de_entrada = os.path.join(currentdir, '{infile}'.format(infile=namefile))
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
    