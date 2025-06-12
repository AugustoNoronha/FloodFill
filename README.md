# Sistema de Mapeamento Inteligente para Robôs Autônomos

## Visão Geral do Projeto

Este projeto consiste no desenvolvimento de um sistema de mapeamento inteligente para robôs autônomos. A principal funcionalidade é a identificação e classificação de regiões em um terreno previamente desconhecido, representado por um grid bidimensional. O sistema utiliza o renomado **Algoritmo Flood Fill** para "colorir" automaticamente todas as áreas livres e conectadas, facilitando a visualização e o planejamento de operações para os robôs.

## O Problema Resolvido

Robôs autônomos que operam em ambientes não mapeados precisam de mecanismos eficientes para entender o espaço ao seu redor. O terreno é modelado como um grid onde cada célula pode ser um espaço navegável (livre) ou um obstáculo. Diferentes áreas navegáveis podem estar isoladas por barreiras, formando regiões desconectadas.

O desafio é, a partir de um ponto inicial, identificar todas as células navegáveis que estão conectadas a esse ponto , preenchê-las com uma cor única, e então encontrar e preencher automaticamente outras regiões desconectadas até que todo o terreno navegável seja mapeado. Isso é crucial para que o robô possa planejar rotas, evitar colisões e otimizar suas tarefas.

## Como o Algoritmo Flood Fill Funciona

O algoritmo Flood Fill é um algoritmo de busca que se baseia na ideia de "inundar" uma área conectada. 

1.  **Ponto de Partida:** O algoritmo começa em uma célula inicial definida $(x, y)$.
2.  **Verificação de Condições:** Para cada célula que o algoritmo visita, ele verifica:
    * Se a célula está dentro dos limites do grid.
    * Se a célula possui o valor `0` (terreno navegável). Obstáculos (`1`) ou células já preenchidas (valores `>1`) são ignoradas, garantindo que o robô não "colida" com eles e que regiões já mapeadas permaneçam intactas.
3.  **Preenchimento:** Se a célula atual atender às condições (está dentro dos limites e é navegável), ela é "pintada" com uma nova cor (um valor numérico, como `2`, `3`, `4`, etc.).
4.  **Expansão:** Após colorir a célula atual, o algoritmo se move para seus vizinhos em todas as direçoes (acima, abaixo, à esquerda e à direita) e repete o processo recursivamente. Isso faz com que o preenchimento se espalhe por todas as células navegáveis conectadas, como uma "inundação".
5.  **Múltiplas Regiões:** Uma vez que uma região conectada é completamente preenchida, o sistema varre todo o grid para encontrar a próxima célula com valor `0` (indicando uma nova região navegável ainda não mapeada). Ao encontrar uma, ele inicia um novo processo de Flood Fill a partir dessa célula, utilizando uma nova cor (incrementando o valor da cor anterior). Este processo continua até que não haja mais células com valor `0` no grid, garantindo que todo o terreno navegável seja mapeado.

## Configuração e Execução do Projeto

Este projeto é implementado em Python e contém todo o código em um único arquivo `main.py`.

### Pré-requisitos

* Python 3.x instalado.

### Como Executar

1.  **Clone o projeto:** Clone o projeto em uma pasta de sua preferencia.

2.  **Abra o Terminal:** Navegue até o diretório onde você clonou o projeto.

3.  **Execute o Script:** Execute o arquivo Python com o seguinte comando:

    ```bash
    python main.py
    ```

O programa imprimirá no terminal o grid inicial, mensagens de progresso sobre o preenchimento das regiões e, finalmente, o grid mapeado e colorido.

## Exemplos de Entrada e Saída

### Exemplo 1

Este exemplo demonstra o preenchimento de múltiplas regiões desconectadas.

**Entrada:**

* **Grid inicial (`0` = navegável, `1` = obstáculo):**
    ```
    0 0 1 0 0
    0 1 1 0 0
    0 0 1 1 1
    1 1 0 0 0
    ```
* **Coordenadas iniciais:** `(0, 0)`

**Saída (Grid preenchido):**

* A primeira região iniciada em `(0,0)` é preenchida com `2`.
* A segunda região encontrada é preenchida com `3`.
* A terceira região encontrada é preenchida com `4`.

```
2 2 1 3 3
2 1 1 3 3
2 2 1 1 1
1 1 4 4 4
```

### Exemplo 2

Este exemplo mostra um terreno com diferentes padrões de obstáculos e uma célula inicial em outra posição.

**Entrada:**

* **Grid inicial (`0` = navegável, `1` = obstáculo):**
    ```
    0 1 0 0 1
    0 1 0 0 1
    0 1 1 1 1
    0 0 0 1 0
    ```
* **Coordenadas iniciais:** `(0, 2)`

**Saída (Grid preenchido):**

* A primeira região iniciada em `(0,2)` é preenchida com `2`.
* A segunda região encontrada é preenchida com `3`.
* A terceira região encontrada é preenchida com `4`.

```
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4
```

### Exemplo Adicional:

Este exemplo demonstra como o sistema lida com uma célula inicial que não é navegável e ainda assim mapeia o restante do grid.

**Entrada:**

* **Grid inicial:**
    ```
    1 0 0
    0 0 0
    0 0 0
    ```
* **Coordenadas iniciais:** `(0, 0)` 

**Saída (Grid preenchido):**

* Como a célula inicial é um obstáculo, o primeiro preenchimento a partir dela é ignorado.
* O sistema então varre o grid, encontra a primeira célula navegável (`0`) e inicia o preenchimento a partir daí com a cor `2`.

```
1 2 2
2 2 2
2 2 2
```
