def common_tc_dates(cyclone_dates_1: list[str], cyclone_dates_2: list[str]) -> dict:
    # Анализирует повторяемость дней года для двух наборов дат циклонов.
    def parse_date(date_str):
        # Извлекает день и месяц из строки даты, игнорируя год.
        try:
            # Убираем пробелы и разбиваем по '/'
            parts = date_str.strip().split('/')
            if len(parts) != 3:
                return None

            day = int(parts[0].strip())
            month = int(parts[1].strip())
            year = int(parts[2].strip())

            # Проверяем корректность года (1982-2022)
            if year < 1982 or year > 2022:
                return None

            # Проверяем корректность дня и месяца
            if month < 1 or month > 12 or day < 1 or day > 31:
                return None

            # Проверяем конкретные ограничения по дням в месяцах
            if month in [4, 6, 9, 11] and day > 30:
                return None
            if month == 2 and day > 28: # 29 февраля не существует по условию
                return None

            return (month, day)

        except (ValueError, AttributeError):
            return None

    # Множества для уникальных дней года (игнорируя год)
    days_set_1 = set()
    days_set_2 = set()

    # Обрабатываем первый набор дат
    for date_str in cyclone_dates_1:
        day_month = parse_date(date_str)
        if day_month:
            days_set_1.add(day_month)

    # Обрабатываем второй набор дат
    for date_str in cyclone_dates_2:
        day_month = parse_date(date_str)
        if day_month:
            days_set_2.add(day_month)

    # Вычисляем различные множества
    both_days = days_set_1 & days_set_2 # Пересечение
    only_first_days = days_set_1 - days_set_2 # Только в первом
    only_second_days = days_set_2 - days_set_1 # Только во втором
    any_days = days_set_1 | days_set_2 # Объединение

    # Подсчитываем результаты
    total_days_in_year = 365

    return {
    "any_year": len(any_days),
    "both_years": len(both_days),
    "only_one_year": len(only_first_days) + len(only_second_days),
    "only_first_year": len(only_first_days),
    "only_second_year": len(only_second_days),
    "none_of_years": total_days_in_year - len(any_days)
    }


cyclone_dates_1 = ["04/01/2014", "05/01/2014"]
cyclone_dates_2 = ["06/01/2015", "04/01/2016"]

print(common_tc_dates(cyclone_dates_1, cyclone_dates_1))