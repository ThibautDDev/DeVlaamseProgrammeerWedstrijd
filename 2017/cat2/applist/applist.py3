for a in range(1, int(input('')) + 1):
    #print()
    #print(a)
    input_lijn = input('')
    input_lijn = input_lijn.split(" ")
    aantal_apps_per_scherm = int(input_lijn[0])
    totaal_aantal_apps = int(input_lijn[1])
    aantal_oproepen = int(input_lijn[2])
    #print(aantal_apps_per_scherm, totaal_aantal_apps, aantal_oproepen)

    lijst_apps = [input("")]
    lijst_apps = lijst_apps[0].split(" ")
    #print(lijst_apps)

    gevraagde_apps = input('')
    gevraagde_apps = gevraagde_apps.split(" ")
    #print(gevraagde_apps)


    aantal_veegbewegingen = 0
    while gevraagde_apps != []:
        teller = 0
        for i in range(totaal_aantal_apps):
            teller += 1
            if lijst_apps[i] == gevraagde_apps[0]:
                break

        getal = 0
        if (teller % aantal_apps_per_scherm) == 0:
            getal = (teller/aantal_apps_per_scherm) - 1
        else:
            getal = int(teller/aantal_apps_per_scherm)
        #print(getal, lijst_apps)
        aantal_veegbewegingen += getal

        if teller != 1:
            app1 = lijst_apps[teller-2]
            app2 = lijst_apps[teller-1]
            lijst_apps[teller-2] = app2
            lijst_apps[teller-1] = app1
        #print(lijst_apps, aantal_veegbewegingen)

        gevraagde_apps.pop(0)

    print(a, int(aantal_veegbewegingen))
