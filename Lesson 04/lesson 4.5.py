# импортирование функции редюс
from functools import reduce

# надеюсь это читабельно))
print(reduce((lambda item1, item2: item1 + item2), [a for a in range(100, 1001) if a % 2 == 0]))
