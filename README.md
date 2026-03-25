# AlgoritomoFloyd-Warshall

## Sobre o Projeto

Este projeto implementa o **Algoritmo de Floyd-Warshall** em Python, que calcula as menores distâncias entre todos os pares de vértices em um grafo direcionado e ponderado. O programa também exibe uma representação visual do grafo resultante utilizando as bibliotecas `networkx` e `matplotlib`.

## Funcionalidades

- Leitura interativa da matriz de distâncias inicial
- Suporte a valores infinitos (`inf`) para arestas inexistentes
- Cálculo das menores distâncias entre todos os pares de vértices
- Exibição da matriz final com os caminhos mínimos
- Geração de um grafo direcionado com as arestas resultantes
- Visualização gráfica do grafo com os pesos das arestas

## Pré-requisitos

Certifique-se de ter instaladas as seguintes bibliotecas Python:

```bash
pip install networkx matplotlib
🧠 Como o Algoritmo Funciona
O algoritmo de Floyd-Warshall compara todas as possíveis rotas entre cada par de vértices, considerando cada vértice como um ponto de passagem intermediário. A cada iteração, ele atualiza a matriz de distâncias caso encontre um caminho mais curto.

A complexidade do algoritmo é O(n³), onde n é o número de vértices.

🖥️ Como Executar
Execute o script:

bash
python AlgoritimoFloyd-Warshall.py
Informe o número de vértices do grafo.

Digite a matriz de adjacência linha por linha, separando os valores por espaços.

Para valores infinitos, utilize a palavra inf.

Exemplo para 3 vértices:

text
0 5 inf
inf 0 2
3 inf 0
O programa exibirá a matriz com as menores distâncias e abrirá uma janela com a visualização do grafo.

📊 Exemplo de Uso
Entrada:

text
Número de vértices: 3
Digite a matriz (use 'inf' para infinito):
0 5 inf
inf 0 2
3 inf 0
Saída:

text
Menores distâncias:
[0.0, 5.0, 7.0]
[5.0, 0.0, 2.0]
[3.0, 8.0, 0.0]
O grafo resultante será exibido com as conexões e seus respectivos pesos.

📁 Estrutura do Código
Entrada dos dados - Leitura do número de vértices e da matriz de distâncias

Algoritmo de Floyd-Warshall - Triplo loop que atualiza as distâncias mínimas

Exibição da matriz - Apresentação do resultado no terminal

Visualização gráfica - Construção e exibição do grafo com networkx

📦 Tecnologias Utilizadas
Python 3.x

math - Para representação de infinito

networkx - Criação e manipulação de grafos

matplotlib - Visualização gráfica

👤 Autor
Desenvolvido como parte de estudos sobre algoritmos de grafos e teoria dos grafos.
