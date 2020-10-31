#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <locale.h>//Biblioteca respons�vel por configura��o de outputs locais
//Defini��o de Constantes
#define MAXPOSITIONS 256
//define a max lenght of matriz
//Fim da Defini��o de Constantes

/*Struct que Representa a Imagem*/
struct Image{	
	char Format[MAXPOSITIONS];//Formato da Imagem    
	char Coment[MAXPOSITIONS];//Coment�rio Presente 
	int Max_Value;//Maior Valor de Intensidade de Pixel da Imagem    

    int Line_Lenght;//Tamanho da Linha da Matriz de Pixel da Imagem
    int Colunm_Lenght;//Tamanho da Coluna da Matriz de Pixel da Imagem

    int** Matriz; //Ponteiro do endere�o para a Matriz de pixels da imagem

} typedef Image;//Defini��o de Novo Tipo Image


/*Struct que Representa os Histogramas*/
struct strHistogram
{
    int Line_Lenght;//Tamanho do histograma da Imagem
    int Histogram[MAXPOSITIONS];//Histograma da quantidade de intensidade dos pixels da imagem
    float EqualizedHistogram[MAXPOSITIONS];//Histograma equalizado da quantidade de intensidade dos pixels da imagem
    float PDFHistogram[MAXPOSITIONS];//Histograma da fun��o de probabilidade de densidade dos pixels da imagem
    float AcumulatedHistogram[MAXPOSITIONS];//Histograma da acumulado da fun��o de probabilidade de densidade dos pixels da imagem
} typedef strHistogram;//Defini��o de Novo Tipo Histograma



/*Fun��o  : Alocar Mem�ria para uma matriz
  Entrada : Tipo Imagem
  Retorno : tipo Imagem com matriz alocada
  Sa�da   : NADA
*/
Image alocateMemory(Image image)//C�digo auto-explicativo
{
	int index;
    image.Matriz = (int**) malloc(image.Line_Lenght * sizeof(int));//aloca��o de mem�ria para linhas da matriz 
    
    for (index = 0; index < image.Line_Lenght; index++)//aloca��o de mem�ria para cada coluna da matriz 
    {
        image.Matriz[index] = (int*) malloc(image.Colunm_Lenght * sizeof(int));
    }
    return image;
}

/*Fun��o  : Imprimir uma imagem com seus atributos
  Entrada : Tipo Imagem
  Retorno : NADA
  Sa�da   : Texto na sa�da padr�o 
*/
void ShowMatriz(Image image)//C�digo auto-explicativo
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

/*Fun��o: Imprimir uma strutura completa de histogramas 
Entrada : Tipo strHistogram
Retorno : NADA
Sa�da   : Texto na sa�da padr�o
*/
void ShowHistogramData(strHistogram Histogram)
{
    int index;
	//Inicio Formata��o de Sa�da
    printf("   PIX  ");
    printf("  Hist ");
    printf("    PDF  ");
    printf("    Accu ");
    printf("   Eqlz");
    printf("\r\n");
	//Fim Formata��o de Sa�da
    for(index = 0; index < Histogram.Line_Lenght; index++)//Impress�o de Cada Posi�ao dos Histogramas da Estrutura
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

/*Fun��o: Inicializar uma strutura completa de histogramas
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram inicializado
Sa�da   : NADA
*/
strHistogram InitHistogram(strHistogram Histogram)//C�digo auto-explicativo
{
    int index;
    Histogram.Line_Lenght = MAXPOSITIONS;
    for(index = 0; index < Histogram.Line_Lenght; index++)//Zera cada posi�ao dos Histogramas da Estrutura
    {
        Histogram.Histogram[index] = 0;
        Histogram.PDFHistogram[index] = 0;
        Histogram.AcumulatedHistogram[index] = 0;
        Histogram.EqualizedHistogram[index] = 0;
    }
    Histogram.AcumulatedHistogram[-1] = 0;//Corrigir Poss�vel erro no C�lculo do acumulado
    return Histogram;
}

/*Fun��o: Calcula o Histograma de Intensidades,cada posi��o do histograma representa uma
intensidade de pixel da imagem que � incrementada cada vez que � encontrada na matriz de 
intensidades da imagem.
Entrada : Tipo Image,Tipo strHistogram
Retorno : Tipo strHistogram com Histogram de Intensidades calculado
Sa�da   : NADA
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

/*Fun��o: Calcula o Fun��o de Probabilidade de Densidade da Imagem,cada posi��o do histograma de intensidades 
� normalizado,dividido pelo pelo produto das dimens�es da matriz de pixels da imagem.
Entrada : Tipo Image,Tipo strHistogram
Retorno : Tipo strHistogram com PDFHistogram calculado
Sa�da   : NADA
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

/*Fun��o: Calcula o Acmulado da Fun��o de Probabilidade de Densidade da Imagem,cada posi��o
� a soma do PDFHistogram na Posi��o atual mais a soma de todos os valores das posi��es anteriores 
do accumulatedhistogram.
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram com accumulatedHistogram calculado
Sa�da   : NADA
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

/*Fun��o: Calcula o Histograma Equalizado,cada posi��o do vetor � o produto do accumulatedhistogram 
na posi��o atual pela resolu��o da camada da imagem.
Entrada : Tipo strHistogram
Retorno : Tipo strHistogram com equalizedHistogram calculado
Sa�da   : NADA
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

/*Fun��o: Equaliza a Imagem,aplica os valores do equalizedHistogram na imagem para gerar constraste,cada valor
de intensidade de pixel da imagem representa uma posi��o do vetor equalizado cujo valor � sustitu�do pelo 
valor corrente na posi��o do equalizedHistogram.
Entrada : Tipo Image,Tipo strHistogram.
Retorno : Tipo Image com matriz de pixels equalizada.
Sa�da   : NADA.
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

/*Fun��o: Salva Imagem
Entrada : Tipo Image,Tipo String Nome do arquivo de Sa�da.
Retorno : NADA.
Sa�da   : Arquivo no Diret�rio com Nome e formato Especificado no nome do Arquivo.
*/
void saveImg(Image image,char* fileNameOutput)
{
    int line,colunm;
    FILE *arq;    //ponteiro para arquivo de sa�da
    arq = fopen(fileNameOutput,"w");//gera arquivo em modo escrita

	//Inicio Inser�ao Cabe�alho Imagem
    fprintf(arq,"%s\n",image.Format);
    fprintf(arq,"%d %d\n",image.Colunm_Lenght,image.Line_Lenght) ; 
    fprintf(arq,"%d\n",image.Max_Value);
	//Fim Inser�ao Cabe�alho Imagem

	//Inicio Inser�ao matriz da Imagem
    for(line=0; line < image.Line_Lenght; line++)
    {
        for(colunm=0; colunm < image.Colunm_Lenght; colunm++)
        {
            fprintf(arq, "%3d ", image.Matriz[line][colunm]);
        }
        fprintf(arq, "\n");
    }
	//Fim Inser�ao matriz da Imagem
    fclose(arq);//fechamento de arquivo
}

/*Fun��o: Carregar Imagem
Entrada : Tipo Image,Tipo String Nome do arquivo de Sa�da.
Retorno : Tipo Imagem com dados da imagem obtidas no arquivo lido.
Sa�da   : (ERROR)String informa��o sobre erro.
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
    /* L� dados do cabe�alho da imagem de entrada */
    Image img;//tipo imagem tempor�rio
    fscanf(arq,"%s\n",&img.Format);
    strcpy(image.Format,img.Format);
    if (!strstr(image.Format,"P2") && !strstr(image.Format,"P5"))//verifica validade pelo cabe�alho do arquivo
    {
        printf("Image is not PGM valid file...error = 2\n") ;
        fclose(arq) ;
        exit(2);//aborto em caso de tipo arquivo inv�lido
    }
	//leitura de coment�rio da imagem se houver
    do
    {
        fgets((char*)img.Coment, 100,arq);
    }
    while (strchr ((char*)img.Coment, '#'));
	//fim leitura de coment�rio da imagem se houver

    sscanf ((char*)img.Coment, "%d %d", &img.Colunm_Lenght, &img.Line_Lenght);//leitura das dimens�es da matriz de pixels
    fscanf(arq,"%d",&img.Max_Value);//leitura das do maior valor presente da matriz de pixels.

	//passagem de dados para parametro de entrada
    image.Colunm_Lenght = img.Colunm_Lenght;
    image.Line_Lenght = img.Line_Lenght;
    image.Max_Value = img.Max_Value;
	//fim passagem de dados para parametro de entrada

    if (image.Colunm_Lenght == 0 || image.Line_Lenght == 0 || image.Max_Value == 0)//valida��o dos atributos carregados
    {
        printf ("File Dimensions Error...erro = 3<%s>\n\n",fileNameInput);
        exit(3);
    }

    image = alocateMemory(image);//aloca��o de mem�ria para a matriz de pixels
    
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

/*Fun��o: Salva Histogram de intensidades por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Sa�da   : Arquivo no Diret�rio com Nome:"Calculated Histogram.txt".
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

/*Fun��o: Salva PDFHistogram por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Sa�da   : Arquivo no Diret�rio com Nome:"Calculated PDF Histogram.txt".
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

/*Fun��o: Salva accumulatedFHistogram por varreadura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Sa�da   : Arquivo no Diret�rio com Nome:"Calculated Accumulated Histogram.txt".
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

/*Fun��o: Salva equalizedHistogram por varredura de vetor.
Entrada : Tipo strhistogram.
Retorno : NADA.
Sa�da   : Arquivo no Diret�rio com Nome:"Calculated Equalized Histogram.txt".
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

/*Fun��o: Salva StrHistogram.
Entrada : Tipo strhistogram.
Retorno : NADA.
Sa�da   : Arquivos no Diret�rio em formaro txt para cada histogram da strutura.
*/
void SaveHistogramData(strHistogram HistogramData)
{
    SaveHistogram(HistogramData);//Salva Histograma de intensidades
    SavePDFHistogram(HistogramData);//Salva Histograma da Fun�ao de Probabilidade de Densidade
    SaveAccumulatedHistogram(HistogramData);//Salva Histograma do acumulado da Fun�ao de Probabilidade de Densidade
    SaveEqualizedHistogram(HistogramData);//Salva Histograma Equalizado
}

/*Fun��o: Calcula todos os Histogramas presentes em uma StrHistogram.
Entrada : Tipo Image,Tipo strhistogram.
Retorno : Tipo Histogram com todos os Histogram calculados.
Sa�da   : NADA.
*/
strHistogram CalcHistogramData(Image image,strHistogram Histogram)
{    
    Histogram = CalcHistogram(image,Histogram);//Calcula Histograma de Intensidades
    Histogram = CalcPDFHistogram(image,Histogram);//Calcula Histograma da Fun��o de Probabilidade de Densidade
    Histogram = CalcAccumulatedHistogram(Histogram);//Calcula Histograma acumulado da Fun��o de Probabilidade de Densidade
    Histogram = CalcEqualizeHistogram(Histogram);//Calcula Histograma Equalizado

    return Histogram;
}

/*Fun��o: Chamada de Fun��es com Informa��o da Etapa Corrente.
Entrada : String Nome Arquivo de Entrada
Retorno : NADA.
Sa�da   : Imagem Equalizada formato(Nome_ + "Equalized.pgm"),arquivos em .txt referentes ao histograma da imagem,
e etapa corrente do processo.
*/
void MasterOperation(char* nameFileinput)
{    
	Image image; //vari�vel tipo image

	printf("Carregando Imagem...\n");
	image = loadImg(image, nameFileinput);//carregamento da imagem
	printf("Imagem Carregada  \n\n");

	char nameFileOut[255];//declara��o do arquivo de sa�da

	sprintf(nameFileOut, "%s__Equalized.pgm", nameFileinput);//inicializa��o do nome do arquivo de sa�da com formata��o

	strHistogram HistogramData;// vari�vel strHistogram

	printf("Inicializando Histograma...\n");
	HistogramData = InitHistogram(HistogramData);//Inicializa��o de Histogramas
	printf("Histograma Inicializado\n\n");

	printf("Calculando Histograma...\n");
	HistogramData = CalcHistogramData(image, HistogramData);//Calculo de todos os Histogramas
	printf("%Histograma Calculado\n\n");

	printf("Equalizando Imagem...  \n");
	image = EqualizeImage(image, HistogramData);//Equaliza��o da imagem
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
/*Fun��o: Ponto de Entrada.
Entrada : Nome do Arquivo tipo .pgm parametro ARGV[]
Retorno : Inteiro : SUCESFULL = '0', ERROR != 0 .
Sa�da   : Mensagens de Compila��o e Execu�ao do processo.
*/
int main(int argc,char *argv[])
{
    setlocale(LC_ALL,"portuguese");

	MasterOperation(argv[1]);//Entrada para Processo Principal

    return 0;
}


