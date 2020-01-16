# импорт системной бибиотеки
from sys import argv

# передача параметров при запуске скрипта
script_name, work_hours, salary, bounty = argv

# расчет формулы и выдача на экран
print(f'({work_hours}x{salary})+{bounty}={int(work_hours)*int(salary)+int(bounty)}')
