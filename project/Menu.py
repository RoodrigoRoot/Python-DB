from User import *
import time

def selected_option(con, option):
    with con.cursor() as cursor:
        
        if option == 1:
            user = UserMethods.create_user()
            UserDB.insert_user(user, cursor)
            
        elif option == 2:
            UserDB.delete_user(cursor)

        elif option == 3:
            UserDB.list_users(cursor)
        elif option == 4:
            UserDB.update_user(cursor)
    
    con.commit()
    cursor.close()

def menu():
    menu = """1.-Agregar Usuario\n2.-Eliminar Usuario\n3.-Listar Usuarios\n4.-Actualizar Usuario\n5.-Salir\nOpción: """
    con = connection()
    import sys
    while True:#option != 5:   
        option = int(input(menu))
        if option == 5:
            print("\nVuelva pronto\n")
            sys.exit(1)
        selected_option(con, option)
    #con.close()

menu()