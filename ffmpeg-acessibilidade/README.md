# ffmpeg-acessibilidade

Presets para compressão de vídeo com foco em acessibilidade digital utilizando a biblioteca ffmpeg (build **Static** em https://ffmpeg.zeranoe.com/builds/). 

**Utilização**: Arraste o arquivo de vídeo para um dos arquivos *batch*:
*comprime.bat*: Comprime o vídeo a partir do bitrate do escolhido. 
*comprime_toods.bat*: Comprime todos vídeos do diretório com a extensão indicada

OBS: a compressão do áudio está pré-definidap para 96kbits/s. É possível obter compressões ainda maiores trocando o parametro **-ab 96k** por **-ab 64k** nos arquivos .bat
