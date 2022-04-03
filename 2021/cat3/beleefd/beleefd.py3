testgevallen = int(input())

def geheel(x):
    return int(x) == x

for testgeval in range(1, 1+testgevallen):
    getal = int(input())
    mogelijk = False

    for lengte in range(2, int((getal)**(1/2)) +2):
        if (lengte % 2 == 0): # even en .5
            deling = getal/lengte
            if (geheel(deling + 0.5)):
                extra_termen = (lengte - 2) / 2
                onder = int(deling - 0.5 - extra_termen)
                boven = int(deling + 0.5 + extra_termen)
                print(f"{testgeval} {getal} = {onder} + ... + {boven}")
                mogelijk = True
        else: # oneven en geheel
            deling = getal/lengte
            if (geheel(deling)):
                extra_termen = (lengte - 1) / 2
                onder = int(deling - extra_termen)
                boven = int(deling + extra_termen)
                print(f"{testgeval} {getal} = {onder} + ... + {boven}")
                mogelijk = True

    if (not mogelijk):
        print(f"{testgeval} ONMOGELIJK")