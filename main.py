from pathlib import Path
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTImage, LTFigure

# Importamos la libreria request para la traduccion del texti
import requests

def pdf2txt(pdfname, txtname):
    btxt=False
    try:
        fp = open(pdfname, 'rb')
        parser = PDFParser(fp)
        doc = PDFDocument()
        parser.set_document(doc)
        doc.set_parser(parser)
        doc.initialize('')
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()

        laparams.char_margin = 1.0
        laparams.word_margin = 1.0
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        ncount=0
        print("pdf2txt %s..." % pdfname) # informa por consola del nombre de archivo

        # abre archivo de texto para la salida
        fptxt = open(txtname, 'w')
        # recorre el documento procesando cada página
        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            # recorre la página procesando cada objeto
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                    spagetxt = lt_obj.get_text().strip() + " "
                    if(spagetxt!=""):
                        btxt=True
                        fptxt.write(spagetxt)
                        print(spagetxt)
                elif isinstance(lt_obj, LTFigure):
                    print("LTFigure, pte implementar!")
                    spagetxt=""
            ncount+=1

        print("end")
        fptxt.closed
        fp.closed
    except Exception as e:
        print("Error: %s" % (e))
    
    
    return spagetxt
"""
/*
 *
 *
Traducto de palabras realizado con Python
 *
 *
 *
"""
 


def Traduccion(source, target, text):
	parametros = {'sl': source, 'tl': target, 'q': text}
	cabeceras = {"Charset":"UTF-8","User-Agent":"AndroidTranslate/5.3.0.RC02.130475354-53000263 5.1 phone TRANSLATE_OPM5_TEST_1"}
	url = "https://translate.google.com/translate_a/single?client=at&dt=t&dt=ld&dt=qca&dt=rm&dt=bd&dj=1&hl=es-ES&ie=UTF-8&oe=UTF-8&inputm=2&otf=2&iid=1dd3b944-fa62-4b55-b330-74909a99969e"
	response = requests.post(url, data=parametros, headers=cabeceras)
	if response.status_code == 200:
		for x in response.json()['sentences']:
			return x['trans']
	else:
		return "Ocurrió un error"


pdf2txt("BlackGolang.pdf", "file.txt")
