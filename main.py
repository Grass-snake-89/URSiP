#загружаем классы (ООП)
from excel_parser import xlsx_parser
from db import db

#создаём таблицу
db = db(path='output.sqlite')

#загружаем данные
parser = xlsx_parser(path=r'Приложение_к_заданию_бек_разработчика.xlsx')
parser.parse(db)
db.commit()

#запрашиваем данные из модуля, чтобы в будущем с ними можно было работать
result = db.get_result() #функция возвращает DataFrame
print(result)

#выводим на печать данные из модуля
#то же самое, что и предыдущее, только отдельной процедурой
db.print_result()
