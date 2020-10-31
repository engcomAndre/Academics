<h2>SISTEMAS OPERACIONAIS – 2017.2</h2>
Prof. Fernando Parente Garcia
<h4>Projeto II – Algoritmos de escalonamento de braço do disco</h4><br>
<b>Objetivo:</b><br>
  Simular os algoritmos de escalonamento de braço do disco FIFO, SSF, SCAN e SCAN Circular (C-SCAN).<br>
<b>Entradas do Sistema:</b><br>
   Quantidade de cilindros do disco.<br>
  Posição inicial do braço do disco (número do cilindro em que o braço se encontra).<br>
  Tempo de seek para o cilindro adjacente (ms).<br>
  Nome do arquivo que contém as requisições de acesso a disco no formato abaixo:<br>
           <b>12-9-43-32-50-43-40-20-36-8-34-3-44-12-32-10-8-18-43-11-<br>
  
  <b>Saídas:
  <br>  
    
  Para cada um dos quatro algoritmos simulados, o programa deverá fornecer as seguintes saídas:<br>
   Quantidade de deslocamentos necessária para atender todas as requisições;<br>
   Quantidade média de deslocamentos;<br>
   Variância e desvio padrão da quantidade de deslocamento;<br>
   Tempo médio de deslocamentos.<br>
   Variância e desvio padrão do tempo de deslocamento.<br>
   Arquivo (mesmo formato do arquivo de entrada) contendo a ordem em que as requisições foram atendidas.<br>
<b>Análise dos resultados:<br>
  A equipe deverá entregar um relatório com uma análise comparativa entres os quatro algoritmos simulados. Este relatório deverá identificar e justificar os pontos fracos de cada algoritmo, como também identificar e justificar qual o melhor algoritmo no caso médio.
