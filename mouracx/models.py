from datetime import date
from typing import Optional, List
from pydantic import condecimal

from sqlmodel import Relationship, SQLModel, Field



# Modelo de Relação entre Transações e Categorias (opcional)
class TransactionCategory(SQLModel, table=True):
    transaction_id: int = Field(foreign_key="transaction.transaction_id", primary_key=True)
    category_id: int = Field(foreign_key="category.category_id", primary_key=True)

# Modelo de Conta
class Account(SQLModel, table=True):
    account_id: Optional[int] = Field(default=None, primary_key=True)
    account_name: str
    account_type: str
    currency: str

    transaction: "Transaction" = Relationship(back_populates="account")

    def __str__(self) -> str:
        return f"{self.account_id} - {self.account_name} - {self.account_type} - {self.currency}"


# Modelo de Categoria
class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(default=None, primary_key=True)
    category_name: str

# Modelo de Transação
class Transaction(SQLModel, table=True):
    transaction_id: Optional[int] = Field(default=None, primary_key=True)
    account_id: int = Field(foreign_key="account.account_id")
    transaction_date: date
    description: str
    amount: condecimal(decimal_places=3) = Field(default=0)
    debit_credit: str
    balance: condecimal(decimal_places=3) = Field(default=0)

    account: Account = Relationship(back_populates="transaction")





