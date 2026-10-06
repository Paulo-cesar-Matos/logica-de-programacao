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
