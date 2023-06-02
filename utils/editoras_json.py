import json
from pathlib import Path
from model.editora import Editora

def caminho_completo(nome_arquivo_json) -> str:
    return f'{str(Path().absolute())}/uploads/{nome_arquivo_json}.json'


def ler_json(nome_arquivo_json) -> list[dict]:
    with open(caminho_completo(nome_arquivo_json)) as arquivo_json:
        dados = json.load(arquivo_json)
        return dados


def ler_json_gera_lista_de_editoras(nome_arquivo_json) -> list[Editora]:
    with open(caminho_completo(nome_arquivo_json)) as arquivo_json:
        dados = json.load(arquivo_json)
        lista_editoras = list()
        for dicionario in dados:
            editora = Editora(dicionario['nome'], dicionario['endereco'], dicionario['telefone'])
            lista_editoras.append(editora)
        return lista_editoras


def criando_json_usando_lista_de_dict(lista_dict, nome_novo_arquivo) -> None:
    with open(caminho_completo(nome_novo_arquivo), mode='w') as novo_json:
        json.dump(lista_dict, novo_json, ensure_ascii=False, indent=4)
    
    print('Arquivo criado com sucesso!')


def criando_json_usando_lista_de_editoras(lista_editoras: list[Editora], nome_novo_arquivo) -> None:
    with open(caminho_completo(nome_novo_arquivo), mode='w') as novo_json:
        editoras_dict = list()
        for editora in lista_editoras:
            editoras_dict.append(editora.dump())
        json.dump(editoras_dict, novo_json, ensure_ascii=False, indent=4)
    
    print('Arquivo criado com sucesso!')