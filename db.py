import pandas
import sqlite3
from datetime import date

with open('create.sql', 'r') as sqlite:
    sql_file = sqlite.read()

class db:
    def __init__(self, path):
        self.path = path
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
        self.cursor.executescript(sql_file)

    #добавляет новую строчку в таблицу
    def add_record(self, record):
        self.cursor.execute("""INSERT INTO "data"
(row_id, row_date, company, status, record_type, data_type, data_value) VALUES(?,?,?,?,?,?,?)""", record)

    #возвращает таблицу в виде массива, чтобы её можно было читать вне класса
    def get_result(self):
        self.cursor.execute("""select d.row_date,
            sum(case when d.record_type = 'Qliq' then d.data_value end) as Qliq,
            sum(case when d.record_type = 'Qoil' then d.data_value end) as Qoil,
            sum(d.data_value) as total_sum
        from "data" d
        group by d.row_date;""")
        return pandas.DataFrame(self.cursor.fetchall(), columns=['date','Qliq','Qoil','total_sum'])

    #выводим на печать данные из модуля
    def print_result(self):
        print("\nВывод таблицы:")
        print(self.get_result().to_markdown())

    #записывает данные в БД
    def commit(self):
        self.conn.commit()
