from typing import Union
from fastapi import FastAPI
from services.user_service import router
from config.database import DatabaseConfig
from config.config import DATABASE_CONFIG

# Create FastAPI instance
app = FastAPI()

# Initialize the database connection pool on startup
@app.on_event("startup")
async def startup_event():
    try:
        DatabaseConfig.initialize(DATABASE_CONFIG)
        print("Database connection pool initialized successfully.")
    except Exception as e:
        print(f"Error initializing the database connection pool: {e}")
        raise

# Close all database connections on shutdown
@app.on_event("shutdown")
async def shutdown_event():
    try:
        DatabaseConfig.close_all_connections()
        print("All database connections closed successfully.")
    except Exception as e:
        print(f"Error closing the database connections: {e}")
        raise


# Include the router
app.include_router(router, prefix="/users", tags=["Users"])

# Optional root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the User API"}