# Utility functions
max_ect_length = 8000

def is_float(s):
    try: 
        float(s)
        return True
    except: 
        return False

def extract_statistic(s, ignore_single_digit = False):
    # The string should not be empty
    s = s.replace(",", "") # Remove commas
    if len(s) == 0:
        return None
    # It could be a valid number that is not a recent year (i.e 2015-2025)
    if ignore_single_digit and is_float(s) and float(s) < 10:
        return None
    if is_float(s) and (float(s) < 2015 or float(s) > 2025):
        return (float(s), None)
    # In the form of $[valid number]
    if s[0] == "$" and is_float(s[1:]):
        return (float(s[1:]), "$")
    # Or in the form of [valid number]%
    if s[-1] == "%" and is_float(s[:-1]):
        return (float(s[:-1]), "%")
    return None

def extract_numbers(text, ignore_single_digit = False):
    words = [s for line in text.split("\n") for s in line.split(" ")]
    words = list(filter(len, words))
    words = list(map(lambda s: s[:-1] if s[-1] in ["."] else s, words))
    numbers = set(map(lambda w: extract_statistic(w, ignore_single_digit), words))
    numbers.remove(None)
    return list(numbers)

def extract_key_points(ect, summary, ignore_single_digit = False):
    ect_numbers = []
    if len(ect) > max_ect_length:
        front = ect[:max_ect_length // 2]
        back = ect[-max_ect_length // 2:]
        ect_numbers = extract_numbers(f"{front}\n{back}", ignore_single_digit)
    else:
        ect_numbers = extract_numbers(ect, ignore_single_digit)
    key_points = ""
    key_points_numbers = []
    for line in summary.split("\n"):
        line_numbers = extract_numbers(line, ignore_single_digit)
        ect_precision = 0
        for n in line_numbers:
            if n in ect_numbers:
                ect_precision += 1
        # print(len(ect), ect_precision, len(line_numbers))
        if ect_precision > 0 and ect_precision == len(line_numbers):
            key_points += line + "\n"
            key_points_numbers.extend(line_numbers)
    return (key_points, list(set(key_points_numbers)))
            