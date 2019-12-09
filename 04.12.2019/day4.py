# range = 124075-580769 watch out for +/-1

counter2 = 0
for i in range(124075, 580769):
    double_number = False
    increase = False
    a = [int(j) for j in str(i)]
    # a = [5, 7, 7, 7, 7, 7]
    counter = 0
    counter3 = 0

    for g in range(len(a) - 1):
        if a[g] == a[g + 1]:
            counter3 = counter3 + 1
            if counter3 == 1:
                double_number = True
            else:
                double_number = False
                counter3 = 0
        if a[g] <= a[g + 1]:
            counter = counter + 1
            if counter == 5 and double_number:
                counter2 = counter2 + 1
                print("OK " + str(a))
                break
print(counter2)
