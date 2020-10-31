#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <string.h>

struct termos
{
    char ingles[41];
    char portugues[41];
};
typedef struct termos TTermo;

struct dicionario
{
    unsigned nte;
    TTermo termos[200];
};
typedef struct dicionario TDicionario;

char menu()
{
    printf("*****************************\n");
    printf("* Tradutor Ingl%cs-Portugu%cs *\n",136,136);
    printf("*****************************\n");
    printf("\n  1 - Buscar termo\n");
    printf("  2 - Introduzir novo termo\n");
    printf("  3 - Alterar termo\n");
    printf("  4 - Listar termos em ingl%cs\n",136);
    printf("  5 - Listar termos em portugu%cs\n",136);
    printf("  0 - Sair\n");
    printf("\n  Escolha uma op%c%co: ",135,198);
    return getche();
}

void mostreTermoIng(TTermo ter)
{
    printf("%-20s %s",ter.ingles,ter.portugues);
}

void mostreTermoPor(TTermo ter)
{
    printf("%-20s %s",ter.portugues,ter.ingles);
}

void mostreDicionario(TDicionario *dic, char tipo)
{
    int i;
    for(i=0; i < dic->nte; i++)
    {
        if(tipo == 'I' || tipo == 'i')
            mostreTermoIng(dic->termos[i]);
        else
            mostreTermoPor(dic->termos[i]);
        printf("\n");
    }
}

int ordIng(const void *a, const void *b)
{
    TTermo *ta = (TTermo *) a;
    TTermo *tb = (TTermo *) b;
    return strcmp(ta->ingles,tb->ingles);
}

int ordPor(const void *a, const void *b)
{
    TTermo *ta = (TTermo *) a;
    TTermo *tb = (TTermo *) b;
    return strcmp(ta->portugues,tb->portugues);
}

int buscaTermo(TDicionario *dic, TTermo ter)
{
    int i;
    for(i=0; i<dic->nte; i++)
    {
        if(strcmp(dic->termos[i].ingles, ter.ingles) == 0)
            return i;
    }
    return -1;
}

void insereTermo(TDicionario *dic, TTermo ter)
{
    dic->termos[dic->nte] = ter;
    dic->nte++;
}

int main()
{
    TDicionario dic;
    dic.nte = 0;

    FILE *fp;
    fp = fopen("dicionario.arq","rb");
    if(fp != NULL)
        fread(&dic,sizeof(TDicionario),1,fp);
    fclose(fp);
    TTermo ter;

    char op = menu();
    while(op != '0')
    {
        switch(op)
        {
            case '1' :
                printf("\n\n  ******************\n");
                printf("  * Buscar palavra *\n");
                printf("  ******************\n");
                printf("\n  Termo em ingl%cs: ",136);
            break;
            case '2' :
                printf("\n\n  ***********************\n");
                printf("  * Inserir novo termo *\n");
                printf("  ***********************\n");
                printf("\n  Termo em ingl%cs: ",136);
                gets(ter.ingles);
                if(buscaTermo(&dic,ter) < 0) {
                    printf("\n  Termo em portugu%cs: ",136);
                    gets(ter.portugues);
                    insereTermo(&dic,ter);
                }
                else
                    printf("  Termo ja existe\n");
                //ter.ingles[strlen(ter.ingles)-1] = '\0';
                //ter.portugues[strlen(ter.portugues)-1] = '\0';
            break;
            case '3' :
                printf("\n\n  *****************\n");
                printf("  * Alterar termo *\n");
                printf("  *****************\n\n");
                printf("\n  Termo em ingl%cs: ",136);
                gets(ter.ingles);
                strcpy(ter.portugues,"");
                int rb = buscaTermo(&dic,ter);
                if(rb < 0)
                    printf("nananan");
                else
                {
                    gets(ter.ingles);
                    gets(ter.portugues);
                    dic.termos[rb] = ter;
                }
            break;
            case '4' :
                printf("\n\n  ********************************\n");
                printf("  * Listagem de termos em ingl%cs *\n",136);
                printf("  ********************************\n\n");
                qsort(dic.termos,dic.nte,sizeof(TTermo),ordIng);
                mostreDicionario(&dic,'I');
            break;
            case '5' :
                printf("\n\n  ***********************************\n");
                printf("  * Listagem de termos em portugu%cs *\n",136);
                printf("  ***********************************\n\n");
                qsort(dic.termos,dic.nte,sizeof(TTermo),ordPor);
                mostreDicionario(&dic,'P');
            break;
            default :
                printf("\n  **** Op%c%co inv%clida ****\n",135,198,160);
        }
        printf("\n\n");
        op = menu();
        system("cls");
    }

    fp = fopen("dicionario.arq","wb");
    fwrite(&dic,sizeof(TDicionario),1,fp);
    fclose(fp);

    return 0;
}
