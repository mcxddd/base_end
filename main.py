# base_end/main.py
from fastapi import FastAPI
from routers import mybaseweb

app = FastAPI()

# Include routers for different parts of the system
app.include_router(mybaseweb.router)
#app.include_router(financial.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
