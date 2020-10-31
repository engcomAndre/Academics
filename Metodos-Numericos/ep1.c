#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <locale.h>

typedef struct{
    int tam;
    double **matriz;
} MatrizSL;

/*
*   @brief  aloca dinamicamente uma matriz l x c.
*   @params l, quantidade de linhas. E c, quantidade de colunas.
*   @return um ponteiro para a matriz. Ou entao, NULL.
*/
double **alocaMatriz(int l, int c){
    int i, j;
    double **m;
    m = malloc(sizeof(double *) * l);
    if (m == NULL)
        return NULL;
    for (i = 0; i < l; i++){
        m[i] = malloc(sizeof(double) * c);
        if (m[i] == NULL){
            for (j = 0; j < i; j++)
                free(m[j]);
            free(m);
            return NULL;
        }
    }
    return m;
}

/*
*   @brief  aloca memoria dinamicamente para um vetor de tamanho c.
*   @params c, quantidade de elementos para o vetor.
*   @return um ponteiro para o vetor. Ou entao, NULL.
*/
double *alocaVetor(int c){
    double *m;
    m = malloc(sizeof(double) * c);
    if (m == NULL)
        return NULL;
    return m;
}

/*
*   @brief  liberar a memoria que foi alocada para as funcionalidades.
*   @params m, ponteiro para uma matriz. E v, quantidade de linhas em m.
*/
void liberaMatriz(double **m, int v){
    int i;
    for (i = 0; i < v; i++)
        free(m[i]);
    free(m);
}

/*
*   @brief  recebe por input(teclado) os coeficientes de uma equacao.
*   @params m, ponteiro para uma matriz, l, quantidade de linhas da
*            matriz. E c, quantidade de colunas da matriz.
*/
void leMatrizLagrange(double **m, int l, int c){
    int i = 0, j;
    do {
        printf("Informe A%d : ", c - i - 1);
        scanf(" %lf", &m[0][0]);
        if (m[0][0] <= 0)
            printf("Lembrar: Termo A%d obrigatoriamente positivo e nao-nulo.\n", c - i - 1);
    } while (m[0][0] <= 0);

    for (i = 1; i < c - 1; i++){
        printf("Informe A%d: ", c - i - 1);
        scanf(" %lf", &m[0][i]);
    }

    do {
        printf("Informe A%d : ", 0);
        scanf(" %lf", &m[0][c - 1]);
        if (m[0][c - 1] == 0)
            printf("Lembrar: A0 obrigatoriamente diferente de 0.\n");
    } while (m[0][c - 1] == 0);

    m[0][c] = 0;
    m[0][c + 1] = 0;

    for (i = 1; i < 4; i++){
        for (j = 0; j < (c + 2); j++){
            m[i][j] = 0;
        }
    }
}
/*
*   @brief  ler um arquivo e salva os valores dados numa matriz de coeficientes.
*   @return um ponteiro do tipo MatrizSL.
*/
MatrizSL *lerArquivo(){
    int n, i, j;
    double **matrix;
    char nomeArquivo[20];
    FILE *fp;

    printf("Digite o nome do arquivo: ");
    scanf(" %s", nomeArquivo);
    fp = fopen(nomeArquivo, "r");

    if (fp == NULL){
        printf("O arquivo nao existe.\n");
        return NULL;
    }

    fscanf(fp, " %d", &n);
    matrix = alocaMatriz(n, n + 1);

    for (i = 0; i < n; i++){
        for (j = 0; j < n + 1; j++){
            fscanf(fp, " %lf", &matrix[i][j]);
        }
    }
    fclose(fp);
    MatrizSL *mSL = (MatrizSL *)malloc(sizeof(MatrizSL));

    if (mSL == NULL){
        liberaMatriz(matrix, n);
        return NULL;
    }
    mSL->matriz = matrix;
    mSL->tam = n;

    return mSL;
}

/*
*   @brief  método de Newton para calcular uma raiz aproximada de uma equacao polinomial.
*   @params vcoef, vetor de coeficientes da equacao, g, grau da equacao. E limites, vetor
*           com os valores dos limites fornecidos pelo método de Lagrange.
*/
void metodoDeNewton(double *vcoef, int g, double *limites){
    int grau = g, i, count = 0;
    long double aux, aux_linha, xi, xiprox;
    xi = limites[0];

    while (count < 10000){
        aux = 0;
        aux_linha = 0;

        if (count != 0)
            xi = xiprox;

        for (i = 0; i < grau; i++){
            aux += vcoef[i] * pow(xi, grau - i);
            aux_linha += (grau - i) * vcoef[i] * pow(xi, grau - (1 + i));
        }
        xiprox = xi - (aux / aux_linha);

        if (fabsl(xi - xiprox) < 0.00000001){
            printf("Raiz aproximada: %Lf\t", xi);
            printf("Iteracoes realizadas: %d\n", count);
            return;
        }
        count += 1;
    }
    printf("Raiz aproximada: %Lf\t", xi);
    printf("Iteracoes realizadas: %d\n", count);
    free(limites);
}

/*
*   @brief  ler um input e faz a validacao quanto ao grau da equacao.
*   @return grauEq, o grau da equacao a ser trabalhada.
*/
int perguntaGrauEquacao(){
    int grauEq;
    do {
        printf("Informe grau da equação: ");
        scanf(" %d", &grauEq);
        printf("\n");
    } while (grauEq < 0);
    return grauEq;
}

/*
*   @brief  método de Lagrange para calcular os limites superiores e inferiores.
*           Logo em seguida, calcula uma aproximacao para a raiz utilizando o 
*           método de Newton.
*/
void metodoDeLagrange(){
    int i, j;
    int mTam = perguntaGrauEquacao() + 1;
    double **ml = alocaMatriz(4, mTam + 2);
    double *limites = alocaVetor(4);

    leMatrizLagrange(ml, 1, mTam);
    // formando p1, p2, p3 e p4
    for (i = 0; i < mTam; i++){
        ml[1][mTam - 1 - i] = ml[0][i];
        ml[2][i] = (mTam - 1 - i) % 2 == 0 ? ml[0][i] : -1 * ml[0][i];
        ml[3][mTam - 1 - i] = i % 2 == 0 ? ml[0][i] : -1 * ml[0][i];
    }

    //calculando o k e b respectivamente
    for (j = 0; j < 4; j++){
        for (i = 0; i < mTam; i++){
            ml[j][mTam] = ((ml[j][i] < 0) && ((mTam - i - 1) > ml[j][mTam])) ? (mTam - i - 1) : ml[j][mTam];
            ml[j][mTam + 1] = (ml[j][i] < ml[j][mTam + 1]) ? ml[j][i] : ml[j][mTam + 1];
        }
        ml[j][mTam + 1] = fabs(ml[j][mTam + 1]);
    }
    //calculando os limites
    for (i = 0; i < 4; i++){
        limites[i] = (1.0 + pow(ml[i][mTam + 1] / ml[i][0], 1.0 / (mTam - 1 - ml[i][mTam]))) * (i < 2 ? 1 : -1);
    }
    limites[1] = 1.0 / limites[1];
    limites[3] = 1.0 / limites[3];

    printf("Os limites para a equacao sao:\n");
    printf("Superior: %.4f  <= x <=  %.4f\n", limites[1], limites[0]);
    printf("Inferior: %.4f <= x <= %.4f\n", limites[2], limites[3]);

    metodoDeNewton(ml[0], mTam, limites);
    liberaMatriz(ml, 4);
}
/*
*   @brief  checagem através dos critérios das linhas e das colunas.
*   @params m, ponteiro para uma matriz de double.
*   @return 1, se for bem condicionada. E -1, caso nao.
*/
int checarCriterioDasLinhasEColunas(double **m){
    int nVariaveis = 3, i, j;
    double pivo, somaLinha, somaColuna;

    for (i = 0; i < nVariaveis; i++){
        somaLinha = 0.0;
        somaColuna = 0.0;
        pivo = fabs(m[i][i]);

        for (j = 0; j < nVariaveis; j++){
            if (i != j){
                somaLinha = somaLinha + fabs(m[i][j]);
                somaColuna = somaColuna + fabs(m[j][i]);
            }
            if (somaLinha > pivo || somaColuna > pivo)
                return -1;
        }
    }
    return 1;
}
/*
*   @brief  metodo de Gauss-Seidel para aproximaçao de uma raiz da equacao.
*/
void metodoDeGaussSeidel(){
    MatrizSL *mSL = lerArquivo();

    if (mSL == NULL){
        return;
    }
    double **m = mSL->matriz;

    if (checarCriterioDasLinhasEColunas(m) == -1){
        printf("\nMatriz não satisfaz criterio das linhas e colunas\n");
        return;
    }
    //verificar condicionamento
    double divisor, valorLinha;
    int i, j, h = 0;
    int nVariaveis = mSL->tam;
    double valores[nVariaveis];
    double valoresAnteriores[nVariaveis];

    for (i = 0; i < nVariaveis; i++){
        valores[i] = 0.0;
        valoresAnteriores[i] = 0.0;
    }

    int difMinimaAlcancada = 0;
    while (h < 1000 && difMinimaAlcancada == 0){
        for (i = 0; i < nVariaveis; i++){
            valorLinha = 0.0;
            divisor = m[i][i];
            for (j = 0; j < nVariaveis; j++){
                if (i != j){
                    valorLinha = valorLinha - (valores[j] * m[i][j]);
                }
            }
            valores[i] = (valorLinha + m[i][nVariaveis]) / divisor;
        }
        
        difMinimaAlcancada = 1;

        for (i = 0; i < nVariaveis; i++){
            difMinimaAlcancada = (fabs(valoresAnteriores[i] - valores[i]) < 0.00000001) && (difMinimaAlcancada == 1) ? 1 : 0;
            valoresAnteriores[i] = valores[i];
        }
        h++;
    }

    printf("Numero de iteracoes: %d\n", h);
    printf("Solucao encontrada:\n");
    for (i = 0; i < nVariaveis; i++)
        printf("x%d: %f\n", i + 1, valores[i]);

    printf("\n");
    liberaMatriz(mSL->matriz, mSL->tam);
}

/*
*   @brief  método auxiliar para checar os valores quando for imprimir
*           na base hexxadecimal.
*   @params value, valor a ser verificado. Se for entre 10 - 15,imprime
*           a respectiva letra, caso nao, imprime o proprio value.*/
void checkValue(int value){
    switch (value){
    case 10:
        printf("A");
        break;
    case 11:
        printf("B");
        break;
    case 12:
        printf("C");
        break;
    case 13:
        printf("D");
        break;
    case 14:
        printf("E");
        break;
    case 15:
        printf("F");
        break;
    default:
        printf("%d", value);
        break;
    }
}

/*
*   @brief  método que converte de decimal para binário
*   @params i, valor da parte inteira do decimal.
*           f, valor da parte fracionária do decimal.
*/
void convertBin(int i, double f)
{
    int j;
    int res_int[10], index_int = 0, index_frac = 0;
    double f_aux = f, res_fra[20];

    while (i >= 2)
    {
        res_int[index_int] = i % 2;
        i = (i - i % 2) / 2;
        index_int++;
    }
    res_int[index_int] = i;

    while (f_aux > 0 && index_frac < 20)
    {
        double k;
        f_aux = modf(f_aux * 2, &k);
        res_fra[index_frac] = k;
        index_frac++;
    }
    // Imprimindo valores convertidos
    printf("Binário: ");
    for (j = index_int; j >= 0; j--)
        printf("%d", res_int[j]);
    if (f > 0)
    {
        printf(".");
        for (j = 0; j < index_frac; j++)
            printf("%d", (int)res_fra[j]);
    }
    printf("\n");
}

/*
*   @brief  método que converte de decimal para hexadecimal.
*   @params i, valor da parte inteira do decimal.
*           f, valor da parte fracionária do decimal.
*/
void convertHex(int i, double f){
    int j;
    int res_int[10], index_int = 0, index_frac = 0;
    double f_aux = f, res_fra[20];

    while (i >= 16){
        res_int[index_int] = i % 16;
        i = (i - i % 16) / 16;
        index_int++;
    }
    res_int[index_int] = i;

    while (f_aux > 0 && index_frac < 20){
        double k;
        f_aux = modf(f_aux * 16, &k);
        res_fra[index_frac] = k;
        index_frac++;
    }
    // Imprimindo valores convertidos
    printf("Hexadecimal: ");
    for (j = index_int; j >= 0; j--)
        checkValue(res_int[j]);
    if (f > 0){
        printf(".");
        for (j = 0; j < index_frac; j++)
            checkValue((int)res_fra[j]);
    }
    printf("\n");
}

/*
*   @brief  método que converte de decimal para octadecimal.
*   @params i, valor da parte inteira do decimal.
*           f, valor da parte fracionária do decimal.
*/
void convertOct(int i, double f){
    int j;
    int res_int[10], index_int = 0, index_frac = 0;
    double f_aux = f, res_fra[20];

    while (i >= 8){
        res_int[index_int] = i % 8;
        i = (i - i % 8) / 8;
        index_int++;
    }
    res_int[index_int] = i;

    while (f_aux > 0 && index_frac < 20){
        double k;
        f_aux = modf(f_aux * 8, &k);
        res_fra[index_frac] = k;
        index_frac++;
    }
    // Imprimindo valores convertidos
    printf("Octadecimal: ");
    for (j = index_int; j >= 0; j--)
        printf("%d", res_int[j]);
    if (f > 0){
        printf(".");
        for (j = 0; j < index_frac; j++)
            printf("%d", (int)res_fra[j]);
    }
    printf("\n");
}

int main(int argc, char *argv[]){
    setlocale(LC_ALL, "");

    char input;
    do {
        printf("C - Conversão \n");
        printf("S - Sistema Linear \n");
        printf("E - Equação Algébrica \n");
        printf("F - Finalizar \n");
        scanf(" %c", &input);
        double value, intpart, fracpart;
        switch (input){
        case 'c':
        case 'C':
            printf("Digite o número a ser convertido: ");
            scanf(" %lf", &value);
            fracpart = modf(value, &intpart);
            convertBin(intpart, fracpart);
            convertOct(intpart, fracpart);
            convertHex(intpart, fracpart);
            printf("\n");
            break;
        case 's':
        case 'S':
            metodoDeGaussSeidel();
            break;
        case 'e':
        case 'E':
            metodoDeLagrange();
            break;
        case 'f':
        case 'F':
            printf("Finalizando a aplicação...\n");
            return 0;
        default:
            printf("Comando inválido!\n");
            break;
        }
    } while (1);
}
