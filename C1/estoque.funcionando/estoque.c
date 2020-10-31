
#include <stdio.h>
#include <string.h>

#define CAIXA 10000

typedef struct Produto{
    int estoque;
    int codigo;
    char descricao[41];
    float valorDeCompra;
    float valorDeVenda;
}TProduto;

typedef struct ListadeProdutos{
    int numProduto;
    float caixa;
    TProduto produtos[50];
}TLista;

int menuPrincipal(){
    int opcao = 0;
    while (!opcao) {
        printf("### Menu ###\n");
        printf("  1 - Buscar Produto\n\n");
        printf("  2 - Comprar Produto\n\n");
        printf("  3 - Vender Produto\n\n");
        printf("  4 - Listar todos os Produtos\n\n");
        printf("  5 - Sair\n\n");
        printf("  Digite uma opcao: ");
        scanf("%d",&opcao);
        if (opcao<1 || opcao>5) {
            opcao = 0;
            printf("  /nDigite uma opcao valida!\n");
        }
    }
    return opcao;
}

void inserirNaLista(TLista *lista, TProduto produto){
    produto.codigo = lista->numProduto+1;
    lista->produtos[lista->numProduto++] = produto;
    lista->caixa -= produto.valorDeCompra*produto.estoque;

    printf("  Produto inserido com sucesso!\n\n");
}

void inserirProduto(TLista *lista){
    TProduto produto;
    char buffer[2];

    gets(buffer);
    printf("  Digite o nome do produto: ");
    fgets(produto.descricao, 41, stdin);
    strtok(produto.descricao, "\n");
    printf("  Digite valor de compra: ");
    scanf("%f", &produto.valorDeCompra);
    produto.valorDeVenda = 1.5*produto.valorDeCompra;
    printf("  Digite quantidade: ");
    scanf("%d", &produto.estoque);

    inserirNaLista(lista, produto);
}

void escreverArquivo(TLista *lista){
    FILE *f;
    f = fopen("produtos.bin", "wb");
    fwrite(&lista, sizeof(TLista),1,f);
    fclose(f);
}

void lerArquivo(TLista *lista){
    FILE *f;
    f = fopen("produtos.bin", "rb");
    fread(&lista, sizeof(TLista),1,f);
    fclose(f);
}

void inicializarLista(TLista *lista){
    lista->caixa = CAIXA;
    lista->numProduto = 0;

    escreverArquivo(lista);
}

int buscarProduto(TLista *lista){
    int i;
    char nome[41];
    char buffer[2];

    gets(buffer);
    printf("  Digite o nome do produto: ");
    fgets(nome, 41, stdin);
    strtok(nome, "\n");

    for (i = 0; i<lista->numProduto; i++) {
        if (strcmp(nome, lista->produtos[i].descricao) == 0){
            return i;
        }
    }
    return -1;
}

void mostreProduto(TProduto produto){
    printf(" %-3d   %-21s  %-40.2f  %-45.2f  ",produto.codigo, produto.descricao, produto.valorDeCompra,
           produto.valorDeVenda);
    if (produto.estoque != 0) {
        printf("%-54d\n", produto.estoque);
    }else{
        printf(" Nao possui mais no estoque!\n");
    }
}

void mostreTodosProdutos(TLista *lista){
    int i;
    printf("  Cod   Descricao do produto     Compra     Venda   Estoque \n "); //aqui print
    for (i = 0; i<lista->numProduto; i++) {
        mostreProduto(lista->produtos[i]);
    }
}

void vendeProduto(TLista *lista, int index){
    if (lista->produtos[index].estoque > 0) {
        printf("Digite a quantidade a serem vendidas: ");
        int aux;
        scanf("%d",&aux);
        lista->produtos[index].estoque-=aux;

        lista->caixa += lista->produtos[index].valorDeVenda;
    }else{
        printf("Não há produtos\n");
    }
}

int main() {
    int ctrl = 1;
    int aux;

    TLista lista;

    //inicializarLista(&lista);
    lerArquivo(&lista);

    while (ctrl) {
        printf("R$ %.2f\n",lista.caixa);
        switch (menuPrincipal()) {
            case 1:
                aux = buscarProduto(&lista);
                if(aux != -1){
                    mostreProduto(lista.produtos[aux]);
                }else{
                    printf("Produto não encontrado\n");
                }
                break;
            case 2:
                inserirProduto(&lista);
                break;
            case 3:
                aux = buscarProduto(&lista);
                if(aux != -1){
                    mostreProduto(lista.produtos[aux]);
                }else{
                    printf("Produto não encontrado\n");
                }
                vendeProduto(&lista, aux);
                break;
            case 4:
                mostreTodosProdutos(&lista);
                break;
            case 5:
                ctrl = 0;
                escreverArquivo(&lista);
                break;
            default:
                break;
        }
    }
    return 0;
}
