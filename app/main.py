from fastapi import FastAPI

app = FastAPI(title="Commute Expense Tracker")

@app.get("/health")
def health_check():
    return{"status": "ok"}