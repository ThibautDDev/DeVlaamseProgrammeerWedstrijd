aantal_testgevallen = int(input())

for geval in range(1, aantal_testgevallen + 1):
    temp = input()
    dagen25, dagen30 = 0, 0
    dag, start = 1, 0
    ok = False

    while(temp != 'stop'):
        temp = float(temp)

        if(not ok):
            if(temp >= 30):
                dagen25 += 1
                dagen30 += 1
            elif(temp >= 25):
                dagen25 += 1

            elif(dagen25 >= 5 and dagen30 >= 3):
                # print(f"dag: {dag}, dagen25: {dagen25}")
                ok = True
                start = dag - dagen25
            else:
                dagen25 = 0
                dagen30 = 0


        # print(f'temp: {temp}, dag: {dag}, dagen25: {dagen25}, dagen30: {dagen30}')
        dag += 1
        temp = input()

    if (start != 0):
        print(f'{geval} {start} {dagen25}')
    else:
        print(f'{geval} geen hittegolf')