def multiplos():
    for i in range(1, 101):
        multiplo_5 = i % 5
        multiplo_3 = i % 3
        if multiplo_5 == 0 and multiplo_3 == 0:
            print("fizzbuzz")
        elif multiplo_3 == 0:
            print("fizz")
        elif multiplo_5 == 0:
            print("buzz")
        else:
            print(i)


multiplos()