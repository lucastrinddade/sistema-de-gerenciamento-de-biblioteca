# Sistema de Gerenciamento de Biblioteca

Sistema desenvolvido em Python utilizando Programação Orientada a Objetos (POO) para gerenciamento de uma biblioteca.

---

# Funcionalidades

O sistema permite:

* Cadastro de livros;
* Cadastro de usuários;
* Empréstimo de livros;
* Devolução de livros;
* Relatório de livros emprestados;
* Exibição do status de todos os livros.

---

# Regras do Sistema

* Um livro não pode ser emprestado se já estiver emprestado;
* Ao devolver um livro, ele volta ao status disponível;
* O sistema exibe todos os livros cadastrados ao finalizar.

---

# Tecnologias Utilizadas

* Python
* Programação Orientada a Objetos (POO)

---

# Estrutura do Projeto

```txt
sistema-biblioteca/
│
├── main.py
├── README.md
│
└── classes/
    ├── livro.py
    ├── usuario.py
    └── biblioteca.py
```

---

# Classes Utilizadas

## Classe Livro

Responsável por armazenar:

* título;
* autor;
* status do empréstimo.

### Métodos

* emprestar()
* devolver()
* status()

---

## Classe Usuario

Responsável pelos dados do usuário.

### Atributos

* nome

---

## Classe Biblioteca

Responsável pelo gerenciamento geral do sistema.

### Funcionalidades

* cadastrar livros;
* cadastrar usuários;
* emprestar livros;
* devolver livros;
* emitir relatórios;
* listar livros.

---

# Menu do Sistema

O sistema possui um menu interativo no console:

```txt
===== SISTEMA DE BIBLIOTECA =====

1 - Cadastrar livro
2 - Cadastrar usuário
3 - Emprestar livro
4 - Devolver livro
5 - Relatório de livros emprestados
6 - Listar todos os livros
0 - Sair
```

---

# Como Executar

## 1. Instalar o Python

Download:
https://www.python.org/

---

## 2. Abrir o terminal na pasta do projeto

---

## 3. Executar o sistema

```bash
python main.py
```

---

# Exemplo de Funcionamento

## Cadastro de Livro

```txt
Título do livro: Dom Casmurro
Autor do livro: Machado de Assis
```

---

## Empréstimo

```txt
Livro 'Dom Casmurro' emprestado para Lucas.
```

---

## Tentativa de empréstimo duplicado

```txt
Livro já está emprestado.
```

---

# Relatório de Livros

```txt
===== TODOS OS LIVROS =====

Título: Dom Casmurro
Autor: Machado de Assis
Status: Emprestado
```

---

# Conclusão

O sistema de gerenciamento de biblioteca foi desenvolvido com foco em simplicidade, organização e aplicação prática de Programação Orientada a Objetos. O projeto atende todos os requisitos solicitados na atividade, permitindo gerenciamento de livros, empréstimos e devoluções através de um menu interativo no console.
