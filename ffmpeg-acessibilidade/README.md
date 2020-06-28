# ffmpeg-acessibilidade

Presets para compressão de vídeo com foco em **acessibilidade digital** utilizando a biblioteca ffmpeg (https://ffmpeg.zeranoe.com/builds/). 
Soluções adaptativas empregadas por sites como o YouTube não são adequadas para o **ensino remoto**, pois resultam em perda de resolução e textos pixelados, além do *overhead* da própria plataforma (vídeos relacionados, propagandas, etc. Com estes *presets*, buscou-se otimizar a compressão para o contexto de **vídeo-aulas expositivas** (webcam + slides).

Vídeos de até 10 minutos com bitrates entre 128k e 256k podem possivelmente ser **distribuídos WhatsApp**, cujo tráfego de dados é liberado por algumas teleoperadores mesmos nos planos mais básicos.

OBS: é provável que os primeiros dez segundos do vídeo fiquem com um resultado inferior ao restante. 

## **Utilização**

Arraste o arquivo de vídeo para um dos arquivos *batch*:

*comprime.bat*: Comprime o vídeo a partir do bitrate do escolhido. 

*comprime_todos.bat*: Comprime todos vídeos do diretório com a extensão indicada


## Sugestões para melhores resultados

- Utilizar slides com a mesma cor de fundo

- Reduzir o espaço dedicado a *webcam*, ou gravar somente texto em cima do slide

- Capturar uma janela/pedaço da tela em vez da tela inteira

- 

## **Parâmetros de compressão**

Os seguintes parâmetros são utilizados na conversão.

- *Bitrate do áudio*: 80kbits/s (" -ab 80k "). Para vídeos com música, sugere-se alterar o parâmetro para 96k (" -ab 96k "). Para vídeos com somente fala, é possível reduzir ainda mais o tamanho do arquivo utilizando 64kbits/s (" -ab 64k ").

- *Tune*: Otimizado para vídeos com imagens estáticas (" -tune stillimage" ). Para melhores resultados, utilize slides com fundos com a mesma cor.

- *Preset*: Otimiza para velocidade de compressão ("-preset veryfast"). 

- *Resolução*: A resolução de origem é mantida. É possível forçar decrescimo de resolução para 720p em casos de vídeos acima desta resolução com o parâmetro  " -vf scale='if(gte(ih\,720)\,720\,iw)':-2 ", porém os resultados testados não foram satisfatórios.

- *Codec*: H.264 (" -c:v libx264 ")
