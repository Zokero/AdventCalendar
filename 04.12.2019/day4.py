# range = 124075-580769 watch out for +/-1

counter2 = 0
for i in range(124075, 580769):
    double_repeat = False
    repeat_counter = 0
    increase = False
    a = [int(j) for j in str(i)]
    counter_to_5 = 0

    for g in range(len(a) - 1):

        if a[g] == a[g + 1]:
            counter_to_5 = counter_to_5 + 1
            repeat_counter = repeat_counter + 1

        if a[g] < a[g + 1]:
            if repeat_counter == 1:
                double_repeat = True

            counter_to_5 = counter_to_5 + 1
            repeat_counter = 0
        if len(a) == g + 2:
            print("test")
            if repeat_counter == 1:
                double_repeat = True

        if counter_to_5 == 5 and double_repeat:
            print("OK " + str(a))
            counter2 = counter2 + 1

print(counter2)
