@ECHO OFF
ECHO ..........................................................
ECHO     Comprime v�deos com ffmpeg sem perda de resolu��o       
ECHO ..........................................................
ECHO[
ECHO Guia para bitrates (menores valores = mais compress�o)
ECHO[
ECHO Compress�o extrema = 128 (WhatsApp / 3G)
ECHO Compress�o alta = 256 (WhatsApp / 3G)
ECHO Compress�o m�dia = 384 (qualidade m�dia)
ECHO Compress�o baixa = 512 (qualidade alta)
ECHO[
ECHO OBS:
ECHO 1) N�o comprima v�deos ao enviar para YouTube, envie na qualidade original.
ECHO 2) O menor bitrate poss�vel depende da resolu��o original. Quanto menor a resolu��o,
ECHO    maior a possibilidade de bitrates menores. Experimente at� descobrir o valor adequado
ECHO    para seus v�deos. Sugiro come�ar com o valor 256.
ECHO[ 
set /p EXT=Digite a extens�o dos arquivos a serem processados, sem utilizar ponto (ex: mp4):
set /p BITRATE=Digite o bitrate desejado (ex: 200):
ECHO[
FOR %%i IN (*.%EXT%) DO ffmpeg -loglevel warning -stats -i "%%i" -ab 96k -b:v %BITRATE%k -preset veryfast "%%i_%BITRATE%k.mp4"

