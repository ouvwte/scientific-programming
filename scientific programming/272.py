import re
from typing import List, Dict, Optional

def common_tc_dates(cyclone_dates_1: List[str], cyclone_dates_2: List[str]) -> Dict[str, int]:
    """
    Подсчитывает совпадающие/уникальные дни года для двух списков дат.
    Формат даты: D[/]M[/]YYYY с возможными пробелами вокруг частей.
    29 февраля считается некорректным (в задаче год = 365 дней).
    Допустимые годы: 1982..2022.
    Некорректные строки игнорируются.
    """
    # дни в месяцах (без високосных)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # накопл. смещения: prefix[month-1] дает количество дней перед данным месяцем
    prefix = [0]
    for d in days_in_month:
        prefix.append(prefix[-1] + d)

    # строгий паттерн: допускает пробелы вокруг частей, день/месяц 1-2 цифры, год — ровно 4 цифры
    date_re = re.compile(r'^\s*(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*(\d{4})\s*$')

    def parse_date(s: object) -> Optional[int]:
        # принимаем только объекты строкового типа
        if not isinstance(s, str):
            return None
        m = date_re.match(s)
        if not m:
            return None
        day = int(m.group(1))
        month = int(m.group(2))
        year = int(m.group(3))
        # год в допустимом диапазоне
        if year < 1982 or year > 2022:
            return None
        # месяц/день в допустимых границах (29 февраля — НЕ допустим)
        if month < 1 or month > 12:
            return None
        max_day = days_in_month[month - 1]
        if day < 1 or day > max_day:
            return None
        # номер дня в году (1..365)
        return prefix[month - 1] + day

    def extract_days(lst: List[object]) -> set:
        s = set()
        for item in lst:
            d = parse_date(item)
            if d is not None:
                s.add(d)
        return s

    set1 = extract_days(cyclone_dates_1)
    set2 = extract_days(cyclone_dates_2)

    both = set1 & set2
    only1 = set1 - set2
    only2 = set2 - set1
    anyd = set1 | set2

    return {
        "any_year": len(anyd),
        "both_years": len(both),
        "only_one_year": len(only1) + len(only2),
        "only_first_year": len(only1),
        "only_second_year": len(only2),
        "none_of_years": 365 - len(anyd),
    }

# --- Быстрая самопроверка на примере из условия ---
if __name__ == "__main__":
    cyclone_dates_1 = ["04/01/2014", "05/01/2014"]
    cyclone_dates_2 = ["06/01/2015", "04/01/2016"]
    expected = {
        "any_year": 3,
        "both_years": 1,
        "only_one_year": 2,
        "only_first_year": 1,
        "only_second_year": 1,
        "none_of_years": 362,
    }
    out = common_tc_dates(cyclone_dates_1, cyclone_dates_2)
    print("Result:", out)
    assert out == expected, f"Ошибка: ожидалось {expected}, получено {out}"
    print("Self-test passed.")
