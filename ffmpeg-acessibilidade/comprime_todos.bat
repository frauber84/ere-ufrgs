@ECHO OFF
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
set /p EXT=Digite a extensÆo dos arquivos a serem processados, sem utilizar ponto (ex: mp4):
set /p BITRATE=Digite o bitrate desejado (ex: 200):
ECHO[
FOR %%i IN (*.%EXT%) DO ffmpeg -loglevel warning -stats -i "%%i" -ab 80k -b:v %BITRATE%k -preset veryfast "%%i_%BITRATE%k.mp4"

