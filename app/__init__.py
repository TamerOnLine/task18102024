 
from fastapi import FastAPI

# Application configuration
app = FastAPI(
    title="My FastAPI Application",
    description="An API built with FastAPI and Docker.",
    version="1.0.0"
)

# Import routers or additional modules if needed
# from . import routes  # Example: import routes if you have a routes.py file
