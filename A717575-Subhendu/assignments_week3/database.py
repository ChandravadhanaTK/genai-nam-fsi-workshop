

import json
import logging
import os
from pathlib import Path


db = None # db file instance


def init_db():
    file_name: str = os.getenv("DB_FILE_NAME")
    if not file_name:
        raise ValueError("DB_FILE_NAME environment variable not set")
    file_path: Path = Path(__file__).parent / file_name
    
    if not file_path.exists():
        file_path.touch()
    global db
    db = file_path


def insert_rows(table_name: str, key: str, rows: list[dict]) -> None:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data = json.loads(lines)
    if table_name  not in data:
        return
    for row in rows:
        if any([True for r in data[table_name] if row[key] == r[key]]):
            logging.warning(f"Row with {key}={row[key]} already exists")
            continue
        data[table_name].append(row)
    with open(db, "w") as f:
        f.write(json.dumps(data, indent=2))


def get_rows(table_name: str, number_of_rows: int = 0) -> list[dict]:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data = json.loads(lines)
    if table_name in data:
        if number_of_rows == 0:
            return data[table_name]
        else:
            return data[table_name][:number_of_rows]
    logging.warning(f"Rows for table {table_name} doesnot exists")
    return None


def get_row_by_id(table_name: str, key: str, row_id: int) -> dict:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data = json.loads(lines)
    if table_name in data:
        for row in data[table_name]:
            if row[key] == row_id:
                return row
    logging.warning(f"Row with {key}={row_id} doesnot exists")
    return None


def update_row(table_name: str, key: str, row_id: int, row: dict) -> dict:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data: dict[str,list[dict]] = json.loads(lines)
    if table_name in data:
        for index, r in enumerate(data[table_name]):
            if r[key] == row_id:
                data[table_name][index] = row
                with open(db, "w") as f:
                    f.write(json.dumps(data, indent=2))
                return row
    logging.warning(f"Row with {key}={row_id} doesnot exists")
    return None

def patch_row(table_name: str, key: str, row_id: int, row: dict) -> dict:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data: dict[str,list[dict]] = json.loads(lines)
    if table_name in data:
        for index, r in enumerate(data[table_name]):
            if r[key] == row_id:
                data[table_name][index].update(row)
                with open(db, "w") as f:
                    f.write(json.dumps(data, indent=2))
                return row
    logging.warning(f"Row with {key}={row_id} doesnot exists")
    return None


def delete_row(table_name: str, key: str, row_id: int) -> dict:
    global db
    with open(db, "r") as f:
        lines = f.read()
    data = json.loads(lines)
    if table_name in data:
        for index, row in enumerate(data[table_name]):
            if row[key] == row_id:
                data[table_name].pop(index)
                with open(db, "w") as f:
                    f.write(json.dumps(data, indent=2))
                return row
    logging.warning(f"Row with {key}={row_id} doesnot exists")
    return None
