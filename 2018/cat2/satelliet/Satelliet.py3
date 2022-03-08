aantal_testgevallen = int(input())

for testgeval in range(1, aantal_testgevallen + 1):
    code = input()
    aantal_verkortingen = int(input())
    dictionary, codes = {}, {}
# Maak lijst
    for verkorting in range(aantal_verkortingen):
        letter = input()
        dictionary[letter] = input()
# Sorteer op lengte (groot --> klein)
    langste = max([len(x) for x in dictionary.values()])
    for lengte in range(langste, 0, -1):
        for key, value in dictionary.items():
            if len(value) == lengte:
                codes[key] = value
# Los op
    output, gevonden = '', True
    while len(code) != 0 and gevonden:
        gevonden = False
        for key, value in codes.items():
            if len(value) <= len(code) and code[0:len(value)] == value and not gevonden:
                gevonden = True
                code = code[len(value):]
                output += key
    if not gevonden:
        output = 'ONMOGELIJK'
    print(testgeval, output)