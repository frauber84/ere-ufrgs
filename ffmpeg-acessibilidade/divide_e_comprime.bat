@ECHO OFF
IF EXIST %1 GOTO PROCESSAR

ECHO Arraste algum arquivo para ser convertido!
ECHO[
PAUSE
GOTO FINAL

:PROCESSAR
ECHO ...........................................................................
ECHO     Divide em partes e comprime v¡deos com ffmpeg sem perda de resolu‡Æo       
ECHO              https://github.com/frauber84/ere-ufrgs/
ECHO ...........................................................................
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
ECHO 2) Para acessibilidade, busque o menor bitrate poss¡vel que não comprometa
ECHO    excessivamente a nitidez do video. Sugere-se come‡ar com o valor 128 para 
ECHO    avaliar os resultados.
ECHO 3) Os dez primeiros segundos do vídeo terão nitidez inferior ao restante,
ECHO    assista pontos diferentes do vídeo para avaliar o resultado.
ECHO 4) Quanto menor a resolu‡Æo, maior a possibilidade de bitrates e (tamanhos)
ECHO    menores. Os valores apresentados são um guia, é possível experimentar com
ECHO    bitrates menores ou maiores dependendo do que se busca.
ECHO[ 
set /p BITRATE=Digite o bitrate desejado e pressione ENTER:
ECHO[ 
set /p SEGMENTO=Digite o tamanho do segmento em minutos (recomendado para WhatsApp = 8):
ECHO[
ffmpeg -i %1 -c copy -map 0 -segment_time 00:%SEGMENTO%:00 -f segment -reset_timestamps 1 %1parte%%02d.mp4


IF ERRORLEVEL 0 FOR %%i IN (%1parte*) DO ffmpeg -loglevel warning -stats -i "%%i" -ab 80k -b:v %BITRATE%k -preset veryfast "%%i_%BITRATE%k.mp4" && del "%%i"

IF ERRORLEVEL 1 ffmpeg -i %1 -c:v libx264 %1.mp4 && FOR %%i IN (%1.mp4parte*) DO ffmpeg -loglevel warning -stats -i "%%i" -ab 80k -b:v %BITRATE%k -preset veryfast "%%i_%BITRATE%k.mp4" && del "%%i"

:PULAR
REM Acrescentar para converter em 720p quando maior que 720p:
REM -vf scale='if(gte(ih\,720)\,720\,iw)':-2

:FINAL
del "%1parte00.mp4"