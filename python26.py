for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end=" ")
    print(" ")

    # second method
    #
    # for i in range(1,6):
    #     for j in range(1,i+1):
    #         print("*", end=" ")
    #     print(" ")