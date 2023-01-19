import os
import openpyxl
import threading
import comtypes.client
from pathlib import *

nomexls = input("Informe a Planilha: ")


class ConvertWordPDF:

    def initbot(self):
            fontdir = Path(__file__).parent.resolve()
            p = os.path.join(fontdir, nomexls)


            wrkbk_input = openpyxl.load_workbook(filename=p)
            sheet_input = wrkbk_input.active
                    

            for i in range(1, sheet_input.max_row+1):
                    cell_obj = sheet_input.cell(row=i, column=1)
                    if cell_obj.value is not None and cell_obj.value != '':
                        docx_name = sheet_input.cell(row=i, column=1).value
                        
                        try:
                            self.convertpdf(name=docx_name)
                        except Exception as e:
                             print(e)
    
                    if i == sheet_input.max_row:
                            
                        print('fim do processo')

    def convertpdf(self, name):

        wdFormatPDF = 17
        currentdir = Path(__file__).parent.resolve()
        inputfile = os.path.join(currentdir, '{infile}'.format(infile=name))
        print(inputfile) 
        removedocx = inputfile.replace(".docx",".pdf")
        outpatch = removedocx
        
        
        # Cria instancia de um objeto COM para manipular Documentos Word
        word = comtypes.client.CreateObject('Word.Application')

        # Carrega Arquivo de entrada (.doc)
        doc = word.Documents.Open(inputfile)

        # Salva arquivo de saida em formato .pdf
        doc.SaveAs(outpatch, FileFormat=wdFormatPDF)

        # Fecha arquivo de Entrada
        doc.Close()

        # Finaliza instancia do Objeto COM criado
        word.Quit()

start = ConvertWordPDF()
start.initbot()
