from sqlmodel import SQLModel, Field

class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category: str
    description: str = ""
    amount: float = Field(gt=0)
