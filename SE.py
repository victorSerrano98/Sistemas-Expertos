import requests
import json
from transformers import pipeline
from googletrans import Translator

nlpPipe = pipeline("question-answering")

def traductor(texto, idioma):
    translator = Translator()
    translation = translator.translate(texto, dest= idioma)
    texto = translation.text
    return texto

def consulta(pregunta):
    respuesta = ""
    with open('D:\Documentos\SistemasExpertos\PlantasMedInformacion.json', encoding='latin-1') as file:
        data = json.load(file)
    for datos in data:
        if pregunta in datos['Sintomas']:
            print(datos['Planta'])
            question = "como se usa " + datos['Planta'] + " para " + pregunta + "?"
            question = traductor(question, 'en')

            contexto = datos['context']
            contexto = traductor(contexto, 'en')

            rest = nlpPipe(question=question, context=contexto)

            resp = traductor(rest['answer'], 'es')
            respuesta = respuesta + "Planta: " + datos['Planta'] + "\n \n" + "Preparación: " + resp + "\n \n \n"
    print(respuesta)
    print("")
    return respuesta