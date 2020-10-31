%facts for scores problems
nota(joao,5.0).
nota(maria,6.0).
nota(joana,8.0).
nota(mariana,9.0).
nota(cleuza,8.5).
nota(jose,6.5).
nota(jaoquim,4.5).
nota(mara,4.0).
nota(mary,10.0).

aprovado(X):-
    nota(X,Y),
    Y > 6.9.


recuperacao(X):-
    nota(X,Y),
    Y < 7,
    Y > 4.9.


reprovado(X):-
    nota(X,Y),
    Y < 5.

%facts for family problems

progenitor(jose,joao).
progenitor(maria,joao).
progenitor(jose,ana).
progenitor(maria,ana).
progenitor(ana,joana).

progenitor(ana,helena).
progenitor(joao,mario).
progenitor(mario,carlos).
progenitor(helena,carlos).

sexo(maria,feminino).
sexo(ana,feminino).
sexo(helena,feminino).
sexo(joana,feminino).
sexo(joao,masculino).
sexo(jose,masculino).
sexo(mario,masculino).
sexo(carlos,masculino).

sexo_e(X,Y):-
    sexo(X,Y).

irma(X,Y):-
    sexo(X,feminino),
    progenitor(PX,X),
    progenitor(PX,Y),
    X\==Y.


irmao(X,Y):-
    sexo(X,masculino),
    progenitor(PX,X),
    progenitor(PX,Y),
    X\==Y.


irmaos(X,Y):-
    progenitor(PX,X),
    progenitor(PX,Y),
    X\==Y.

descendente(X,Y):-
    progenitor(X,Y).

descendente(X,Y):-
    progenitor(X,Y),
    descendente(X,Y).

mae(X,Y):-
    progenitor(X,Y),
    sexo(X,feminino).

pai(X,Y):-
    progenitor(X,Y),
    sexo(X,masculino).

av�(X,Y):-
    progenitor(X,PX),
    progenitor(PX,Y),
    sexo(X,masculino).

av�(X,Y):-
    progenitor(X,PX),
    progenitor(PX,Y),
    sexo(X,feminino).

tio(X,Y):-
    progenitor(IX,Y),
    irmaos(X,IX).


primo(X,Y):-
    sexo(X,masculino),
    progenitor(IX,X),
    progenitor(IY,Y),
    irmaos(IX,IY).


primos(X,Y):-
    progenitor(IX,X),
    progenitor(IY,Y),
    irmaos(IX,IY).

joao_filho_de_jose():-
    progenitor(jose,joao).

filhos_de_maria(X):-
    mae(maria,X).


primos_mario(X):-
    primos(mario,X).

qntd_sobrinhos_com_um_tio(X):-
    tio(Y,X).

ascendentes_carlos():-
    descendente(X,carlos).

helena_tem_irmaos():-
    irmaos(helena,X).

fatorial(0,1).

fatorial(N,F):-
    N>0,
    N1 is N-1,
    fatorial(N1, F1),
    F is N * F1.























