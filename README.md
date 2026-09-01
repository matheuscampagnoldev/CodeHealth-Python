# 🩺 CodeHealth

![Python](https://img.shields.io/badge/python-3.x-blue) ![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow) ![Versão](https://img.shields.io/badge/versão-1.0-blue) ![License](https://img.shields.io/badge/licença-MIT-green)

Ferramenta de linha de comando desenvolvida em Python, que analisa um arquivo `.py` e gera um diagnóstico de qualidade de código: linhas longas, funções gigantes, contagem de classes, falta de comentários e uma nota final de saúde do código — tudo apresentado em painéis coloridos no terminal com a biblioteca `Rich`.

O projeto foi construído do zero como exercício prático dos fundamentos da linguagem — leitura e manipulação de texto, funções, contagem e lógica condicional — aplicados a um problema real do dia a dia de quem programa: entender rapidamente a saúde de um arquivo de código.

## 🖼️ Demonstração

<img width="732" height="832" alt="image" src="https://github.com/user-attachments/assets/55de5d4f-180f-4531-8bc4-89773d32231e" />


## ✨ Funcionalidades

- ✅ Análise de um arquivo `.py` a partir do caminho informado no terminal
- ✅ Contagem de linhas de código (ignorando linhas em branco)
- ✅ Contagem de linhas de comentário (`#`)
- ✅ Cálculo da proporção comentário/código
- ✅ Contagem de funções (`def`)
- ✅ Contagem de classes (`class`)
- ✅ Sinalização de funções longas (mais de 20 linhas) como candidatas a refatoração
- ✅ Sinalização de linhas longas, com indicação de quais linhas ultrapassam 79 caracteres (padrão PEP8)
- ✅ Nota final de saúde do código, de 0 a 10, baseada no conjunto das métricas
- ✅ Interface no terminal com painéis (`Panel`) da biblioteca `Rich`

## 🛠️ Tecnologias e conceitos aplicados

| Categoria | Detalhes |
|---|---|
| Linguagem | Python 3 |
| Bibliotecas | [Rich](https://github.com/Textualize/rich) — `Console` e `Panel` para exibição no terminal |
| Estruturas de dados | Listas, dicionários, strings e contadores |
| Organização | Separação em `main.py`, `exibicoes.py` e `funcoes.py` |
| Boas práticas | Leitura segura de arquivo, contagem e cálculo de métricas |
| Persistência | Nenhuma — cada execução analisa o arquivo na hora, sem salvar histórico |

## 📁 Estrutura do projeto

```
CodeHealth-Python/
├── main.py           # Ponto de entrada: orquestra o fluxo do programa
├── exibicoes.py       # Interface: menu, títulos e exibição dos resultados no terminal (Rich)
├── funcoes.py         # Lógica: contagem de linhas, comentários, funções, classes e cálculo da nota
├── amostras/           # Arquivos .py de exemplo para testar a ferramenta
├── LICENSE
└── README.md
```

## 🚀 Como executar

Pré-requisito: ter o Python 3 instalado.

```bash
# Clone o repositório
git clone https://github.com/matheuscampagnoldev/codehealth-python.git

# Acesse a pasta do projeto
cd codehealth-python

# Instale a dependência (Rich)
pip install rich

# Execute o programa apontando para o arquivo que deseja analisar
python main.py caminho/para/arquivo.py
```

## 🖥️ Exemplo de saída

```
┌──────────── CODE HEALTH ────────────┐
│              teste.py               │
└─────────────────────────────────────┘

┌────────── ARQUIVO SELECIONADO ───────┐
│ Arquivo: teste.py                    │
└──────────────────────────────────────┘

┌────────── INFORMAÇÕES DO CÓDIGO ──────┐
│ Linhas do código: 273                 │
│ Comentários: 3                        │
│ Proporção: 1.10%                      │
│ Funções: 24                           │
│ Classes: 0                            │
│ Funções longas: 5                     │
│ Linhas longas: 3                      │
└───────────────────────────────────────┘

┌───────────── FUNÇÕES LONGAS ──────────┐
│ - ler_texto -> 24                     │
│ - cadastro -> 46                      │
│ - saidaproduto -> 26                  │
│ - remover_produto -> 26               │
│ - relatorio -> 68                     │
└───────────────────────────────────────┘

┌───────────── LINHAS LONGAS ───────────┐
│ - Linha 12                            │
│ - Linha 27                            │
│ - Linha 43                            │
└───────────────────────────────────────┘

┌───────────────── RESULTADO ──────────┐
│ SAÚDE DO CÓDIGO: 5/1                 │
└──────────────────────────────────────┘
```

## 🗺️ Roadmap

O projeto está em evolução contínua. Próximas versões planejadas:

- **v2.0 — Análise mais profunda**
  - Detecção de complexidade ciclomática (mede o quão aninhada/emaranhada uma função está)
  - Detecção de código duplicado (blocos de linhas repetidos no mesmo arquivo)
  - Detecção de nomes de variáveis ruins (nomes muito curtos ou genéricos)
  - Detecção de imports não usados
  - Sugestões automáticas de refatoração com base nos problemas encontrados

- **v3.0 — Comparação e histórico**
  - Salvar cada análise com data/hora em JSON
  - Comparar a análise atual com análises anteriores do mesmo arquivo
  - Gerar gráfico de evolução da nota (`matplotlib`)
  - Analisar uma pasta inteira / múltiplos arquivos de uma vez
  - Interface gráfica
  - Reestruturação com orientação a objetos

## 📚 Aprendizados

Este projeto foi desenvolvido como parte da minha jornada de estudos em Python, com foco em consolidar fundamentos antes de avançar para tópicos como orientação a objetos e persistência de dados. A ideia foi priorizar a construção de algo funcional e útil usando apenas os conceitos essenciais da linguagem, incorporando bibliotecas de terceiros (como o Rich) conforme o projeto evoluiu.

## 👤 Autor

**Matheus Zuim Campagnol**
Estudante de Engenharia de Software | Foco em Python

## ⭐ Curtiu o projeto?

Se este projeto te ajudou de alguma forma ou você gostou da ideia, deixe uma estrela no repositório!
