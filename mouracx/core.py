"""Core module of mouracx"""

import csv
from datetime import date
from decimal import Decimal

from pydantic import ValidationError

from mouracx.database import get_session
from mouracx.models import Account, Category, Transaction, TransactionCategory
from mouracx.utils.db import (
    find_account_by_name,
    find_category_by_name,
    save_account,
    save_category,
    save_transaction,
    save_transaction_category,
)
from mouracx.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database

    >>> len(load('assets/extrato.csv'))
    2
    """
    movements = []
    try:
        with get_session() as session:
            with open(filepath, mode="r", newline="") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    # Convertendo a data do CSV para o formato de data
                    data = date.fromisoformat(row["date_transaction"])
                    amount_transaction = Decimal(row["value_transaction"])

                    account = find_account_by_name(row["account"])
                    if account is None:
                        raise ValueError(
                            f"Account not found {row['account']}!"
                        )

                    instance = Transaction(
                        account_id=account.account_id,
                        transaction_date=data,
                        description=row["description"],
                        amount=amount_transaction,
                        debit_credit=row["debit_credit"],
                    )
                    category = find_category_by_name(row["category"])
                    if category is None:
                        raise ValueError(
                            f"Category is invalida for transaction_date {data}"
                        )

                    movement = save_transaction(session, instance)
                    session.commit()

                    transaction_category = TransactionCategory(
                        transaction_id=movement.transaction_id,
                        category_id=category.category_id,
                    )
                    save_transaction_category(session, transaction_category)

                    returndata = movement.dict(exclude={"transaction_id"})
                    movements.append(returndata)
                    print(movements)
                    session.commit()
    except FileNotFoundError as e:
        log.error(str(e))
        raise e

    return movements


# def list_movements() -> List[Movement]:
#     movements = []

#     for mov in list_all_movements():
#         returndata = mov.dict(exclude={"id"})
#         movements.append(returndata)
#     return movements


# account
def register_account(name, type, currency) -> Account:
    """Register account to manager transactions"""
    with get_session() as session:
        try:
            name_account_for_register = name
            account = get_account_by_name(str(name_account_for_register))
            if account is not None:
                raise ValueError("Account already exist!")

            instance = Account(
                account_name=name, account_type=type, currency=currency
            )
            account = save_account(session, instance)
            return_data = account.model_dump(exclude={"account_id"})
            session.commit()
            return return_data
        except ValidationError:
            log.error("Invalid type account")


def get_account_by_name(name) -> Account:
    """Find account by name"""
    if name == "" or len(name) < 3:
        raise ValueError("Name Account should be filled!")
    account = find_account_by_name(name)
    return account


# Category
def add_category(name) -> Category:
    """Register category to transactions"""
    with get_session() as session:
        name_category_for_register = name
        category = find_category_by_name(str(name_category_for_register))
        if category is not None:
            raise ValueError("Category already exist!")

        instance = Category(category_name=name)
        category = save_category(session, instance)
        return_data = category.dict(exclude={"category_id"})
        session.commit()
        return return_data


# Transaction
def add_transaction(
    account_name,
    date_transaction,
    category_name,
    description,
    value_transction,
    debit_credit,
    balance,
) -> Transaction:
    """Save transaction to database"""
    with get_session() as session:
        account = find_account_by_name(account_name)

        if account is None:
            raise ValueError("Account is invalid!")

        category = find_category_by_name(category_name)
        if category is None:
            raise ValueError("Category is invalid!")
        # TODO: arrumar uma forma de não perder o balance
        # para evitar concorrencia
        instance = Transaction(
            account_id=account.account_id,
            transaction_date=date_transaction,
            description=description,
            amount=Decimal(value_transction),
            debit_credit=debit_credit,
            balance=Decimal(balance),
        )
        transaction = save_transaction(session, instance)
        session.commit()

        transaction_category = TransactionCategory(
            transaction_id=transaction.transaction_id,
            category_id=category.category_id,
        )
        save_transaction_category(session, transaction_category)

        return_data = transaction.dict(exclude={"transaction_id"})
        session.commit()
        return return_data
