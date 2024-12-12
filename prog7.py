import re

# Список типових патернів SQL-ін’єкцій
SQL_INJECTION_PATTERNS = [
    r"(--|\#)",  # коментарі
    r"(;|\/\*)",  # завершення SQL запиту
    r"(\'|\")",  # апострофи та лапки
    r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|EXEC|TRUNCATE|ALTER|CREATE|REVOKE|GRANT|HAVING|FROM|WHERE|OR|AND)\b)",  # ключові слова SQL
    r"(eval\()",
    r"(\b(CHAR|DATABASE|HEX|MD5|CONCAT|BENCHMARK)\b)"  # можливі небезпечні функції
]

def is_sql_injection(input_data):
    """
    Перевірка вхідних даних на наявність SQL-ін'єкцій.
    """
    for pattern in SQL_INJECTION_PATTERNS:
        if re.search(pattern, input_data, re.IGNORECASE):
            return True
    return False

def sanitize_input(input_data):
    """
    Фільтрація небезпечних символів.
    """
    # Замінюємо потенційно небезпечні символи на пробіли або екрануємо їх
    input_data = re.sub(r"[;'\"]", " ", input_data)
    return input_data

def analyze_input(input_data):
    """
    Основна функція аналізу вхідних даних.
    Виявляє SQL-ін’єкції та фільтрує небезпечні символи.
    """
    if is_sql_injection(input_data):
        print("Попередження: можливе SQL-ін’єкція!")
        # Фільтрація небезпечних символів
        sanitized_input = sanitize_input(input_data)
        print("Очищені дані:", sanitized_input)
    else:
        print("Дані безпечні.")

# Приклад використання
input_data = input("Введіть дані для перевірки: ")
analyze_input(input_data)
