def split(sequence, x):
    return sequence[:x], sequence[x:]

def parse(digits):
    for n in range(1, len(digits)):
        expected, remainder = split(digits, n)
        failures = []
        while len(failures) <= 1 and remainder:
            expected = str(int(expected) + 1)
            actual, remainder = split(remainder, len(expected))
            if actual != expected:
                failures.append(expected)
                remainder = actual + remainder  # Re-parse
        if len(failures) == 1:
            return int(failures[0])
    return -1

for testgeval in range(1, 1+int(input())):
    digits = input()
    res = parse(digits)
    if res == -1:
        print(f"{testgeval} geen ontbrekend getal")
    else:
        print(f"{testgeval} {res}")