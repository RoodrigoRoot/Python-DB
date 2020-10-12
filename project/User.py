import psycopg2
from Db import *
import getpass
import hashlib

class User:
    def __init__(self, name, age, password):
        self.__name = name
        self.__age = age
        self.__password = password
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
    
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
    
    name = property(get_name, set_name)
    age = property(get_age, set_age)
    password = property(get_password, set_password)


class UserMethods:

    @classmethod
    def create_user(cls):
        name = input("Nombre: ")
        age = int(input("Edad: "))
        password = getpass.getpass("Contraseña: ")
        user = User(name, age, password)
        return user


    @classmethod
    def set_password(cls, password):
        password = hashlib.sha256(password.encode()).hexdigest()
        return password

    

class UserDB:


    @classmethod
    def insert_user(cls, user, cursor):
        name = user.name
        age = user.age
        password = UserMethods.set_password(user.password)
        query = "INSERT INTO users(name, age, password) VALUES(%s, %s, %s)"
        cursor.execute(query, (name, age, password))
        cursor.close()


    @classmethod
    def delete_user(cls, cursor):
        id_user = int(input("Ingrese el id a eliminar: "))
        query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id_user,))
        user = cursor.fetchone()
        if user:
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id_user,))
            print("Usuario Eliminado")
        else:
            print("No existe un usuario con ese id")


    @classmethod
    def list_users(cls, cursor):
        query = "SELECT id, name, age FROM users;"
        cursor.execute(query)
        print("-----------Usuarios Regitrados-----------")
        for id, name, age in cursor.fetchall():
            print("ID: {} - Nombre: {} - Edad: {}".format(id, name, age))
        print("-----------------------------------------")
    

    @classmethod
    def update_user(cls, cursor):
        id_user = int(input("Ingrese el id del usuario a modificar: "))
        query = "SELECT id FROM users WHERE id = {}".format(id_user)
        cursor.execute(query)
        user_exists = cursor.fetchone()
        name = input("Ingrese el nuevo nombre: ")
        age = int(input("Ingrese la nueva edad: "))
        password = UserMethods.set_password(getpass.getpass("Ingrese la nueva contraseña"))

        if user_exists:
            query = "UPDATE users SET name='{}', age={}, password='{}' WHERE id = {}".format(name, age, password, id_user)
            cursor.execute(query)
        else:
            print("El id proporcionado no existe")
