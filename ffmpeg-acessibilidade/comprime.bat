@ECHO OFF
IF EXIST %1 GOTO PROCESSAR

ECHO Arraste algum arquivo para ser convertido!
ECHO[
PAUSE
GOTO FINAL

:PROCESSAR
ECHO ..........................................................
ECHO     Comprime v°deos com ffmpeg sem perda de resoluá∆o       
ECHO ..........................................................
ECHO[
ECHO Guia para bitrates (menores valores = mais compress∆o)
ECHO[
ECHO Compress∆o extrema = 128 (WhatsApp / 3G)
ECHO Compress∆o alta = 256 (WhatsApp / 3G)
ECHO Compress∆o mÇdia = 384 (qualidade mÇdia)
ECHO Compress∆o baixa = 512 (qualidade alta)
ECHO[
ECHO OBS:
ECHO 1) N∆o comprima v°deos ao enviar para YouTube, envie na qualidade original.
ECHO 2) O menor bitrate poss°vel depende da resoluá∆o original. Quanto menor a resoluá∆o,
ECHO    maior a possibilidade de bitrates menores. Experimente atÈ descobrir o valor adequado
ECHO    para seus v°deos. Sugiro comeáar com o valor 256.
ECHO[ 
set /p BITRATE=Digite o bitrate desejado e pressione ENTER:
ECHO[ 
ffmpeg -loglevel warning -stats -i %1 -ab 96k -b:v %BITRATE%k -preset veryfast %1_%BITRATE%k.mp4

:FINAL