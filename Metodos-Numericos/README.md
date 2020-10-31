# Metodos-Numericos
Algoritmos em Linguagem C para disciplina de Metodos Numericos trabalho em Equipe(Raphael Andradr,Alcivanio,Andre,Nathan)

1º Exercício-programa de Métodos Numéricos
Prof. Glauber Cintra – Entrega: 23/out/17

Este EP deve ser feito por grupos de no mínimo 3 e no máximo 4 alunos. Ele vale 5 pontos.

Escreva um programa em C com um menu principal que possua 4 opções: ‘C’ – Conversão, ‘S’ – Sistema Linear, ‘E’ – Equação Algébrica e ‘F’ – Finalizar.

Ao selecionar a opção ‘C’, o usuário deverá digitar um número decimal, eventualmente com parte fracionária, e o programa deverá exibir esse número nos sistemas numéricos binário, octal e hexadecimal com até vinte casas decimais significativas. Por exemplo, se o usuário digitar o número 14.25 o programa deverá exibir:

Binário: 1110.01
Octal: 16.2
Hexadecimal: E.4

Ao selecionar a opção ‘S’, o programa deverá pedir o nome de um arquivo de texto contendo um sistema linear de n equações e n variáveis. O lay-out do arquivo deverá ser:

n
a1,1 a1,2 ... a1,n b1
a2,1 a2,2 ... a2,n b2
...
an,1 an,2 ... an,n bn

onde ai,j é o coeficiente da variável j na equação i e bi é o termo independente da equação i. Por exemplo, o arquivo correspondente ao sistema:

 x1 –  x2 + 3x3 =  8
2x1 – 2x2 +  x3 =  1
–x1 + 3x2 –  x3 =  2

seria

 3
 1 -1  3  8
 2 -2  1  1
-1  3 -1  2

O programa deverá então verificar se a matriz de coeficientes satisfaz o critério das linhas ou o critério das colunas. Se isso não ocorrer, o programa deverá apenas informar que o sistema linear não satisfaz o critério das linhas nem o critério das colunas. Caso contrário, o programa deverá calcular uma solução aproximada do sistema linear usando o método de Gauss-Seidel. Pare quando a variação no valor das variáveis numa iteração for menor que  10-8 ou após 1000 iterações. Exiba a solução encontrada e o número de iterações realizadas.

Entregue, dentro de uma folha plástica transparente, um CD contendo somente o arquivo ep1.c. Tal arquivo deverá estar no diretório raiz do CD. Escreva no CD o nome de todos os integrantes do grupo. Entregue, também dentro da folha plástica, uma listagem impressa do programa.

Ao selecionar a opção ‘E’, o programa deverá ler uma equação algébrica da forma anxn + an-1xn-1 + ... + a1x + a0, com an> 0 e a0 ≠ 0. O programa deverá solicitar o grau da equação e os coeficientes an, an-1, ..., a0, nessa ordem. O programa deve exigir que an> 0 e a0 ≠ 0. 

Utilizando o Teorema de Lagrange, o programa deverá calcular e exibir os intervalos onde se encontram as raízes reais negativas e as raízes reais positivas da equação. Utilizando o limite superior do intervalo onde se encontram as raízes positivas como aproximação inicial (x0), o programa deverá determinar uma aproximação para uma raiz usando o Método de Newton. Pare quando a diferença (em módulo) entre duas soluções aproximadas for menor do que 10-8 ou após 1000 iterações. Exiba a solução encontrada e o número de iterações realizadas.

Siga rigorosamente as especificações contidas neste texto. Não se esqueça de colocar comentários no seu programa, indentar o código, usar nomes de variáveis significativos, modularizar o código, enfim, programar com estilo. Programas com erros de compilação serão rejeitados.
