# arvore de decicso 

"""
TRATAMENTO DO ARQUIVO DTree PARA CSV

with open("base fortinite - para Dtree.txt") as arquivo:
    text = arquivo.read()

text = text.replace("A: ", "")
text = text.replace("T: ", "")
text = text.replace(";", "")
text = text.replace(",", ";")

with open("databaseFortinite.csv", "w") as csv:
    csv.write(text)"""

import pandas as pd

def CalcularPoderDescriminante(database:pd.DataFrame, objetivo):

    objectiveValues = list(set(database[f"{objetivo}"]))

    alldatasNumber = database.shape[0]

    poderDescriminante = {}

    for colunm in database.columns:
        if colunm == objetivo:
            continue

        values = list(set(database[f"{colunm}"]))

        dictofvalues = {}

        for objectiveValue in objectiveValues:

            databaseObjective = database[database[f"{objetivo}"] == objectiveValue]

            for value in values:
                if value not in dictofvalues.keys():
                    dictofvalues[f"{value}"] = [list(databaseObjective[f"{colunm}"]).count(value)]
                else:
                    dictofvalues[f"{value}"].append(list(databaseObjective[f"{colunm}"]).count(value))

        maxValues = []

        for key in dictofvalues:
            maxValues.append(max(dictofvalues[f"{key}"]))

        
        poderDescriminante[f"{colunm}"] = sum(maxValues) / alldatasNumber

    return poderDescriminante


def MontarDecisao(database:pd.DataFrame, objetivo:str):
    poderDestrimante : dict = CalcularPoderDescriminante(database, objetivo)

    colunaMaiorDescriminancia = ""
    power = 0
    for key in poderDestrimante.keys():
        if poderDestrimante[f"{key}"] > power:
            power = poderDestrimante[f"{key}"]
            colunaMaiorDescriminancia = key

    print(poderDestrimante)
    print(colunaMaiorDescriminancia)

    print(list(set(database[f"{colunaMaiorDescriminancia}"])))




colunaClasses = "desempenho_final"
database = pd.read_csv("databaseFortinite.csv", ";")

MontarArvoreDecisao(database, colunaClasses)
