aantal_testgevallen = int(input())

for geval in range(1, aantal_testgevallen + 1):
    temp = input()
    dagen, dag, start = 0, 1, 0
    while(temp != 'stop'):
        temp = float(temp)
        if (start == 0 and temp >= 25.0):
            dagen += 1
        elif (start == 0 and dagen >= 5):
            start = dag - dagen

        print(f'temp: {temp}, dag: {dag}, dagen: {dagen}')
        temp = input()
        dag += 1

    if (start != 0):
        print(f'-------------{geval} {start} {dagen}')
    else:
        print(f'-------------{geval} geen hittegolf')