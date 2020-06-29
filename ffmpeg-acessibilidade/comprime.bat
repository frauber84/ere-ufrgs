@ECHO OFF
IF EXIST %1 GOTO PROCESSAR

ECHO Arraste algum arquivo para ser convertido!
ECHO[
PAUSE
GOTO FINAL

:PROCESSAR
ECHO ..........................................................
ECHO     Comprime v¡deos com ffmpeg sem perda de resolu‡Æo       
ECHO         https://github.com/frauber84/ere-ufrgs/
ECHO ..........................................................
ECHO[
ECHO Guia para bitrates (valores menores = mais compressÆo, menor tamanho do arquivo e qualidade)
ECHO[
ECHO CompressÆo extrema = 128 (WhatsApp / 3G)
ECHO CompressÆo alta = 256 (WhatsApp / 3G)
ECHO CompressÆo m‚dia = 384 (qualidade m‚dia)
ECHO CompressÆo baixa = 512 (qualidade alta)
ECHO[
ECHO OBS:
ECHO 1) NÆo comprima v¡deos ao enviar para YouTube, envie na qualidade original.
ECHO 2) O menor bitrate poss¡vel depende da resolu‡Æo original. Quanto menor a resolu‡Æo,
ECHO    maior a possibilidade de bitrates menores. Experimente at‚ descobrir o valor adequado
ECHO    para seus v¡deos. Sugere-se come‡ar com o valor 128 para avaliar os resultados.
ECHO[ 
set /p BITRATE=Digite o bitrate desejado e pressione ENTER:
ECHO[ 
ffmpeg -loglevel warning -stats -i %1 -c:v libx264 -ab 80k -b:v %BITRATE%k  -tune stillimage -preset veryfast %1_%BITRATE%k.mp4

REM Acrescentar para converter em 720p quando maior que 720p:
REM -vf scale='if(gte(ih\,720)\,720\,iw)':-2

:FINAL
