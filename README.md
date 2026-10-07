# 01 - Introdução a Algoritmos

Esta pasta é dedicada aos conceitos fundamentais de lógica e introdução a algoritmos.

## 📌 Conteúdo Teórico
- **O que é um Algoritmo:** Sequência finita de instruções lógicas e bem definidas que visam resolver um problema ou executar uma tarefa.
- **Formas de Representação:**
  - *Descrição Narrativa*: Uso de linguagem natural para descrever os passos (ex.: receita de bolo).
  - *Fluxograma*: Representação gráfica e padronizada do fluxo de dados e decisões.
  - *Pseudocódigo (Portugol)*: Escrita estruturada próxima de uma linguagem de programação, mas acessível e independente de sintaxes complexas.
- **Instruções Sequenciais:** A ordem de execução de cima para baixo.

---
> *Nota: Este módulo introduz a base teórica do curso. A partir do próximo módulo iniciam-se os scripts práticos em Python.*

# 02 - Primeiro Algoritmo

Primeiro contato com a linguagem Python, saída de dados e manipulação inicial de variáveis.

## 📌 Conteúdos Abordados
- Função de saída padrão: `print()`
- Criação e atribuição de variáveis de texto (strings)
- Exibição de valores literais e referências de variáveis no terminal

## 📁 Scripts Nesta Categoria
| Arquivo | Descrição |
| :--- | :--- |
| [`01. primeiro.py`](./01.%20primeiro.py) | Primeiro algoritmo: criação de variável textual e testes com a função `print()`. |

# 03 - Comandos de Entrada e Operadores

Leitura de dados informados pelo usuário, conversão de tipos de dados (casting), operadores aritméticos, relacionais e lógicos, e funções matemáticas.

## 📌 Conteúdos Abordados
- **Comando de Entrada:** `input()`
- **Tipos Primitivos e Conversões:** `int()`, `float()`, `str()`
- **Operadores Aritméticos:** `+`, `-`, `*`, `/`, `**` (exponenciação), `%` (módulo/resto)
- **Precedência de Operadores:** Uso de parênteses para ditar a prioridade de cálculo
- **Funções Matemáticas:** Módulo `math` (`sqrt`, `radians`, `sin`, etc.) e funções embutidas (`abs`, `pow`)
- **Operadores Relacionais:** `>`, `<`, `>=`, `<=`, `==`, `!=`
- **Operadores Lógicos:** `and`, `or`, `not`

## 📁 Scripts Nesta Categoria
| Arquivo | Descrição |
| :--- | :--- |
| [`02. atribuicoes.py`](./02.%20atribuicoes.py) | Leitura do nome do usuário via `input()` e formatação de texto com f-strings. |
| [`02. dolares.py`](./02.%20dolares.py) | Conversão de moedas (Reais para Dólares) utilizando divisão aritmética. |
| [`03. conversor-temp-c-f.py`](./03.%20conversor-temp-c-f.py) | Conversão de temperatura Fahrenheit para Celsius com fórmula matemática. |
| [`03. somas.py`](./03.%20somas.py) | Entrada de dados e soma entre valores. |
| [`04. haddad.py`](./04.%20haddad.py) | Cálculo aritmético de porcentagem de imposto (60%). |
| [`04. media.py`](./04.%20media.py) | Cálculo da média aritmética demonstrando a precedência dos parênteses. |
| [`05. emprestimo.py`](./05.%20emprestimo.py) | Cálculo de juros de 20% e divisão de parcelas de um empréstimo. |
| [`05. funcao_aritmetica.py`](./05.%20funcao_aritmetica.py) | Aplicação de funções aritméticas (`abs`, `pow`, `sqrt`, trigonometria com `math`). |
| [`06. maior_menor_que.py`](./06.%20maior_menor_que.py) | Comparações relacionais completas entre dois números inteiros. |
| [`07. p_e_q.py`](./07.%20p_e_q.py) | Expressões lógicas booleanas com `or` e comparações relacionais. |
| [`08. triangulos.py`](./08.%20triangulos.py) | Teste de existência de triângulo e classificação (Equilátero, Escaleno, Isósceles) puramente com operadores lógicos. |

# 04 - Estruturas Condicionais

Desvios condicionais simples, compostos, aninhados e de múltipla escolha com `if`, `elif`, `else` e `match / case`.

## 📌 Conteúdos Abordados
- **Condicional Simples:** `if <condição>:`
- **Condicional Composta:** `if <condição>: ... else: ...`
- **Condicionais Aninhadas:** `if ... elif ... else:`
- **Seleção Múltipla:** `match ... case:` (equivalente a `escolha / caso`)

## 📁 Scripts Nesta Categoria
| Arquivo | Descrição |
| :--- | :--- |
| [`01. idade.py`](./01.%20idade.py) | Cálculo da idade atual e validação de maioridade (`if`). |
| [`0111. eq_seg_grau.py`](./0111.%20eq_seg_grau.py) | Equação do 2º grau: cálculo de delta e identificação de raízes reais (`if / elif / else`). |
| [`02. par_impar.py`](./02.%20par_impar.py) | Verificação se um número é PAR ou ÍMPAR utilizando operador de resto (`%`) e condicional composta. |
| [`03. imc.py`](./03.%20imc.py) | Cálculo do IMC e classificação nas faixas de peso corporal (`if / elif`). |
| [`04. apto-a-direcao.py`](./04.%20apto-a-direcao.py) | Validação de elegibilidade para habilitação no departamento de trânsito. |
| [`05. notas.py`](./05.%20notas.py) | Cálculo de média e determinação de situação: Aprovado, Recuperação ou Reprovado. |
| [`06. ir para bangladesh.py`](./06.%20ir%20para%20bangladesh.py) | Verificação de condições com faixas orçamentárias (`if / elif / else`). |
| [`11. crianca_esperanca.py`](./11.%20crianca_esperanca.py) | Menu de seleção de doações do Criança Esperança. |
| [`12. Funcionaris.py`](./12.%20Funcionaris.py) | Reajuste salarial escalonado pelo número de dependentes. |
| [`13. desempenho_aluno.py`](./13.%20desempenho_aluno.py) | Conversão de média numérica em conceito de desempenho (A, B, C, D, E, F). |
| [`14. Futebol 2009.py`](./14.%20Futebol%202009.py) | Cálculo de diferença de gols e status da partida com `match / case`. |
| [`17. haddad 4x.py`](./17.%20haddad%204x.py) | Verificação condicional de cobrança de imposto. |

# 05 - Estruturas de Repetição

Laços de repetição (iterações e loops) utilizando `while` (com teste lógico no início) e `for` com `range()`.

## 📌 Conteúdos Abordados
- **Laço `while`:** Repetição enquanto uma condição for verdadeira.
- **Variáveis de Controle:** Contadores (`cont += 1`) e acumuladores (`soma += valor`).
- **Valores Extremos:** Algoritmos para detecção de maior e menor valor dentro do laço.
- **Laço `for` com `range()`:** Estrutura de repetição com variável de controle e limites predefinidos.
- **Laço Infinito:** `while True:` com condições de interrupção ou execução contínua.

## 📁 Scripts Nesta Categoria
| Arquivo | Descrição |
| :--- | :--- |
| [`09. andando.py`](./09.%20andando.py) | Simulação de passos utilizando loop `for` e temporizador `time.sleep()`. |
| [`15. troca troca ( ͡° ͜ʖ ͡°).py`](./15.%20troca%20troca%20%28%20%CD%A1%C2%B0%20%CD%9C%CA%96%20%CD%A1%C2%B0%29.py) | Contagem progressiva e regressiva com laços `while`. |
| [`16. somador_tamanho.py`](./16.%20somador_tamanho.py) | Acumulador de valores e identificação do maior número digitado com `while`. |
| [`18. dolares x4.py`](./18.%20dolares%20x4.py) | Repetição de conversões cambiais usando contador em laço `while`. |
| [`19. contador.py`](./19.%20contador.py) | Contador inteligente (progressivo ou regressivo) com `while`. |
| [`20. kbsa de sibola.py`](./20.%20kbsa%20de%20sibola.py) | Leitura de múltiplos alunos com identificação do melhor aluno e maior nota. |
| [`21. somador.py`](./21.%20somador.py) | Somador com quantidade de termos definida dinamicamente pelo usuário. |
| [`22. bol.py`](./22.%20bol.py) | Tabuada com repetições configuráveis via laço `while`. |
| [`23. negativos.py`](./23.%20negativos.py) | Contagem da quantidade de números negativos inseridos dentro do laço. |
| [`24. fatoral.py`](./24.%20fatoral.py) | Cálculo matemático de fatorial utilizando laço `while`. |
| [`25. procurando o meu primo.py`](./25.%20procurando%20o%20meu%20primo.py) | Verificação de número primo por meio da contagem de divisores no laço `while`. |
| [`26. for fim.py`](./26.%20for%20fim.py) | Tabuada e somatório de intervalos utilizando o laço `for` com `range()`. |
| [`tela_hack.py`](./tela_hack.py) | Loop contínuo (`while True`) gerando fluxo de caracteres aleatórios no terminal. |

# 06 - Procedimentos

Sub-rotinas e rotinas em Python que realizam ações sem retornar um valor explícito (`void`).

## 📌 Conteúdos Teóricos
- **O que é um Procedimento:** Bloco de código com nome definido que agrupa instruções para serem reaproveitadas sempre que chamadas, sem a necessidade de retornar um valor com `return`.
- **Definição em Python:**
  ```python
  def saudacao(nome):
      print(f"Olá, {nome}! Bem-vindo ao sistema.")
  
  # Chamada do procedimento:
  saudacao("Paulo")
  ```
- **Passagem de Parâmetros:** Passagem de dados para o procedimento através de parâmetros/argumentos.
- **Diferença entre Procedimento e Função:** Enquanto o procedimento apenas executa um conjunto de instruções (geralmente gerando efeitos colaterais, como impressões na tela ou modificações de estado), uma função calcula e retorna um valor via `return`.

---
> *Nota: Pasta reservada para os exercícios do Módulo 12 (Procedimentos).*

# 07 - Funções

Sub-rotinas que realizam processamento e retornam um valor ao chamador através da instrução `return`.

## 📌 Conteúdos Teóricos
- **O que é uma Função:** Bloco de código reutilizável que recebe argumentos, executa um processamento e **devolve (retorna)** um valor com a palavra-chave `return`.
- **Definição em Python:**
  ```python
  def somar(a, b):
      return a + b

  # Uso da função:
  resultado = somar(10, 5)
  print(f"Resultado: {resultado}")
  ```
- **Retorno de Valores:** Uso de `return` para entregar o resultado do cálculo.
- **Escopo de Variáveis:** Variáveis locais (definidas dentro da função) vs variáveis globais.

---
> *Nota: Pasta reservada para os exercícios do Módulo 13 (Funções).*

# 08 - Vetores

Estruturas de variáveis compostas homogêneas unidimensionais (vetores / arrays / listas em Python).

## 📌 Conteúdos Teóricos
- **O que é um Vetor:** Estrutura que permite armazenar múltiplos valores sob uma mesma variável, acessados por índices numéricos (em Python, começando do índice `0`).
- **Definição em Python (Listas):**
  ```python
  valores = [10, 20, 30, 40, 50]
  
  # Acessando elementos:
  print(valores[0])  # Primeiro elemento: 10
  
  # Adicionando elementos:
  valores.append(60)
  
  # Iterando sobre o vetor:
  for valor in valores:
      print(valor)
  ```
- **Operações Comuns:**
  - Preenchimento e leitura de dados pelo usuário
  - Busca de valores em um vetor
  - Ordenação de elementos
  - Contagem e cálculos sobre os dados armazenados

---
> *Nota: Pasta reservada para os exercícios do Módulo 14 (Vetores).*

# 09 - Matrizes

Estruturas de variáveis compostas bidimensionais (matrizes / listas de listas em Python), compostas por linhas e colunas.

## 📌 Conteúdos Teóricos
- **O que é uma Matriz:** Coleção bidimensional de dados organizada em linhas e colunas, onde cada posição é identificada por dois índices `[linha][coluna]`.
- **Definição em Python:**
  ```python
  # Matriz 3x3:
  matriz = [
      [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]
  ]

  # Acessando o elemento da linha 1, coluna 2 (valor 6):
  print(matriz[1][2])

  # Percorrendo a matriz com laços aninhados:
  for linha in range(3):
      for coluna in range(3):
          print(f"{matriz[linha][coluna]:4}", end="")
      print()
  ```
- **Operações Comuns:**
  - Leitura e preenchimento de matrizes
  - Identificação da diagonal principal e diagonal secundária
  - Criação de matriz identidade
  - Operações matemáticas (soma de elementos da linha/coluna, transposta)

---
> *Nota: Pasta reservada para os exercícios do Módulo 15 (Matrizes).*
