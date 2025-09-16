def common_tc_dates(cyclone_dates_1: list[str], cyclone_dates_2: list[str]) -> dict:
    # количество дней в каждом месяце (без високосных)
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    # префиксные суммы для перевода (месяц-1 -> смещение)
    prefix = [0]
    for d in days_in_month:
        prefix.append(prefix[-1] + d)

    def parse_date(s: str):
        s = s.strip()
        parts = s.split("/")
        if len(parts) != 3:
            return None
        try:
            day = int(parts[0].strip())
            month = int(parts[1].strip())
            year = int(parts[2].strip())
        except ValueError:
            return None
        # проверка диапазонов
        if not (1982 <= year <= 2022):
            return None
        if not (1 <= month <= 12):
            return None
        if not (1 <= day <= days_in_month[month - 1]):
            return None
        # перевод в день года
        return prefix[month - 1] + day

    def extract_days(dates):
        days = set()
        for d in dates:
            day_of_year = parse_date(d)
            if day_of_year is not None:
                days.add(day_of_year)
        return days

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
