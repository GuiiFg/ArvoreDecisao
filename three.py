from multiprocessing.spawn import import_main_path


import pandas as pd

class Node():

    def __init__(self) -> None:
        
        self.__logic = None
        self.__father = None
        self.__childrens = []


class DecisionThree:

    def __init__(self, database : pd.DataFrame, objetiveColumn = None) -> None:
        
        self.__head = None
        self.__database = database
        self.__objetiveColumn = objetiveColumn if objetiveColumn != None else database.columns[-1]
        self.__usedColunmsList = []
        self.__CarregarNodesLogico()

    def __CarregarNodesLogico(self, father = None, logicNode = None):

        if father == None:
            # Inserir na rais 

            column = self.__CalcularPoderDescriminante()

            node = Node()

            values = list(set(self.__database[f"{column}"]))

            for value in 


            pass
        else:
            # inserir como filho
            pass

    def __CalcularPoderDescriminante(self):

        database = self.__database

        # Dropa as colunas usadas
        for column in self.__usedColunmsList:
            database.drop(columns=column, inplace=True)

        objetivo = self.__objetiveColumn

        # seleciona os valores da coluna objetivo
        objectiveValues = list(set(database[f"{objetivo}"]))

        alldatasNumber = database.shape[0]

        poderDescriminante = {}

        # Calcula o poder
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

        colunaMaiorDescriminancia = ""
        power = 0
        for key in poderDescriminante.keys():
            if poderDescriminante[f"{key}"] > power:
                power = poderDescriminante[f"{key}"]
                colunaMaiorDescriminancia = key

        return colunaMaiorDescriminancia
