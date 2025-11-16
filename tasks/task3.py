# tasks/task3.py

def solve():
# Ниже пишите решение задачи
     # Чтение двух слов
    word1 = input().strip()
    word2 = input().strip()

# Проверка, что хотя бы одно слово равно "awesome"
    result = word1 == "awesome" or word2 == "awesome"

# Вывод результата
    print(result)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()