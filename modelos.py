from pydantic import BaseModel
from typing import Optional
from datetime import date

class Beneficiary(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: str  # Será 'M' o 'F' o algún otro valor de 1 caracter
    birth_date: Optional[date] = None
    rut_number: Optional[int] = None
    program: Optional[str] = None
    process_date: Optional[date] = None
