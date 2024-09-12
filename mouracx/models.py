from datetime import date
from typing import Optional
from pydantic import condecimal

from sqlmodel import SQLModel, Field

class Movement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    data: date = Field(nullable=False)
    transacao: str = Field(nullable=False)
    valor: condecimal(decimal_places=3) = Field(default=0)
    tipo: str = Field(nullable=False)


    def __str__(self):
        return f"{self.data} - {self.transacao} - ({self.valor}) - {self.tipo}"
