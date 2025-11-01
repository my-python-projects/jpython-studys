🌎 Leia em [Português](README.md)

# 🧩 <a name="english-version"></a>Challenge: Pattern Matching with `match` in Python 3.10+

## 🎯 Challenge Objective

The goal is to create a simple mathematical expression interpreter using the new **Structural Pattern Matching** (`match / case`) feature introduced in Python 3.10+.

The program should read expressions like:

```
5 + 3
10 - 2
4 * 6
8 / 2
2 ^ 3
```

And return the **numeric result**, also handling error cases such as division by zero or invalid expressions.

## 🧠 Challenge Requirements

* Create a class or function `evaluate(expression: str) -> float | str`

* Support operations:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
  * Exponentiation (`^` → converted to `**`)

* Use `match / case` to:

  * Separate operator and operands
  * Handle each operation clearly
  * Return errors gracefully

## ⚙️ Rules and Validations

* Return `"Invalid expression"` if the format is unrecognized
* Return `"Error: division by zero"` when applicable
* Allow negative numbers and optional parentheses
* Use regex for format validation
* Use three different pattern types:

  1. **Literal pattern** — for fixed operators (`case "+"`)
  2. **Capture pattern** — for values (`case [op, b]`)
  3. **Guard pattern** — with `if` to validate conditions (like division by zero)

## 🧮 Usage Example

```python
evaluate("5 + 3")      # → 8.0
evaluate("10 / 0")     # → "Error: division by zero"
evaluate("abc")        # → "Invalid expression"
evaluate("(2 + 3) * 4")# → 20.0
evaluate("2 ^ 3")      # → 8.0
evaluate("-5 + 3")     # → -2.0
```

## 🧱 Recommended Structure

A full implementation example (with `match / case`) can be found in the main file:

```
match.py
```

The logic is divided into:

* **Regex Validation** — ensures only valid numbers and operators
* **Parentheses Simplification** — resolves inner expressions first
* **Simple Match Evaluation** — identifies operator and computes the result
* **Interactive Loop (optional)** — allows users to test expressions via terminal

---

# 📘 Theory: Pattern Matching in Python 3.10+

## 🧩 Topic of the Day

**Technology/Concept:**
➡️ Structural Pattern Matching (`match / case`) in Python 3.10+

## 💡 Why is it useful?

Replaces long chains of `if / elif` with a more declarative, readable, and safe syntax, ideal for:

* Command interpretation (CLI, bots, games)
* Processing dynamic JSON / APIs
* Event and action dispatching
* Replacing missing switch-case in older versions

👉 It's like a “supercharged” switch, with data destructuring, guards (`if`), and pattern capture — used in real projects with Flask, FastAPI, Pydantic, etc.

## 📘 Basic Syntax

```python
match subject:
    case pattern1 [if condition]:
        # action
    case pattern2:
        # another action
    case _:
        # default
```

### Key Concepts:

* `case` can capture values, destructure lists/dictionaries, and use guards (`if`)
* `_` is the wildcard (equivalent to `default`)
* Supported patterns:

  * Literals (`case "add")`
  * Variables (`case x`)
  * Tuples / lists (`case [a, b]`)
  * Classes (`case Point(x, y)`)
  * OR pattern (`case "a" | "b"`)
  * Guards (`case v if v > 10:`)

## 💬 Theoretical Example: Command Interpreter

```python
from dataclasses import dataclass
from typing import Literal, Any

@dataclass
class AddTask:
    title: str
    priority: Literal["low", "medium", "high"] = "medium"

@dataclass
class ListTasks:
    filter: Literal["all", "done", "pending"] | None = None

@dataclass
class CompleteTask:
    id: int

def parse_command(user_input: str) -> Any:
    parts = user_input.strip().lower().split()
    if not parts:
        return None

    command = parts[0]
    args = parts[1:]

    match command:
        case "add":
            title = " ".join(args[:-1]) if len(args) > 1 else args[0] if args else ""
            priority = args[-1] if args and args[-1] in {"low", "medium", "high"} else "medium"
            return AddTask(title, priority)

        case "list":
            filter_val = args[0] if args else None
            return ListTasks(filter_val if filter_val in {"all", "done", "pending"} else None)

        case "done" | "complete":
            if args and args[0].isdigit():
                return CompleteTask(int(args[0]))
            return "Invalid ID"

        case "help":
            return "Commands: add, list, done"

        case _:
            return "Unknown command"
```

---

## 🧭 Best Practices

✅ Use `match` only when it improves readability

✅ Always include `case _:` as default

✅ Combine with `dataclasses` to structure data

✅ Prefer simple guards rather than heavy logic inside `case`

✅ Test thoroughly — pattern matching can hide type errors

```python
case Point(x, y) if is_origin(x, y):
    print("It's at the origin!")
```

---

## 🚀 Conclusion

This challenge combines theory and practice:

* **Theory:** learn and apply `match / case` with different patterns
* **Practice:** build a mini mathematical interpreter
* **Benefit:** consolidate understanding of modern Python pattern matching

------------

🌍 Read this in [English](#english-version).

# 🧩 <a name="portuguese-version"></a>Desafio: Pattern Matching com `match` em Python 3.10+

## 🎯 Objetivo do Desafio

O objetivo é criar um interpretador de expressões matemáticas simples utilizando o novo recurso de **Structural Pattern Matching** (`match / case`) introduzido no Python 3.10+.

O programa deve ler expressões como:

```
5 + 3
10 - 2
4 * 6
8 / 2
2 ^ 3
```

E retornar o **resultado numérico**, tratando também casos de erro, como divisões por zero ou expressões inválidas.

## 🧠 Requisitos do Desafio

* Criar uma classe ou função `evaluate(expression: str) -> float | str`

* Suportar as operações:

  * Soma (`+`)
  * Subtração (`-`)
  * Multiplicação (`*`)
  * Divisão (`/`)
  * Potência (`^` → convertido para `**`)

* Usar `match / case` para:

  * Separar operador e operandos
  * Tratar cada operação com clareza
  * Retornar erros de forma elegante

## ⚙️ Regras e Validações

* Retornar `"Expressão inválida"` se o formato não for reconhecido
* Retornar `"Erro: divisão por zero"` quando aplicável
* Permitir uso de números negativos e parênteses opcionais
* Usar regex para validação de formato
* Utilizar três tipos de padrões diferentes:

  1. **Literal pattern** — para operadores fixos (`case "+"`)
  2. **Capture pattern** — para valores (`case [op, b]`)
  3. **Guard pattern** — com `if` para validar condições (como divisão por zero)

## 🧮 Exemplo de Uso

```python
evaluate("5 + 3")      # → 8.0
evaluate("10 / 0")     # → "Erro: divisão por zero"
evaluate("abc")        # → "Expressão inválida"
evaluate("(2 + 3) * 4")# → 20.0
evaluate("2 ^ 3")      # → 8.0
evaluate("-5 + 3")     # → -2.0
```

## 🧱 Estrutura Recomendada

Um exemplo de implementação completa e comentada (com uso de `match / case`) pode ser encontrado no arquivo principal:

```
match.py
```

A lógica é dividida em:

* **Validação com Regex** — garante que só há números e operadores válidos
* **Simplificação de Parênteses** — resolve expressões internas primeiro
* **Avaliação Simples com Match** — identifica operador e aplica o cálculo
* **Loop Interativo (opcional)** — permite ao usuário testar expressões pelo terminal

---

# 📘 Teoria: Pattern Matching no Python 3.10+

## 🧩 Tema do Dia

**Tecnologia/Conceito:**
➡️ Structural Pattern Matching (`match / case`) no Python 3.10+

## 💡 Por que é útil?

Substitui cadeias longas de `if / elif` por uma sintaxe mais declarativa, legível e segura, sendo ideal para:

* Interpretação de comandos (CLI, bots, jogos)
* Processamento de JSON / APIs dinâmicas
* Despacho de eventos e ações
* Substituição de switch-case (ausente em versões antigas)

👉 É como um switch “turbinado”, com desconstrução de dados, guards (`if`) e captura de padrões — usado em projetos reais com Flask, FastAPI, Pydantic, etc.

## 📘 Sintaxe Básica

```python
match subject:
    case pattern1 [if condition]:
        # ação
    case pattern2:
        # outra ação
    case _:
        # default
```

### Conceitos-Chave:

* `case` pode capturar valores, desestruturar listas/dicionários e usar guards (`if`)
* `_` é o wildcard (equivalente ao `default`)
* Padrões suportados:

  * Literais (`case "add")`
  * Variáveis (`case x`)
  * Tuplas / listas (`case [a, b]`)
  * Classes (`case Point(x, y)`)
  * OR pattern (`case "a" | "b"`)
  * Guards (`case v if v > 10:`)

## 💬 Exemplo Teórico: Interpretador de Comandos

```python
from dataclasses import dataclass
from typing import Literal, Any

@dataclass
class AddTask:
    title: str
    priority: Literal["low", "medium", "high"] = "medium"

@dataclass
class ListTasks:
    filter: Literal["all", "done", "pending"] | None = None

@dataclass
class CompleteTask:
    id: int

def parse_command(user_input: str) -> Any:
    parts = user_input.strip().lower().split()
    if not parts:
        return None

    command = parts[0]
    args = parts[1:]

    match command:
        case "add":
            title = " ".join(args[:-1]) if len(args) > 1 else args[0] if args else ""
            priority = args[-1] if args and args[-1] in {"low", "medium", "high"} else "medium"
            return AddTask(title, priority)

        case "list":
            filter_val = args[0] if args else None
            return ListTasks(filter_val if filter_val in {"all", "done", "pending"} else None)

        case "done" | "complete":
            if args and args[0].isdigit():
                return CompleteTask(int(args[0]))
            return "ID inválido"

        case "help":
            return "Comandos: add, list, done"

        case _:
            return "Comando desconhecido"
```

---

## 🧭 Boas Práticas

✅ Use `match` quando realmente melhorar a legibilidade

✅ Sempre inclua `case _:` como default

✅ Combine com `dataclasses` para estruturar dados

✅ Prefira guards simples em vez de lógica pesada dentro dos `case`

✅ Teste exaustivamente — o pattern matching pode mascarar erros de tipo

```python
case Point(x, y) if is_origin(x, y):
    print("Está na origem!")
```

---

## 🚀 Conclusão

Este desafio combina teoria e prática:

* **Teoria:** aprender e aplicar o `match / case` com padrões diferentes
* **Prática:** construir um mini interpretador matemático
* **Benefício:** consolidar o entendimento sobre pattern matching no Python moderno

