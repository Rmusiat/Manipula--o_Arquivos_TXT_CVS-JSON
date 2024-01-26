# Importar o mdulo CSV

import csv

# Criar um arquivo CSV com as funções WRITER e WRITEROW

with open('Arquivos/nomes.csv','w+',newline="", encoding='utf-8') as fcsv:
        escreve = csv.writer(fcsv,delimiter=',')
        escreve.writerow(('Nome',"Sobrenome","Idade"))
        escreve.writerow(('João',"Ricardo","39"))
        escreve.writerow(('Juca',"Souza","34"))
        escreve.writerow(('Alberto',"Cunha","12"))

# Ler o arquivo CSV criado

with open('Arquivos/nomes.csv','r') as fcsv:
    ler = csv.reader(fcsv)
    lista1 = list(ler)
    print(lista1)

    for c in lista1:
        print(c)

# Transformar s saida em dicionario com o metodo DICTREADER

with open('Arquivos/nomes.csv','r') as fcsv2:
    ler_dic = csv.DictReader(fcsv2)

# Iterar os valores

    for d in ler_dic:
        print(d["Nome"])
