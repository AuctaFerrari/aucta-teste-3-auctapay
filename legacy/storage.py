import sqlite3


def connect():
    return sqlite3.connect("concilia.db")


def save_result(connection, result):
    connection.execute(
        "INSERT INTO reconciliation(title_id, payment_id, status) VALUES (?, ?, ?)",
        (result["title_id"], result["payment_id"], result["status"]),
    )
    connection.commit()
