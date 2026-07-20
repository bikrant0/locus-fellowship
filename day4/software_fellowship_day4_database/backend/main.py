from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import select

from database import db
from models import Expense

app = FastAPI(title="Expense Tracker API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Welcome to the Expense Tracker API!"}


@app.get("/expenses", response_model=list[Expense])
def get_expenses():
    return db.exec(select(Expense)).all()


@app.post("/expenses", response_model=Expense)
def add_expense(expense: Expense):#get data as expense table with the Expense model
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    expense = db.get(Expense, expense_id)

    if not expense:
        raise HTTPException(status_code=404, detail="Expense not found")

    db.delete(expense)
    db.commit()

    return {"message": "deleted"}

## Lab classwork
# Make endpoint to update the product

