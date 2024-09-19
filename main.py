from fastapi import FastAPI
from routers import mybase_routers

app = FastAPI()

# Include routers for different parts of the system
app.include_router(mybase_routers.router)
#app.include_router(financial.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
