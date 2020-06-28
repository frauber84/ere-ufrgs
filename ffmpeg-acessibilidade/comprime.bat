@ECHO OFF
IF EXIST %1 GOTO PROCESSAR

ECHO Arraste algum arquivo para ser convertido!
ECHO[
PAUSE
GOTO FINAL

:PROCESSAR
ECHO ..........................................................
ECHO     Comprime v°deos com ffmpeg sem perda de resoluá∆o       
ECHO         https://github.com/frauber84/ere-ufrgs/
ECHO ..........................................................
ECHO[
ECHO Guia para bitrates (valores menores = mais compress∆o, menor tamanho do arquivo e qualidade)
ECHO[
ECHO Compress∆o extrema = 128 (WhatsApp / 3G)
ECHO Compress∆o alta = 256 (WhatsApp / 3G)
ECHO Compress∆o mÇdia = 384 (qualidade mÇdia)
ECHO Compress∆o baixa = 512 (qualidade alta)
ECHO[
ECHO OBS:
ECHO 1) N∆o comprima v°deos ao enviar para YouTube, envie na qualidade original.
ECHO 2) O menor bitrate poss°vel depende da resoluá∆o original. Quanto menor a resoluá∆o,
ECHO    maior a possibilidade de bitrates menores. Experimente atÇ descobrir o valor adequado
ECHO    para seus v°deos. Sugere-se comeáar com o valor 256 para avaliar os resultados.
ECHO[ 
set /p BITRATE=Digite o bitrate desejado e pressione ENTER:
ECHO[ 
ffmpeg -loglevel warning -stats -i %1 -c:v libx264 -ab 80k -b:v %BITRATE%k  -tune stillimage -preset veryfast %1_%BITRATE%k.mp4

REM Acrescentar para converter em 720p quando maior que 720p:
REM -vf scale='if(gte(ih\,720)\,720\,iw)':-2

:FINAL