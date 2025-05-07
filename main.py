from fastapi import FastAPI, HTTPException
from typing import List
from basedatos import connection
from modelos import Beneficiary

app = FastAPI()

@app.get("/beneficiaries", response_model=List[Beneficiary])
def get_beneficiaries(skip: int = 0, limit: int = 10):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM beneficiaries ORDER BY id OFFSET ? ROWS FETCH NEXT ? ROWS ONLY", (skip, limit))
    rows = cursor.fetchall()
    return [Beneficiary(
            id=row[0], first_name=row[1], last_name=row[2], gender=row[3],
            birth_date=row[4], rut_number=row[5], program=row[6], process_date=row[7]
        ) for row in rows]

@app.get("/beneficiaries/{id}", response_model=Beneficiary)
def get_beneficiary(id: int):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM beneficiaries WHERE id = ?", (id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Beneficiary not found")
    return Beneficiary(
        id=row[0], first_name=row[1], last_name=row[2], gender=row[3],
        birth_date=row[4], rut_number=row[5], program=row[6], process_date=row[7]
    )

@app.get("/beneficiaries/program/{program}", response_model=List[Beneficiary])
def get_beneficiaries_by_program(program: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM beneficiaries WHERE program = ?", (program,))
    rows = cursor.fetchall()
    return [Beneficiary(
            id=row[0], first_name=row[1], last_name=row[2], gender=row[3],
            birth_date=row[4], rut_number=row[5], program=row[6], process_date=row[7]
        ) for row in rows]
