
import funcoes
from rich.console import Console
from rich.panel import Panel

console = Console(markup=False)


def titulo(n):
    console.print(
        Panel(
            n,
            title='CODE HEALTH',
            border_style='blue',
            expand=False
        )
    )


def menu():
    while True:
        caminho_arquivo = input(
            'Digite o caminho do arquivo .py: '
        ).strip()

        if caminho_arquivo[-3:].lower() == '.py':
            try:
                with open(caminho_arquivo, 'r', encoding='utf-8'):
                    return caminho_arquivo

            except FileNotFoundError:
                console.print('O arquivo não foi encontrado.')

            except PermissionError:
                console.print('Não tenho permissão para lê-lo.')

            except IsADirectoryError:
                console.print(
                    'Você passou o caminho de uma pasta em vez de um arquivo.'
                )

            except UnicodeDecodeError:
                console.print(
                    'O arquivo existe e foi aberto, mas o Python não '
                    'consegue interpretar o conteúdo como texto com '
                    'aquela codificação.'
                )

        elif caminho_arquivo == '':
            console.print('Digite um caminho válido.')

        else:
            console.print('O arquivo precisa ser .py.')


def arquivo_selecionado(n):
    console.print(
        Panel(
            f'Arquivo: {n}',
            title='ARQUIVO SELECIONADO',
            border_style='green',
            expand=False
        )
    )


def informacoes(n):
    linhas = funcoes.contar_linhas(n)
    comentarios = funcoes.contador_comentario(n)
    proporcao = funcoes.proporcao_comentarios(n)
    quantidade_funcoes = funcoes.contador_funcoes(n)

    funcoes_longas = funcoes.funcoes_longas(n)
    linhas_longas = funcoes.linhas_longas(n)

    classes = funcoes.contar_classes(n)

    texto = (
        f'Linhas do código: {linhas}\n'
        f'Comentários: {comentarios}\n'
        f'Proporção: {proporcao:.2f}%\n'
        f'Funções: {quantidade_funcoes}\n'
        f'Classes: {classes}\n'
        f'Funções longas: {len(funcoes_longas)}\n'
        f'Linhas longas: {len(linhas_longas)}'
    )

    console.print(
        Panel(
            texto,
            title='INFORMAÇÕES DO CÓDIGO',
            border_style='cyan',
            expand=False
        )
    )

    if funcoes_longas:
        texto_funcoes = '\n'.join(
            f'- {funcao}' for funcao in funcoes_longas
        )

        console.print(
            Panel(
                texto_funcoes,
                title='FUNÇÕES LONGAS',
                border_style='red',
                expand=False
            )
        )

    if linhas_longas:
        texto_linhas = '\n'.join(
            f'- Linha {linha}' for linha in linhas_longas
        )

        console.print(
            Panel(
                texto_linhas,
                title='LINHAS LONGAS',
                border_style='red',
                expand=False
            )
        )


def mostrarnota(n):
    linhas = funcoes.contar_linhas(n)
    comentarios = funcoes.contador_comentario(n)

    if linhas == 0 and comentarios == 0:
        mensagem = (
            'SAÚDE DO CÓDIGO: 0/0\n'
            'O seu programa não tem linhas de código.'
        )

    elif comentarios != 0 and linhas == 0:
        mensagem = (
            'SAÚDE DO CÓDIGO: 0/0\n'
            'O seu programa tem apenas linhas de comentários.'
        )

    else:
        mensagem = (
            f'SAÚDE DO CÓDIGO: '
            f'{funcoes.nota_programa(n)}/10'
        )

    console.print(
        Panel(
            mensagem,
            title='RESULTADO',
            border_style='yellow',
            expand=False
        )
    )