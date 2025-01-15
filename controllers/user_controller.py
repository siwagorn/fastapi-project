from config.database import DatabaseConfig
from models.user_model import User,UserCreate
import random

class UserController:
    
    @staticmethod
    def create_user(name: str, email: str):
        
        # Generate a random vector
        # random_vector = [random.uniform(0.0, 1.0) for _ in range(vector_length)]
        
        connection = DatabaseConfig.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING user_id",
                (name, email)
            )
            connection.commit()
            return cursor.fetchone()[0]
        finally:
            cursor.close()
            DatabaseConfig.return_connection(connection)
    
    @staticmethod
    def get_all():
        connection = DatabaseConfig.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT user_id, name, email FROM users")
            users = [
                User(user_id=row[0], name=row[1], email=row[2])
                for row in cursor.fetchall()
            ]
            return users
        finally:
            cursor.close()
            DatabaseConfig.return_connection(connection)
            
    @staticmethod
    def get_by_id(user_id):
        connection = DatabaseConfig.get_connection()
        cursor = connection.cursor()
        try:
            q = 'SELECT user_id, name, email FROM users WHERE user_id = %s;'
            cursor.execute(q,user_id)
            return cursor.fetchone()
        finally:
            cursor.close()
            DatabaseConfig.return_connection(connection)
            
    @staticmethod
    def update(user_id,name=None,email=None):
        connection = DatabaseConfig.get_connection()
        cursor = connection.cursor()
        try:
            q = """UPDATE users
                SET name = %s,
                email = %s
                WHERE user_id = %s;"""
            cursor.execute(q,(name,email,user_id))
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            DatabaseConfig.return_connection(connection)
    
    @staticmethod
    def delete(user_id):
        connection = DatabaseConfig.get_connection()
        cursor = connection.cursor()
        try:
            q = """DELETE FROM users
                WHERE user_id = %s;"""
            cursor.execute(q,user_id)
            connection.commit()
            return cursor.rowcount > 0
        finally:
            cursor.close()
            DatabaseConfig.return_connection(connection)