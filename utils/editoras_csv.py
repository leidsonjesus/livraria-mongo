import csv
from model.editora import Editora
from pprint import pprint
from pathlib import Path


def caminho_completo(nome_arquivo_csv) -> str:
    return f'{str(Path().absolute())}/uploads/{nome_arquivo_csv}.csv'


def ler_csv(nome_arquivo_csv) -> list:
    with open(caminho_completo(nome_arquivo_csv), encoding='utf-8') as arquivo_csv:
        lista_csv = list()
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        for linha in csv_reader:
            lista_csv.append(linha)
        return lista_csv


def ler_csv_e_cria_uma_lista_de_editoras(nome_arquivo_csv) -> list[Editora]:
    with open(caminho_completo(nome_arquivo_csv), encoding='utf-8') as arquivo_csv:
        csv_reader = csv.reader(arquivo_csv, delimiter=',')
        lista_de_editoras = list()

        quantidade_de_linhas = 0
        for item in csv_reader:
            if quantidade_de_linhas == 0:
                quantidade_de_linhas += 1
            else:
                editora = Editora(item[0], item[1], item[2])
                lista_de_editoras.append(editora)
        return lista_de_editoras


def ler_csv_e_gera_uma_lista_de_dict(nome_arquivo_csv) -> list[dict]:
    with open(caminho_completo(nome_arquivo_csv), encoding='utf-8') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_dict = list()
        for dicionario in csv_reader:
            lista_dict.append(dicionario)
        return lista_dict
    

def ler_csv_e_gera_uma_lista_de_editoras_de_um_dict(nome_arquivo_csv) -> list[Editora]:
    with open(caminho_completo(nome_arquivo_csv), encoding='utf-8') as arquivo_csv:
        csv_reader = csv.DictReader(arquivo_csv, delimiter=',')
        lista_de_editoras = list()
        for dicionario in csv_reader:
            editora = Editora(dicionario['nome'], dicionario['endereco'], dicionario['telefone'])
            lista_de_editoras.append(editora)
        return lista_de_editoras


def criando_csv_usando_lista(lista: list, nome_novo_csv) -> None:
    with open(caminho_completo(nome_novo_csv), mode='w', encoding='utf-8') as novo_csv:
        escritor = csv.writer(novo_csv)
        escritor.writerow(lista[0])
        escritor.writerows(lista[1:])
        print('Arquivo criado com sucesso!')


def criando_csv_usando_lista_de_editoras(lista_editoras: list[Editora], nome_novo_csv) -> None:
    with open(caminho_completo(nome_novo_csv), mode='w', encoding='utf-8') as novo_csv:
        escritor = csv.writer(novo_csv)
        escritor.writerow(['nome', 'endereco', 'telefone'])
        for editora in lista_editoras:
            escritor.writerow([editora.nome, editora.endereco, editora.telefone])
    print('Arquivo criado com sucesso!')