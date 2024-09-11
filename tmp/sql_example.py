import sqlite3

con = sqlite3.connect("sql_example.db")

# create_table = """\
#     CREATE TABLE if not exists movement(
#         id integer PRIMARY KEY AUTOINCREMENT,
#         transaction_description varchar(250),
#         transaction_at date,
#         value_transaction decimal(10,5),
#         type_transaction varchar(12)
#     )
# """

query = """\
    SELECT id, transaction_at, transaction_description, value_transaction, type_transaction
    FROM movement
    WHERE type_transaction = 'Pagamento'
"""

cur = con.cursor()
result = cur.execute(query)

for row in result:
    print(row)


# insert = """\
#     INSERT INTO movement (transaction_description, transaction_at, value_transaction, type_transaction)
#            VALUES ('Pagamento Financiamento', '2024-09-04', -200.05, 'Pagamento')
# """

# con.execute(insert)

# con.execute(create_table)
# con.commit()
con.close()
