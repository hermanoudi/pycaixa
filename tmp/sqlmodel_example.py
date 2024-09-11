from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select, Relationship

# we have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
import sqlmodel
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True # type: ignore
Select.inherit_cache = True # type: ignore

# Base (declarative_base)
# BaseModel (pydantic)

class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")

class Balance(SQLModel, table=True):

    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:////tmp/sqlmodel.db", echo=False)

SQLModel.metadata.create_all(bind=engine)

with Session(engine) as session:
    # person = Person(name="Hermano")
    # session.add(person)

    # person = Person(name="Dayane")
    # session.add(person)

    # session.commit()

    # SELECT FROM PERSON WHERE person.name = "Hermano"
    # sql = select(Person).where(Person.name == "Hermano")
    # results = session.exec(sql)
    # for person in results:
    #     balance = Balance(value=60, person=person)
    #     session.add(balance)
    # session.commit()

    # sql = select(Person)
    # results = session.exec(sql)
    # for person in results:
    #     print(person.name, person.balance[0].value)

    # sql = select(Balance).where(Balance.value > 3)
    # results = session.exec(sql)
    # for balance in results:
    #     print(f"{balance.person.name} tem {balance.value} pontos!")


    # Exemplo de Join
    # sql = select(Person, Balance).where(Balance.person_id == Person.id)
    # results = session.exec(sql)
    # for person, balance in results:
    #     print(person.name, balance.value)

    # Exemplo de left join
    sql = select(Person, Balance).join(Balance, isouter=True)
    results = session.exec(sql)
    for person, balance in results:
        print(person.name, balance.value)
