from typing import List, Dict

def common_tc_dates(cyclone_dates_1: List[str], cyclone_dates_2: List[str]) -> Dict[str, int]:
    # количество дней в каждом месяце (без високосных)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # префиксные суммы: смещение в днях до начала месяца m (1-based)
    prefix = [0]
    for d in days_in_month:
        prefix.append(prefix[-1] + d)

    def parse_date(s):
        # принимать только строки
        if not isinstance(s, str):
            return None
        s = s.strip()
        parts = s.split('/')
        if len(parts) != 3:
            return None
        day_s = parts[0].strip()
        mon_s = parts[1].strip()
        year_s = parts[2].strip()

        # формальные проверки: день/месяц — 1..2 цифры, год — ровно 4 цифры
        if not (1 <= len(day_s) <= 2 and day_s.isdigit()):
            return None
        if not (1 <= len(mon_s) <= 2 and mon_s.isdigit()):
            return None
        if not (len(year_s) == 4 and year_s.isdigit()):
            return None

        day = int(day_s)
        month = int(mon_s)
        year = int(year_s)

        # год в допустимом диапазоне
        if not (1982 <= year <= 2022):
            return None
        # месяц и день в пределах
        if not (1 <= month <= 12):
            return None
        max_day = days_in_month[month - 1]
        if not (1 <= day <= max_day):
            return None

        # перевод в номер дня в году (1..365)
        return prefix[month - 1] + day

    def extract_days(lst):
        s = set()
        for it in lst:
            d = parse_date(it)
            if d is not None:
                s.add(d)
        return s

    set1 = extract_days(cyclone_dates_1)
    set2 = extract_days(cyclone_dates_2)

    anyd = set1 | set2
    both = set1 & set2
    only1 = set1 - set2
    only2 = set2 - set1

    return {
        "any_year": len(anyd),
        "both_years": len(both),
        "only_one_year": len(only1) + len(only2),
        "only_first_year": len(only1),
        "only_second_year": len(only2),
        "none_of_years": 365 - len(anyd),
    }
