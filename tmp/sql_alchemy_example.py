from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


class Base:
    __allow_unmapped__ = True


Base = declarative_base(cls=Base)


class Person(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    def __str__(self):
        return (self.name.upper())


class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)

    person_id = Column(Integer, ForeignKey(Person.id))

    person = relationship('Person', foreign_keys='Balance.person_id')


engine = create_engine("sqlite:////tmp/database.db")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

movement = Person(name="Hermano")
session.add(movement)

# results = session.query(Movement).filter(Movement.name == "Despesa Teste 2")
# results = session.query(Person)
# for result in results:
#     balance = Balance(value=40, person_id=result.id)
#     session.add(balance)

# session.commit()

results = session.query(Balance)
for result in results:
    print(result.value, result.person.name)
