## importando 'mysql.connector' como mysql para conveniencia
import mysql.connector as mysql

def return_all_animals():
    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "brzPWD@15",
        database = "test"
    )
    ## Criando instancia da classe 'cursor' que é usada para executar comandos sql em Python
    cursor = db.cursor()
    ## Definindo a consulta
    query = "SELECT * FROM animais order by id"
    ## Coletando resultados da tabela
    cursor.execute(query)
    ## Coletando todos os dados do cursor, por default retorna tupla
    records = cursor.fetchall()
    #Transformando valores em lista para manipulação
    li = [x[0] for x in records]
    
    return li

# busca binaria Elementos = Lista, Value = valor a encontrar, Left = id inicial, Right = id final
def binary_search(elements, value, left, right):
    if left <= right:
        middle = (left + right) // 2
        if elements[middle] == value:
            return elements[middle]
        if elements[middle] < value:
            return binary_search(elements, value, middle + 1, right)
        elif elements[middle] > value:
            return binary_search(elements, value, left, middle - 1)
    return "Not found!"



#Lista de ids dos animais
values = return_all_animals()


#Encontrando a partir do id 1 até o ultimo id da consulta
found = binary_search(elements=values,value=3,left=1,right=len(values))

##Mostra id do animal encontrado
print(values[found-1])