# ⚡ Distributed Cache Lab

Implementação de um **cache LRU (Least Recently Used)** em Python, criada para estudar estruturas de dados, gerenciamento de memória em cache e análise de desempenho.

> **Nota:** apesar do nome do repositório, esta implementação é um cache local em memória. Ela serve como laboratório para conceitos que também aparecem em sistemas distribuídos.

## 🎯 Objetivos

- Implementar a política de descarte **LRU**.
- Entender como uma estrutura de cache mantém a ordem de uso.
- Trabalhar com operações eficientes de leitura e escrita.
- Praticar testes automatizados e organização de projeto Python.

## ✨ Funcionalidades

- Capacidade máxima configurável.
- Inserção e atualização de valores.
- Recuperação de valores com atualização da ordem de uso.
- Remoção automática do item menos recentemente utilizado.
- Validação da capacidade.
- Testes automatizados com `unittest`.

## 🧠 Como funciona

O cache utiliza `collections.OrderedDict`:

1. Cada chave é associada a um valor.
2. Quando uma chave é acessada, ela passa para o final da estrutura.
3. Quando a capacidade é excedida, o primeiro item é removido.
4. O primeiro item representa o menos recentemente utilizado.

### Complexidade

As operações principais são realizadas em **O(1) amortizado**:

| Operação | Complexidade |
|---|---:|
| Inserir | O(1) |
| Atualizar | O(1) |
| Obter | O(1) |
| Remover o LRU | O(1) |

## 📁 Estrutura

```text
distributed-cache-lab/
├── tests/
│   └── test_lru_cache.py
├── .gitignore
├── LICENSE
├── README.md
└── lru_cache.py
```

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/marcellabongiolo/distributed-cache-lab.git
cd distributed-cache-lab
```

### 2. Executar a demonstração

```bash
python lru_cache.py
```

### 3. Executar os testes

```bash
python -m unittest discover -s tests -v
```

O projeto utiliza apenas a **biblioteca padrão do Python**, portanto não há dependências externas para instalar.

## 🧪 Conceitos praticados

- Estruturas de dados
- Cache e política LRU
- `OrderedDict`
- Complexidade de algoritmos
- Programação orientada a objetos
- Validação de entradas
- Testes automatizados
- Organização de projetos Python

## 👩‍💻 Autora

**Marcella Bongiolo**

[GitHub](https://github.com/marcellabongiolo) · [LinkedIn](https://linkedin.com/in/marcellabongiolo)

## 📄 Licença

Este projeto está disponível sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE).
