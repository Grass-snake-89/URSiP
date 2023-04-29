import pandas   # pip install pandas #работа с файлом Excel
#pip install tabulate #используется для отображения DataFrame
from datetime import date #работа с датами

class xlsx_parser:
    def __init__(self, path):
        self.path = path
        
    def parse(self, db):
        df = pandas.read_excel(self.path, sheet_name=0, header=None, index_col=None)
        #заполняем каждую объединённую ячейку
        df = df.fillna(method='ffill', axis=1)
        #выводим полученную таблицу
        print('Получили таблицу:')
        print(df.to_markdown(), end="\n\n")
        print("Количество колонок:",df.shape[1], sep="\t")
        print("Количество строк:",df.shape[0], sep="\t")
        print()
        
        #считываем данные построчно (кроме 3 первых строк-заголовков)
        for row in range(3,df.shape[0]):
            record_date = date(2023, 4, df[0][row])
            company = df[1][row]
            #считываем каждую ячейку отдельно
            for column in range(2,df.shape[1]):
                #print("значение=",df[column][row],"\tстатус=",df[column][0],"\tтип=",df[column][1],"\tданные=",df[column][2],"\tномер_строки=",df[0][row],"\tдата_записи=",record_date,"\tкомпания=",company, sep="")
                #row_id, row_date, company, status, record_type, data_type, data_value
                db.add_record([df[0][row],record_date,company,df[column][0],df[column][1],df[column][2],df[column][row]])
