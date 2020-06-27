# -*- coding: utf-8 -*-
'''
Registro de presença e participação no chat do MConf
por Fernando Rauber em 22/06/2020

Exemplo de formato da mensagem: 
[13:52] ANA BEATRIZ MICHELS : Olá, Profes! Boa tarde para nós... :)
'''

import codecs
import sys
import subprocess

class Aluno:
    def __init__(self, nome, msgs, chars):
        self.nome = nome
        self.msgs = msgs
        self.chars = chars
        
class Mensagem:
    def __init__(self, nome, hora, msg):        
        self.nome  = nome
        self.hora = hora        
        self.msg = msg

    def __str__(self):
        return (str(self.nome) + ' - ' + str(self.hora) + ' - ' + str(self.msg))

def getMsgs(obj):
    return obj.msgs

def getChars(obj):
    return obj.chars

ListaMsg = []
ListaPresenca = []
ListaAlunos = []
mensagens = []
msgCount = 0

if not len(sys.argv) > 1:
	print("Arraste o histórico de mensagens do MConf para este executável!\n\nPressione qualquer tecla para fechar...")
	input()
	sys.exit()

with codecs.open(sys.argv[1], 'r', encoding='utf8') as f:
    mensagens = f.readlines()

saida = sys.argv[1]
saida = saida[:-4] + "_analise.txt"

with codecs.open(saida, 'w', encoding='utf8') as f2:
    # lê mensagens
    for msg in mensagens:
        h1 = msg.find("[") + len("[")   # hora
        h2 = msg.find("]")
        hora = msg[h1:h2]

        nome = msg.split(':')    # nome
        if len(nome)>1:
            nome = (nome[1])[4:]     

        m = msg.find(" : ")   # mensagem
        mensagem = msg[m+3:]        
        
        # Filtra mensagens mal-formatadas (quebras de linha, avisos)
        Descartar = False        
        if msg.find(" : ") == -1 or msg.find("[") == -1 or msg.find("]") == -1 or len(msg) < 10:
            Descartar=True                
        
        # Monta lista de mensagens válidas
        if Descartar==False:
            MSG = Mensagem(nome, hora, mensagem)
            ListaMsg.append(MSG)
    
    for msg in ListaMsg:    
        # Lista de Presença
        nome = msg.nome
        if nome not in ListaPresenca:
            ListaPresenca.append(nome)
            ListaAlunos.append( Aluno(nome, 1, len(msg.msg) ) )
            msgCount += 1
        elif nome in ListaPresenca:
            # conta mensagens e caracteres
            for aluno in ListaAlunos:
                if aluno.nome == nome:
                    aluno.msgs += 1
                    aluno.chars += len(msg.msg)
                    msgCount += 1
    
    # Organiza listas (presença e participação)
    ListaPresenca = sorted(ListaPresenca)
    PartMsgs = sorted(ListaAlunos, key=getMsgs, reverse=True)
    PartChars = sorted(ListaAlunos, key=getChars, reverse=True)
    
    f2.write( "Lista de presença (Alunos participantes no chat = " + str( len(ListaPresenca) ) + ")\n")
        
    for presenca in ListaPresenca:
        f2.write(presenca + "\n")        
    
    
    if len(ListaPresenca) > 5:    
        f2.write("\nTop 5 participação (mensagens):" + "\n")                
        for i in range(0,5):        
            f2.write(PartMsgs[i].nome + " (" + str(PartMsgs[i].msgs) + " mensagens, " + str(PartMsgs[i].chars) + " caracteres, " + str( round(PartMsgs[i].msgs*100 / int(msgCount), 2) ) + "%)\n")    
    
        f2.write("\nTop 5 participação (caracteres):" + "\n")                
        for i in range(0,5):        
            f2.write(PartChars[i].nome + " (" + str(PartChars[i].msgs) + " mensagens, " + str(PartChars[i].chars) + " caracteres, " + str( round(PartChars[i].msgs*100 / int(msgCount), 2) ) + "%)\n")    

    f2.write("\nParticipação por mensagens (total = " + str(msgCount) + ")\n")
    for aluno in PartMsgs:
        f2.write(aluno.nome + " (" + str(aluno.msgs) + " mensagens, " + str( round(aluno.msgs*100 / int(msgCount), 2) ) + "%, " + str(aluno.chars) + " caracteres)"  + "\n")

    f2.write("\nParticipação por caracteres: \n")        
    for aluno in PartChars:
        f2.write(aluno.nome + " (" + str(aluno.msgs) + " mensagens, " + str(aluno.chars) + " caracteres)" + "\n" )

subprocess.Popen("notepad " + saida)  # abre bloco de notas no Windows
