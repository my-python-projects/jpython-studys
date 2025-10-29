[🇺🇸 English](#english-version) | [🇧🇷 Português](#versão-em-português)

---

### 🛡️ English Version

---

# 🧭 Challenge: `restrict_access` Decorator (Permission Control in Functions)

## 📘 Description

This challenge aims to create a **Python decorator** called `restrict_access`, which **controls function execution** based on a user's permissions.

The decorator must:

* Receive a **list of required permissions** as an argument.
* Check if the **user passed to the function** has all the necessary permissions.
* Execute the function normally if the user has the required permissions.
* Otherwise, **display an error message** indicating access was denied.

---

## Functional Requirements

| Requirement             | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| Decorator parameters    | Accepts a list of required permissions, optional error message, and log flag |
| Permission verification | Compares the user's permissions to the required ones                         |
| Custom error message    | Allows defining a custom error message                                       |
| Optional logging        | Records access denials with timestamp and details                            |
| Metadata preservation   | Uses `@wraps` to maintain the original function's name and docstring         |
| Argument flexibility    | Works with any function that receives `user` as its first argument           |

---

## 🧬 Expected Usage Example

```python
@restrict_access(["admin", "write"])
def delete_user(user, user_id):
    print(f"User {user_id} deleted by {user['name']}")

user = {"name": "Alice", "permissions": ["admin", "write"]}
delete_user(user, 123)  # Should execute successfully

user_no_perm = {"name": "Bob", "permissions": ["read"]}
delete_user(user_no_perm, 123)  # Should fail
```

### 💡 Expected Output:

```
User 123 deleted by Alice
Access denied: insufficient permissions
```

### 📝 Log File Example:

```python
2025-10-29 10:15:23,456 - WARNING - Access denied to function 'delete_user' for user 'Bob'
```

---

## ⚙️ Instructions

1. Create a decorator function named `restrict_access` that:

   * Accepts **a list of permissions** as an argument.
   * Returns an **inner decorator** to be applied to the target function.
   * Inside the decorator, validate the user's permissions.
2. If the user has all required permissions, execute the function.
3. Otherwise, display an error message and **do not execute the function**.

---

## Applied Best Practices

* Proper use of @functools.wraps
* Three-layer decorator structure to support parameters
* Safe dictionary handling with .get()
* Logging configured via basicConfig
* Efficient permission check using set.issubset()
* Default error message handling
* Defensive and reusable coding style

---

## Technologies Used

* Python 3.8+
* Standard modules: logging, functools
* Concepts: Decorators, Higher-order functions, Closures, Sets

---

## How to Test

* Clone the repository
* Run the main script
* Check the terminal output
* Review the generated access_denied.log file

---

## 🚀 Improvement Suggestions (Future Roadmap)

| Improvement                                 | Benefit                                             |
| ------------------------------------------- | --------------------------------------------------- |
| Unit tests with `pytest`                    | Ensure production robustness                        |
| Raise custom exception (`PermissionDenied`) | Allows structured handling in APIs and applications |
| Support for flexible function signatures    | Avoid assuming `user` is the first argument         |
| Injectable logger configuration             | Avoid global `basicConfig` (better for libraries)   |
| Hierarchical permission support             | e.g., `admin` implies `write` and `read`            |
| Permission caching                          | Avoid recalculating on frequent calls               |

---

## 🧾 License

This exercise is free for educational use and part of **Intermediate Python** practice challenges.

------

### 🛡️ Versão em Português

---

# 🧭 Desafio: Decorador `restrict_access` (Controle de Permissões em Funções)

## 📘 Descrição

Este desafio tem como objetivo criar um **decorador em Python** chamado `restrict_access`, que **controla o acesso** a funções com base nas permissões de um usuário.

O decorador deve:

* Receber uma **lista de permissões necessárias** como argumento.
* Verificar se o **usuário passado como argumento da função** possui todas as permissões exigidas.
* Executar a função normalmente caso o usuário tenha as permissões.
* Caso contrário, **exibir uma mensagem de erro** informando que o acesso foi negado.

---

## Requisitos Funcionais

| Requisito | Descrição |
|---------|-----------|
| Parâmetros do decorador | Recebe uma lista de permissões obrigatórias, mensagem de erro opcional e flag de log |
| Verificação de permissão | Compara permissões do usuário com as exigidas |
| Mensagem personalizada | Permite definir texto de erro customizado |
| Logging opcional | Registra negações em arquivo com timestamp e detalhes |
| Preservação de metadados | Usa `@wraps` para manter nome e docstring da função original |
| Flexibilidade de argumentos | Funciona com qualquer função que receba `user` como primeiro argumento |

---

## 🧬 Exemplo de Uso Esperado

```python
@restrict_access(["admin", "write"])
def delete_user(user, user_id):
    print(f"Usuário {user_id} deletado por {user['name']}")

user = {"name": "Alice", "permissions": ["admin", "write"]}
delete_user(user, 123)  # Deve executar com sucesso

user_no_perm = {"name": "Bob", "permissions": ["read"]}
delete_user(user_no_perm, 123)  # Deve falhar
```

### 💡 Saída esperada:

```
Usuário 123 deletado por Alice
Acesso negado: permissões insuficientes
```

### 📝 Log em arquivo:

```python
2025-10-29 10:15:23,456 - WARNING - Acesso negado à função 'delete_user' para usuário 'Bob'
```

---

## ⚙️ Instruções

1. Crie uma função decoradora chamada `restrict_access` que:

   * Aceita **uma lista de permissões** como argumento.
   * Retorna um **decorador interno** que será aplicado à função.
   * Dentro do decorador, valide as permissões do usuário.
2. Caso o usuário possua todas as permissões, execute a função.
3. Caso contrário, mostre uma mensagem de erro e **não execute a função**.

---

## Boas Práticas Aplicadas

  * Uso correto de @functools.wraps
  * Decorador com 3 camadas para suportar parâmetros
  * Tratamento seguro de dicionários com .get()
  * Logging configurado com basicConfig
  * Uso eficiente de set.issubset() para verificação
  * Mensagem de erro com valor padrão
  * Código defensivo e reutilizável

---

## Tecnologias Utilizadas

  * Python 3.8+
  * Módulo padrão: logging, functools
  * Conceitos: Decorators, Higher-order functions, Closures, Sets

---

## Como Testar

  * Clone o repositório
  * Execute o script principal
  * Verifique a saída no terminal
  * Confira o arquivo access_denied.log gerado

---

## 🚀 Sugestões de Melhoria (Roadmap Futuro)

| Melhoria                                            | Benefício                                            |
| --------------------------------------------------- | ---------------------------------------------------- |
| Testes unitários com `pytest`                       | Garantir robustez em produção                        |
| Levantar exceção personalizada (`PermissionDenied`) | Permite tratamento estruturado em APIs e aplicações  |
| Suporte a funções com assinatura flexível           | Não assumir que `user` é o primeiro argumento        |
| Configuração de logger injetável                    | Evita `basicConfig` global (melhor para bibliotecas) |
| Suporte a permissões hierárquicas                   | Ex: `admin` implica em `write` e `read`              |
| Cache de permissões                                 | Evitar recálculo em chamadas frequentes              |


---

## 🧾 Licença

Este exercício é livre para uso educativo e faz parte de desafios de prática de **Python intermediário**.

