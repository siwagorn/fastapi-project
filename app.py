from controllers.user_controller import UserController
from models.user_model import User
from config.database import DatabaseConfig
from config.config import DATABASE_CONFIG
import random

def main():
    # Initialize database connection
    DatabaseConfig.initialize(DATABASE_CONFIG)
    
    user_controller = UserController()
    
    # Add a new user
    new_user_id = user_controller.create_user("s", "aaa@example.com")
    print(f"New user added with ID: {new_user_id}")

    # # Get all users
    # users = user_controller.get_all_users()
    # for user in users:
    #     print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    
    # # Get by id
    # users = user_controller.get_by_id('1')
    # print(users)
    
    # # Update
    # update_users = user_controller.update(1,name='Siwakorn',email='siwakorn@raxinterdiag.com')
    # print(f"Update ,{update_users}")
    
    # # Delete
    # delete_users = user_controller.delete('2')
    # print(f"Delete ,{delete_users}")
        
    # # Test fetching users
    # users = UserController.get_users()
    
    # print("Users:", users)

    # Close all connections
    DatabaseConfig.close_all_connections()

if __name__ == "__main__":
    main()