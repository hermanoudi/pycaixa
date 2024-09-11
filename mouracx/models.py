import json
from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal



class Movement(BaseModel):
    pk: int
    data: datetime
    transacao: str
    valor: Decimal
    tipo: str


    def __str__(self):
        return f"{self.data} - {self.transacao} - ({self.valor}) - {self.tipo}"

from mouracx.database import connect
db = connect()

for pk, data in db["movement"].items():
    mov = Movement(pk=pk, **data)
    print(mov)
    print(mov.json())
