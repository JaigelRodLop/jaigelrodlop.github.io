import re
import random
from investigacion import tipos
from investigacion import met

tipoInv = tipos()
metInv = met()

def getResponse(userInput):
    splitMessage = re.split(r'\s|[,;.:?!-_]\s*',userInput.lower())
    response = checkMessages(splitMessage)
    return response

def messageProbability(userMessage,recognizedWords,singleResp=False,requiredWords=[]):
    messageCertanity = 0
    hasRequiredWords = True
    
    for word in userMessage:
        if word in recognizedWords:
            messageCertanity += 1
    
    percent = float(messageCertanity)/float(len(recognizedWords))
    
    for word in requiredWords:
        if word not in userMessage:
            hasRequiredWords = False
            break
    
    if hasRequiredWords or singleResp:
        return int(percent*100)
    else:
        return 0

def checkMessages(message):
    highestProb = {}
        
    def response(botResponse,listWords,singleResponse=False,requiredWords=[]):
        nonlocal highestProb
        highestProb[botResponse] = messageProbability(message,listWords,singleResponse,requiredWords)
    
    response('Hola',['hola','klk','saludos','buenas'],singleResponse=True)
    response('Estoy bien, ¿qué tal tú?',['como','estas','va','vas','sientes'],requiredWords=['como'])
    response('Siempre a la orden',['gracias','te agradezco','thanks'],singleResponse=True)
    
    response(tipoInv.concepto(),['investigacion'],requiredWords=['que','es'])
    response(tipoInv.tiposTotal(),['tipos','investigacion'],requiredWords=['tipos','investigacion'])
    response(tipoInv.comparativo(),['comparativa'],requiredWords=['comparativa'])
    response(tipoInv.correlacional(),['correlacional'],requiredWords=['correlacional'])
    response(tipoInv.cualitativo(),['cualitativa'],requiredWords=['cualitativa'])
    response(tipoInv.decaso(),['de','caso'],requiredWords=['de','caso'])
    response(tipoInv.demercardo(),['de','mercado'],requiredWords=['de','mercado'])
    response(tipoInv.descriptivo(),['descriptiva'],requiredWords=['descriptiva'])
    response(tipoInv.etnografico(),['etnografica'],requiredWords=['etnografica'])
    response(tipoInv.evaluativo(),['evaluativa'],requiredWords=['evaulativa'])
    response(tipoInv.experimental(),['experimental'],requiredWords=['experimental'])
    response(tipoInv.expostfacto(),['ex','post','facto'],requiredWords=['ex','post','facto'])
    response(tipoInv.historico(),['historica'],requiredWords=['historica'])
    response(tipoInv.participativo(),['participativa'],requiredWords=['participativa'])
    
    response(metInv.concepto(),['metodologia'],requiredWords=['que','es'])
    response(metInv.tiposTotal(),['tipos','metodologias'],requiredWords=['tipos','metodologias'])
    response(metInv.cualitativo(),['metodologia','cualitativa'],requiredWords=['cualitativa','metodologia'])
    response(metInv.cuantitativo(),['metodologia','cuantitativa'],requiredWords=['cuantitativa'])
    response(metInv.mixta(),['mixta'],requiredWords=['mixta'])
    
    bestMatch = max(highestProb,key=highestProb.get) # type: ignore
    
    return unknow() if highestProb[bestMatch] < 1 else bestMatch

def unknow():
    response = ['Disculpa, no entendí la pregunta.','¿Podrías repetirlo?','No comprendo tu consulta'][random.randrange(3)]
    return response

print('Bot: Soy tu amigable "BOT" sobre "INVESTIGACIÓN", escribe "exit()" cuando desees salir.')
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit()':
        print(["Bot: Adiós!","Bot: Ha sido un placer ayudar","Bot: Hasta la próxima usuario."][random.randrange(3)])
        break
    if getResponse(user_input) is None:
        print("Bot: ",unknow())
    print("Bot: ", getResponse(user_input))
