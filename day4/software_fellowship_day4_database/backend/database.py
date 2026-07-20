from sqlmodel import SQLModel, create_engine, Session
from models import Expense

engine = create_engine("sqlite:///./expenses.db", connect_args={"check_same_thread": False}) # connects Python with sqlite database
SQLModel.metadata.create_all(engine) # this creates the tables with model (we made one with SQLModel : Expense)

db = Session(engine) # this allow to use the database 
