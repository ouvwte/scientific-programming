from typing import List, Dict, Optional
import re

def common_tc_dates(
    cyclone_dates_1: List[str],
    cyclone_dates_2: List[str]
) -> Dict[str, int]:
    days_in_month = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    prefix = [0]
    for d in days_in_month:
        prefix.append(prefix[-1] + d)

    date_re = re.compile(r'^\s*(\d{1,2})\s*/\s*(\d{1,2})\s*/\s*(\d{4})\s*$')

    def parse_date(s: str) -> Optional[int]:
        m = date_re.match(s)
        if not m:
            return None
        day, month, year = map(int, m.groups())

        if not (1982 <= year <= 2022):
            return None
        if not (1 <= month <= 12):
            return None
        max_day = days_in_month[month - 1]
        if not (1 <= day <= max_day):
            return None
        return prefix[month - 1] + day

    def extract_days(lst: List[str]) -> set:
        res = set()
        for s in lst:
            if not isinstance(s, str):
                continue
            d = parse_date(s)
            if d is not None:
                res.add(d)
        return res

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

# cyclone_dates_1 = ["04/01/2014", "05/01/2014"]
# cyclone_dates_2 = ["06/01/2015", "04/01/2016"]

# print(common_tc_dates(cyclone_dates_1, cyclone_dates_1))
