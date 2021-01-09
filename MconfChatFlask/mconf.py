from flask import Flask, make_response, request
app = Flask(__name__)
app.config["DEBUG"] = True

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

def process_data(input_data):
    result = ""
    '''
    Exemplo de formato da mensagem:
    [13:52] ANA BEATRIZ MICHELS : Olá, Profes! Boa tarde para nós... :)
    '''
    ListaMsg = []
    ListaPresenca = []
    ListaAlunos = []
    mensagens = []
    msgCount = 0

    #for line in input_data.split("\n"):
    mensagens = input_data.split("\n")

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

    result += "Lista de presença (Alunos participantes no chat = " + str( len(ListaPresenca) ) + ")\n"

    for presenca in ListaPresenca:
        result += str(presenca) + "\n"

    if len(ListaPresenca) > 5:
        result += "\nTop 5 participação (mensagens):" + "\n"
        for i in range(0,5):
            result += PartMsgs[i].nome + " (" + str(PartMsgs[i].msgs) + " mensagens, " + str(PartMsgs[i].chars) + " caracteres, " + str( round(PartMsgs[i].msgs*100 / int(msgCount), 2) ) + "%)\n"

        result += "\nTop 5 participação (caracteres):" + "\n"
        for i in range(0,5):
            result += PartChars[i].nome + " (" + str(PartChars[i].msgs) + " mensagens, " + str(PartChars[i].chars) + " caracteres, " + str( round(PartChars[i].msgs*100 / int(msgCount), 2) ) + "%)\n"

    result += "\nParticipação por mensagens (total = " + str(msgCount) + ")\n"
    for aluno in PartMsgs:
        result += aluno.nome + " (" + str(aluno.msgs) + " mensagens, " + str( round(aluno.msgs*100 / int(msgCount), 2) ) + "%, " + str(aluno.chars) + " caracteres)"  + "\n"

    result += "\nParticipação por caracteres: \n"
    for aluno in PartChars:
        result += aluno.nome + " (" + str(aluno.msgs) + " mensagens, " + str(aluno.chars) + " caracteres)" + "\n"

    return result

@app.route("/", methods=["GET", "POST"])
def file_summer_page():
    if request.method == "POST":
        input_file = request.files["input_file"]
        input_data = input_file.stream.read().decode("utf-8")
        output_data = process_data(input_data)
        response = make_response(output_data)
        response.headers["Content-Disposition"] = "attachment; filename=relatório.txt"
        return response

    return '''<!DOCTYPE html><head><meta charset="UTF-8">
<link rel="apple-touch-icon" type="image/png" href="https://static.codepen.io/assets/favicon/apple-touch-icon-5ae1a0698dcc2402e9712f7d01ed509a57814f994c660df9f7a952f3060705ee.png" />
<meta name="apple-mobile-web-app-title" content="CodePen">
<link rel="shortcut icon" type="image/x-icon" href="https://static.codepen.io/assets/favicon/favicon-aec34940fbc1a6e787974dcd360f2c6b63348d4b1f4e06c77743096d55480f33.ico" />
<link rel="mask-icon" type="" href="https://static.codepen.io/assets/favicon/logo-pin-8f3771b1072e3c38bd662872f6b673a722f4b3ca2421637d5596661b4e2132cc.svg" color="#111" />
<title>MConfChat</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" type="text/javascript"></script>
<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css'>
<link rel='stylesheet' href='https://mconf.pythonanywhere.com/static/estilo.css'>
<script>
  window.console = window.console || function(t) {};
</script>
<script>
  if (document.location.search.match(/type=embed/gi)) {
    window.parent.postMessage("resize", "*");
  }
</script>
</head>
<body translate="no">
<link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css" rel="stylesheet">
<div class="container center">
<div class="row">
<div class="col-md-12">
<h1 class="white">MConf: Lista de Presença e Participação</h1>
<p class="white">
<br><b>1)</b> Salve o bate-papo clicando no local indicado (no final da sessão):<br><br><img src="http://mconf.pythonanywhere.com/static/mconf.png" style="border-radius:5px;border-color: #ff3f3f" width="448" height="112"><br><br>( <b>OBS</b>: para constar como presente, o partcipante deve ter enviado uma mensagem ao bate-papo público )</p>
</div>
</div>
<p class="white"><br><b>2)</b> Envie o arquivo gerado e clique no botão <i>Processar</i>:<br></p>
<form name="upload" method="post" action="#" enctype="multipart/form-data" accept-charset="utf-8">
<div class="row">
<div class="col-md-6 col-md-offset-3 center">
<div class="btn-container">
<h1 class="imgupload"><i class="fa fa-file-image-o"></i></h1>
<h1 class="imgupload ok"><i class="fa fa-check"></i></h1>
<h1 class="imgupload stop"><i class="fa fa-times"></i></h1>
<p id="namefile">Arquivo public-chat-etc.txt</p>
<button type="button" id="btnup" class="btn btn-primary btn-lg">Enviar Arquivo</button>
<input type="file" value="" name="input_file" id="input_file">
</div>
</div>
</div>
<div class="row">
<div class="col-md-12">
<input type="submit" value="Processar" class="btn btn-primary" id="submitbtn">
<button type="button" class="btn btn-default" disabled="disabled" id="fakebtn">Processar <i class="fa fa-minus-circle"></i></button>
</div>
</div>
</form>
<br><hr>
<p class="white">Desenvolvido por <a href="http://fernandorauber.com.br">Fernando Rauber</a> (fernando.rauber@ufrgs.br)<br></p>
</div>
<script src="https://static.codepen.io/assets/common/stopExecutionOnTimeout-157cd5b220a5c80d4ff8e0e70ac069bffd87a61252088146915e8726e5d9f147.js"></script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js'></script>
<script src="https://mconf.pythonanywhere.com/static/mconf.js" type="text/javascript" id="rendered-js"></script>
</body></html>
'''