[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/PqHvR8Ro)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11018717&assignment_repo_type=AssignmentRepo)
# Funções - Fibonacci

O script principal de vocês deve estar no arquivo `main.py`.

## 📝 Instruções 📝

Escreva uma função que recebe um número inteiro `n` como parâmetro e retorna o `n`-ésimo número da sequência de Fibonacci.

O identificador da função deve ser `fibonacci`.

Caso a função receba um número `n < 0` a função deve lançar um erro do tipo `ValueError`.
Para isso basta fazer a instrução `raise ValueError("n tem que ser maior do que zero")`.

## 🧑‍💻 Exemplo de Execução 🧑‍💻

```python
fibonacci(0) # 0
fibonacci(1) # 1
fibonacci(2) # 1
fibonacci(3) # 2
fibonacci(4) # 3
fibonacci(5) # 5
fibonacci(6) # 8
fibonacci(7) # 13
fibonacci(8) # 21
```

## 🧪 Testes Automáticos 🧪

Para testar automaticamente o programa **antes** de fazer um commit e enviar o seu trabalho existem algumas formas de fazer isso.

1. executar o módulo `unittest` direto no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python -m unittest
```

2. executar o arquivo `test_main.py` no terminal.
   Para isso, basta executar o seguinte comando:

```bash
python test_main.py
```

3. caso você esteja usando o [VSCode](https://code.visualstudio.com/), você pode abrir a paleta de comandos `CTRL+SHIFT+P` e digitar `Run All Tests`.
4. no seu editor de código, você pode executar o arquivo `test_main.py` e verificar o resultado dos testes no terminal.

## 🤖 Observações Importantes 🤖

- **Não altere o nome dos arquivos**. Os arquivos `test_main.py` e `main.py` precisam ter esses nomes para que os testes funcionem.
- **Não altere o nome das funções**. Os testes dependem que as funções tenham os nomes especificados no enunciado ou já escritos nos arquivos.
- **Não altere o nome dos parâmetros**. Os testes dependem que as funções tenham os parâmetros especificados no enunciado ou já escritos nos arquivos.
- **Antes de fazer um commit**, execute os testes usando um dos métodos acima para verificar se o seu programa está funcionando corretamente.
- **Caso não consiga corrigir os erros**, entre em contato com o professor ou monitores para que eles possam te ajudar.
  Para isso você deve fazer um commit com o seu trabalho incompleto e abrir uma **issue** no repositório do exercício explicando o seu problema.
