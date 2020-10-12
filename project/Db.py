import psycopg2


def connection():
    try:
        connection = psycopg2.connect("host='localhost' user='tester' password='123456' dbname='azul' ")    
        return connection
    except psycopg2.Error as error:
        print("Error en la Base de datos: ", error)

