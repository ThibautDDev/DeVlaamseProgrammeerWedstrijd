##TE TRAAG


testgevallen = int(input())

for testgeval in range(1, 1+testgevallen):
    # if(testgeval == 5): print("TEST 5!")
    aantalGetallen = int(input())
    arr = []
    for i in range(aantalGetallen):
        arr += [int(input())]
    
    counter = 0
    if(len(arr) == 0): print(f"{testgeval} 1")
    else:
        for i in range(len(arr)+1):
            for k in range(i, len(arr)+1):
                ar1 = arr[:i]
                ar2 = arr[i:k]
                ar3 = arr[k:]
                num1 = sum(arr[:i])
                num2 = sum(arr[i:k])
                num3 = sum(arr[k:])
                # if(testgeval == 5):
                #     print()
                #     print(arr)
                #     print(ar1, ar2, ar3)
                #     print(num1, num2, num3)
                if(num1 == num2 and num2 == num3): 
                    counter += 1
                    # if(testgeval == 5):
                    #     print("found!", ar1, ar2, ar3)
        print(f"{testgeval} {counter}")
    # print()
    