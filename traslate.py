
"""
Traducto de palabras realizado con Python
"""

# Importamos la libreria request
import requests

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


f = open("file.txt", "r")
w = open("file_traslate.txt", "w")
line = f.readline()
while line:
	line = f.readline()
	ass = Traduccion("en", "es", line)
	write = str(ass)
	w.write(write)
	w.write("\n")
	print(write)
