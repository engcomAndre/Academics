#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <locale.h>//Biblioteca responsável por configuração de outputs locais
//Definição de Constantes
#define MAXPOSITIONS 256
//define a max lenght of matriz
//Fim da Definição de Constantes

/*Struct que Representa a Imagem*/
struct Image{	
	char Format[MAXPOSITIONS];//Formato da Imagem    
	char Coment[MAXPOSITIONS];//Comentário Presente 
	int Max_Value;//Maior Valor de Intensidade de Pixel da Imagem    

    int Line_Lenght;//Tamanho da Linha da Matriz de Pixel da Imagem
    int Colunm_Lenght;//Tamanho da Coluna da Matriz de Pixel da Imagem

    int** Matriz; //Ponteiro do endereço para a Matriz de pixels da imagem

} typedef Image;//Definição de Novo Tipo Image


/*Struct que Representa os Histogramas*/
struct strHistogram
{
    int Line_Lenght;//Tamanho do histograma da Imagem
    int Histogram[MAXPOSITIONS];//Histograma da quantidade de intensidade dos pixels da imagem
    float EqualizedHistogram[MAXPOSITIONS];//Histograma equalizado da quantidade de intensidade dos pixels da imagem
    float PDFHistogram[MAXPOSITIONS];//Histograma da função de probabilidade de densidade dos pixels da imagem
    float AcumulatedHistogram[MAXPOSITIONS];//Histograma da acumulado da função de probabilidade de densidade dos pixels da imagem
} typedef strHistogram;//Definição de Novo Tipo Histograma



/*Função  : Alocar Memória para uma matriz
  Entrada : Tipo Imagem
  Retorno : tipo Imagem com matriz alocada
  Saída   : NADA
*/
Image alocateMemory(Image image)//Código auto-explicativo
{
	int index;
    image.Matriz = (int**) malloc(image.Line_Lenght * sizeof(int));//alocação de memória para linhas da matriz 
    
    for (index = 0; index < image.Line_Lenght; index++)//alocação de memória para cada coluna da matriz 
    {
        image.Matriz[index] = (int*) malloc(image.Colunm_Lenght * sizeof(int));
    }
    return image;
}

/*Função  : Imprimir uma imagem com seus atributos
  Entrada : Tipo Imagem
  Retorno : NADA
  Saída   : Texto na saída padrão 
*/
void ShowMatriz(Image image)//Código auto-explicativo
{
    int line,colunm;
    printf("PGM Format : %s\n",image.Format);
    printf("PGM Colum Size : %d\n",image.Colunm_Lenght);
    printf("PGM Line Size : %d\n",image.Line_Lenght);
    printf("PGM Max Value : %d\n",image.Max_Value);
    printf("PGM Coment : %s\n",image.Coment);
    for(line = 0; line < image.Line_Lenght; line++)
    {
        for(colunm = 0; colunm < image.Colunm_Lenght; colunm++)
        {
            printf("%4d",image.Matriz[line][colunm]);
        }
        printf("\n");
    }
}

/*Função: Imprimir uma strutura completa de histogramas 
Entrada : Tipo strHistogram
Retorno : NADA
Saída   : Texto na saída padrão
*/
void ShowHistogramData(strHistogram Histogram)
{
    int index;
	//Inicio Formatação de Saída
    printf("   PIX  ");
    printf("  Hist ");
    printf("    PDF  ");
    printf("    Accu ");
    printf("   Eqlz");
    printf("\r\n");
	//Fim Formatação de Saída
    for(index = 0; index < Histogram.Line_Lenght; index++)//Impressão de Cada Posiçao dos Histogramas da Estrutura
    {
        printf("%6d",index);
        printf("  %6d",Histogram.Histogram[index]);
        printf("  %f",Histogram.PDFHistogram[index]);
        printf("  %f",Histogram.AcumulatedHistogram[index]);
        printf("  %f",Histogram.EqualizedHistogram[index]);
        printf("\n");
    }
    printf("\n");
}

/*Função: Inicializar uma strutura completa de histogramas
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram inicializado
Saída   : NADA
*/
strHistogram InitHistogram(strHistogram Histogram)//Código auto-explicativo
{
    int index;
    Histogram.Line_Lenght = MAXPOSITIONS;
    for(index = 0; index < Histogram.Line_Lenght; index++)//Zera cada posiçao dos Histogramas da Estrutura
    {
        Histogram.Histogram[index] = 0;
        Histogram.PDFHistogram[index] = 0;
        Histogram.AcumulatedHistogram[index] = 0;
        Histogram.EqualizedHistogram[index] = 0;
    }
    Histogram.AcumulatedHistogram[-1] = 0;//Corrigir Possível erro no Cálculo do acumulado
    return Histogram;
}

/*Função: Calcula o Histograma de Intensidades,cada posição do histograma representa uma
intensidade de pixel da imagem que é incrementada cada vez que é encontrada na matriz de 
intensidades da imagem.
Entrada : Tipo Image,Tipo strHistogram
Retorno : Tipo strHistogram com Histogram de Intensidades calculado
Saída   : NADA
*/
strHistogram CalcHistogram(Image image,strHistogram Histogram)
{
    int line,colunm;
    for(line = 0; line < image.Line_Lenght; line++)
    {
        for(colunm = 0; colunm < image.Colunm_Lenght; colunm++)
        {													   
            Histogram.Histogram[image.Matriz[line][colunm]]++;         
        }
    }
    return Histogram;
}

/*Função: Calcula o Função de Probabilidade de Densidade da Imagem,cada posição do histograma de intensidades 
é normalizado,dividido pelo pelo produto das dimensões da matriz de pixels da imagem.
Entrada : Tipo Image,Tipo strHistogram
Retorno : Tipo strHistogram com PDFHistogram calculado
Saída   : NADA
*/
strHistogram CalcPDFHistogram(Image image,strHistogram Histogram)
{
    int index;
    for(index = 0; index < Histogram.Line_Lenght; index++)
    {
        Histogram.PDFHistogram[index] = (float)(Histogram.Histogram[index])/(image.Colunm_Lenght * image.Line_Lenght);
    }
    return Histogram;
}

/*Função: Calcula o Acmulado da Função de Probabilidade de Densidade da Imagem,cada posição
é a soma do PDFHistogram na Posição atual mais a soma de todos os valores das posições anteriores 
do accumulatedhistogram.
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram com accumulatedHistogram calculado
Saída   : NADA
*/
strHistogram CalcAccumulatedHistogram(strHistogram Histogram)
{
    int index;
    for(index = 0; index < Histogram.Line_Lenght; index++)
    {
        Histogram.AcumulatedHistogram[index] = Histogram.PDFHistogram[index] + Histogram.AcumulatedHistogram[index - 1];
    }
    return Histogram;
}

/*Função: Calcula o Histograma Equalizado,cada posição do vetor é o produto do accumulatedhistogram 
na posição atual pela resolução da camada da imagem.
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram com equalizedHistogram calculado
Saída   : NADA
*/
strHistogram CalcEqualizeHistogram(strHistogram Histogram)
{
    int index;
    for(index = 0; index < Histogram.Line_Lenght; index++)
    {
        Histogram.EqualizedHistogram[index] = MAXPOSITIONS * Histogram.AcumulatedHistogram[index];
    }
    return Histogram;
}

/*Função: Equaliza a Imagem,aplica os valores do equalizedHistogram na imagem para gerar constraste,cada valor
de intensidade de pixel da imagem representa uma posição do vetor equalizado cujo valor é sustituído pelo 
valor corrente na posição do equalizedHistogram.
Entrada : Tipo Image,Tipo strHistogram.
Retorno : Tipo Image com matriz de pixels equalizada.
Saída   : NADA.
*/
Image EqualizeImage(Image image,strHistogram Histogram)
{
    int line,colunm;    
    for(line = 0; line < image.Line_Lenght; line++)
    {
        for(colunm = 0; colunm < image.Colunm_Lenght; colunm++)
        {
            image.Matriz[line][colunm] = Histogram.EqualizedHistogram[image.Matriz[line][colunm]];
        }
    }
    return image;
}

/*Função: Salva Imagem
Entrada : Tipo Image,Tipo String Nome do arquivo de Saída.
Retorno : NADA.
Saída   : Arquivo no Diretório com Nome e formato Especificado no nome do Arquivo.
*/
void saveImg(Image image,char* fileNameOutput)
{
    int line,colunm;
    FILE *arq;    //ponteiro para arquivo de saída
    arq = fopen(fileNameOutput,"w");//gera arquivo em modo escrita

	//Inicio Inserçao Cabeçalho Imagem
    fprintf(arq,"%s\n",image.Format);
    fprintf(arq,"%d %d\n",image.Colunm_Lenght,image.Line_Lenght) ; 
    fprintf(arq,"%d\n",image.Max_Value);
	//Fim Inserçao Cabeçalho Imagem

	//Inicio Inserçao matriz da Imagem
    for(line=0; line < image.Line_Lenght; line++)
    {
        for(colunm=0; colunm < image.Colunm_Lenght; colunm++)
        {
            fprintf(arq, "%3d ", image.Matriz[line][colunm]);
        }
        fprintf(arq, "\n");
    }
	//Fim Inserçao matriz da Imagem
    fclose(arq);//fechamento de arquivo
}

/*Função: Carregar Imagem
Entrada : Tipo Image,Tipo String Nome do arquivo de Saída.
Retorno : Tipo Imagem com dados da imagem obtidas no arquivo lido.
Saída   : (ERROR)String informação sobre erro.
*/
Image loadImg(Image image,char * fileNameInput)
{
    FILE *arq;//ponteiro para arquivo
    arq = fopen(fileNameInput, "r") ;//abri arquivo em modo leitura

    if (arq == NULL)//verifica a validade da abertuda de arquivo encerra programa em caso de erro.
    {
        printf("Open file error...error = 1\n") ;
		exit(1);//aborto de programa em caso de erro.
    }
    /* Lê dados do cabeçalho da imagem de entrada */
    Image img;//tipo imagem temporário
    fscanf(arq,"%s\n",&img.Format);
    strcpy(image.Format,img.Format);
    if (!strstr(image.Format,"P2") && !strstr(image.Format,"P5"))//verifica validade pelo cabeçalho do arquivo
    {
        printf("Image is not PGM valid file...error = 2\n") ;
        fclose(arq) ;
        exit(2);//aborto em caso de tipo arquivo inválido
    }
	//leitura de comentário da imagem se houver
    do
    {
        fgets((char*)img.Coment, 100,arq);
    }
    while (strchr ((char*)img.Coment, '#'));
	//fim leitura de comentário da imagem se houver

    sscanf ((char*)img.Coment, "%d %d", &img.Colunm_Lenght, &img.Line_Lenght);//leitura das dimensões da matriz de pixels
    fscanf(arq,"%d",&img.Max_Value);//leitura das do maior valor presente da matriz de pixels.

	//passagem de dados para parametro de entrada
    image.Colunm_Lenght = img.Colunm_Lenght;
    image.Line_Lenght = img.Line_Lenght;
    image.Max_Value = img.Max_Value;
	//fim passagem de dados para parametro de entrada

    if (image.Colunm_Lenght == 0 || image.Line_Lenght == 0 || image.Max_Value == 0)//validação dos atributos carregados
    {
        printf ("File Dimensions Error...erro = 3<%s>\n\n",fileNameInput);
        exit(3);
    }

    image = alocateMemory(image);//alocação de memória para a matriz de pixels
    
	//Leitura as intensidades dos pixels da imagem de entrada e armazena na matrix da Imagem 
    int line,colunm;
    for(line=0; line < image.Line_Lenght; line++)
    {
        for(colunm=0; colunm < image.Colunm_Lenght; colunm++)
        {
            fscanf(arq, "%d ", &image.Matriz[line][colunm]);
        }
    }
	//Fim Leitura as intensidades dos pixels da imagem de entrada e armazena na matrix da Imagem 

    fclose(arq);//fechamento de arquivo
    return image;
}

/*Função: Salva Histogram de intensidades por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Saída   : Arquivo no Diretório com Nome:"Calculated Histogram.txt".
*/
void SaveHistogram(strHistogram Histogram)
{
    FILE *arq;//ponteiro para arquivo
    arq = fopen("Calculated Histogram.txt","w");//abertura de arquivo em modo escrita
    int i;
	//inicio escrita de valores
    for(i = 0; i < Histogram.Line_Lenght; i++)
    {
        fprintf(arq,"%d",Histogram.Histogram[i]);
    }
	//fim escrita de valores
    fclose(arq);//fechamento de arquivo	
}

/*Função: Salva PDFHistogram por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Saída   : Arquivo no Diretório com Nome:"Calculated PDF Histogram.txt".
*/
void SavePDFHistogram(strHistogram HistogramData)
{
    FILE *arq;//ponteiro para arquivo
    arq = fopen("Calculated PDF Histogram.txt","w");//abre arquivo em modo escrita
    int i;
	//inicio escrita de valores
    for(i = 0; i < HistogramData.Line_Lenght; i++)
    {
        fprintf(arq,"%g ",HistogramData.PDFHistogram[i]);
    }
	//fim escrita de valores
    fclose(arq);
}

/*Função: Salva accumulatedFHistogram por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Saída   : Arquivo no Diretório com Nome:"Calculated Accumulated Histogram.txt".
*/
void SaveAccumulatedHistogram(strHistogram HistogramData)
{
    FILE *arq;//ponteiro para arquivo 
    arq = fopen("Calculated Accumulated Histogram.txt","w");//abre arquivo em modo escrita

	//inicio escrita de valores
    int index;
    for(index = 0; index < HistogramData.Line_Lenght; index++)
    {
        fprintf(arq,"%g ",HistogramData.AcumulatedHistogram[index]);
    }
	//fim escrita de valores
    fclose(arq);//fechamento de arquivo
}

/*Função: Salva equalizedHistogram por varredura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Saída   : Arquivo no Diretório com Nome:"Calculated Equalized Histogram.txt".
*/
void SaveEqualizedHistogram(strHistogram HistogramData)
{
    FILE *arq;//ponteiro para arquivo
    arq = fopen("Calculated Equalized Histogram.txt","w");//abre arquivo em modo escrita

	//inicio escrita de valores
    int index;
    for(index = 0; index < HistogramData.Line_Lenght; index++)
    {
        fprintf(arq,"%g ",HistogramData.EqualizedHistogram[index]);
    }
	//fim escrita de valores
    fclose(arq);//fechamento de arquivo

}

/*Função: Salva StrHistogram.
Entrada : Tipo strhistogram.
Retorno : NADA.
Saída   : Arquivos no Diretório em formaro txt para cada histogram da strutura.
*/
void SaveHistogramData(strHistogram HistogramData)
{
    SaveHistogram(HistogramData);//Salva Histograma de intensidades
    SavePDFHistogram(HistogramData);//Salva Histograma da Funçao de Probabilidade de Densidade
    SaveAccumulatedHistogram(HistogramData);//Salva Histograma do acumulado da Funçao de Probabilidade de Densidade
    SaveEqualizedHistogram(HistogramData);//Salva Histograma Equalizado
}

/*Função: Calcula todos os Histogramas presentes em uma StrHistogram.
Entrada : Tipo Image,Tipo strhistogram.
Retorno : Tipo Histogram com todos os Histogram calculados.
Saída   : NADA.
*/
strHistogram CalcHistogramData(Image image,strHistogram Histogram)
{    
    Histogram = CalcHistogram(image,Histogram);//Calcula Histograma de Intensidades
    Histogram = CalcPDFHistogram(image,Histogram);//Calcula Histograma da Função de Probabilidade de Densidade
    Histogram = CalcAccumulatedHistogram(Histogram);//Calcula Histograma acumulado da Função de Probabilidade de Densidade
    Histogram = CalcEqualizeHistogram(Histogram);//Calcula Histograma Equalizado

    return Histogram;
}

/*Função: Chamada de Funções com Informação da Etapa Corrente.
Entrada : String Nome Arquivo de Entrada
Retorno : NADA.
Saída   : Imagem Equalizada formato(Nome_ + "Equalized.pgm"),arquivos em .txt referentes ao histograma da imagem,
e etapa corrente do processo.
*/
void MasterOperation(char* nameFileinput)
{    
	Image image; //variável tipo image

	printf("Carregando Imagem...\n");
	image = loadImg(image, nameFileinput);//carregamento da imagem
	printf("Imagem Carregada  \n\n");

	char nameFileOut[255];//declaração do arquivo de saída

	sprintf(nameFileOut, "%s__Equalized.pgm", nameFileinput);//inicialização do nome do arquivo de saída com formatação

	strHistogram HistogramData;// variável strHistogram

	printf("Inicializando Histograma...\n");
	HistogramData = InitHistogram(HistogramData);//Inicialização de Histogramas
	printf("Histograma Inicializado\n\n");

	printf("Calculando Histograma...\n");
	HistogramData = CalcHistogramData(image, HistogramData);//Calculo de todos os Histogramas
	printf("%Histograma Calculado\n\n");

	printf("Equalizando Imagem...  \n");
	image = EqualizeImage(image, HistogramData);//Equalização da imagem
	printf("Imagem Equalizada\n\n");

	printf("Salvando Imagem Equalizada...  \n");
	saveImg(image, nameFileOut);//Salvando arquivo
	printf("Imagem Equalizada Salva\n\n");

	printf("Salvando Histograma...\n");
	SaveHistogramData(HistogramData);//Salvando Histogramas
	printf("Histograma Salvo\n\n");

	printf("Programa Finalizado\n\n");
	/*Fim de Programa*/
}
/*Função: Ponto de Entrada.
Entrada : Nome do Arquivo tipo .pgm parametro ARGV[]
Retorno : Inteiro : SUCESFULL = '0', ERROR != 0 .
Saída   : Mensagens de Compilação e Execuçao do processo.
*/
int main(int argc,char *argv[])
{
    setlocale(LC_ALL,"portuguese");

	MasterOperation(argv[1]);//Entrada para Processo Principal

    return 0;
}


