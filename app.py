from controllers.user_controller import UserController
from config.database import Database
from config.config import DATABASE_CONFIG

def main():
    # Initialize database connection
    Database.initialize(DATABASE_CONFIG)

    # Test fetching users
    users = UserController.get_users()
    
    print("Users:", users)

    # Close all connections
    Database.close_all_connections()

if __name__ == "__main__":
    main()