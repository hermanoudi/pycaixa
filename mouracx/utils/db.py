from sqlmodel import Session, select, create_engine
from mouracx.models import Account, Category, TransactionCategory, Transaction
from mouracx.settings import SQL_CON_STRING
from typing import List

engine = create_engine(SQL_CON_STRING, echo=False)

# account
def save_account(session: Session, instance: Account):
    """Saves account data to database"""
    session.add(instance)
    return instance


def list_accounts() -> List[Account]:
    with Session(engine) as session:
        sql = select(Account)
        accounts = session.exec(sql).all()
    return accounts


def find_account_by_name(name) -> Account:
    with Session(engine) as session:
        sql = select(Account).where(Account.account_name == name)
        return session.exec(sql).first()



# category
def save_category(session: Session, instance: Category):
    """saves category data to database"""
    session.add(instance)
    return instance


def list_categories() -> List[Category]:
    with Session(engine) as session:
        sql = select(Category)
        category = session.exec(sql).all()
    return category


def find_category_by_name(name) -> Account:
    with Session(engine) as session:
        sql = select(Category).where(Category.category_name == name)
        return session.exec(sql).first()

# transaction
def save_transaction(session: Session, instance: Transaction):
    """saves transaction data to database"""
    session.add(instance)
    return instance


def list_transactions() -> List[Transaction]:
    with Session(engine) as session:
        sql = select(Transaction)
        transaction = session.exec(sql).all()
    return transaction


def save_transaction_category(session: Session, transaction_category: TransactionCategory):
    """saves linked table to transaction and category"""
    session.add(transaction_category)
    return transaction_category
