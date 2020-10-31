# Problema da Ponte Estreita

Carros vindos do norte e carros vindos do sul chegam a uma ponte com só uma pista. Os
que viajam no mesmo sentido podem atravessar a ponte ao mesmo tempo, mas os que
viajam em sentido oposto não podem. Modele os carros como threads e use semáforos
para sincronização entre threads. Note que os carros devem sair da ponte na mesma ordem
em que entraram (não é possível ultrapassagem, pois a ponte só tem uma pista).

## Configuração:

Ao iniciar a execução, o usuário deverá configurar a direção preferencial da ponte.

- **Leste-Oeste:** Os carros que trafegam no sentido leste-oeste têm preferência sobre os
carros que trafegam no sentido oeste-leste. Neste caso, um carro que trafega no
sentido oeste-leste somente pode iniciar a travessia sobre a ponte quando não
houver nenhum carro na direção leste-oeste atravessando a ponte ou aguardando a
sua liberação.

- **Oeste-Leste:** Os carros que trafegam no sentido oeste-leste têm preferência sobre os
carros que trafegam no sentido leste-oeste. Neste caso, um carro que trafega no
sentido leste-oeste somente pode iniciar a travessia sobre a ponte quando não
houver nenhum carro na direção oeste-leste atravessando a ponte ou aguardando a
sua liberação.

- **Nenhuma:** Neste caso, um carro não pode atravessar a ponte apenas quando houver
carros atravessando a ponte no sentido contrário.

## Criar processo carro:

Durante a criação do processo carro devem ser definidos os seguintes parâmetros:

- **Tempo de travessia:** tempo (em segundos) que o carro leva para atravessar a ponte
na ausência de carros mais lentos à frente dele. Um carro não pode ultrapassar outro
sobre a ponte.

- **Tempo de permanência no mesmo lado da ponte:** tempo (em segundos) que o
carro permanece no mesmo lado da ponte. Depois de decorrido este tempo, o carro
deverá tentar atravessar a ponte para o outro lado.

## Eliminar processo carro:

Esta opção permite eliminar o processo carro, para posteriormente poder criar outro
processo com novos parâmetros.

## Saídas:

A interface deverá atender aos seguintes requisitos:

- Mostrar os dados de cada carro: identificador, tempo de travessia e tempo de
permanência.

- Mostrar todos os carros (parados, aguardando a liberação da ponte ou atravessando a
ponte).

- Mostrar, a cada instante, o status de cada processo carro (atravessando a ponte no
sentido leste-oeste, atravessando a ponte no sentido oeste-leste, aguardando a
liberação da ponte ou parado no mesmo lado da ponte).

- Mostrar um log com os principais eventos de cada carro.

### Datas de entrega 18/10/2017

