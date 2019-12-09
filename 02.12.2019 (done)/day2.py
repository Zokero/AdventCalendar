# --- Day 2: 1202 Program Alarm ---
# On the way to your gravity assist around the Moon, your ship computer beeps angrily about a "1202 program alarm". 
# On the radio, an Elf is already explaining how to handle the situation: "Don't worry, that's perfectly norma--" 
# The ship computer bursts into flames.

# You notify the Elves that the computer's magic smoke seems to have escaped. "That computer ran Intcode programs 
# like the gravity assist program it was working on; surely there are enough spare parts up there to build a new Intcode computer!"

# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one, start by looking 
# at the first integer (called position 0). Here, you will find an opcode - either 1, 2, or 99. The opcode 
# indicates what to do; for example, 99 means that the program is finished and should immediately halt. Encountering an unknown 
# opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers 
# immediately after the opcode tell you these three positions - the first two indicate the positions from which you 
# should read the input values, and the third indicates the position at which the output should be stored.

# For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those 
# values, and then overwrite the value at position 30 with their sum.

# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three 
# integers after the opcode indicate where the inputs and outputs are, not their values.

# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

# For example, suppose you have the following program:

# 1,9,10,3,2,3,11,0,99,30,40,50
# For the purposes of illustration, here is the same program split into multiple lines:

# 1,9,10,3,
# 2,3,11,0,
# 99,
# 30,40,50
# The first four integers, 1,9,10,3, are at positions 0, 1, 2, and 3. Together, they represent the 
# first opcode (1, addition), the positions of the two inputs (9 and 10), and the position of the output (3). To handle 
# this opcode, you first need to get the values at the input positions: position 9 contains 30, and position 10 contains 40. Add these 
# numbers together to get 70. Then, store this value at the output position; here, the output position (3) is at position 3, so it overwrites 
# itself. Afterward, the program looks like this:

# 1,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50
# Step forward 4 positions to reach the next opcode, 2. This opcode works just like the previous, but it 
# multiplies instead of adding. The inputs are at positions 3 and 11; these positions contain 70 and 50 respectively. 
# Multiplying these produces 3500; this is stored at position 0:

# 3500,9,10,70,
# 2,3,11,0,
# 99,
# 30,40,50
# Stepping forward 4 more positions arrives at opcode 99, halting the program.

# Here are the initial and final states of a few more small programs:

# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
# 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
# 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
# 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.
# Once you have a working computer, the first step is to restore the gravity assist program (your puzzle input) to the "1202 program alarm" state it 
# had just before the last computer caught fire. To do this, before running the program, replace position 1 with the value 12 and 
# replace position 2 with the value 2. What value is left at position 0 after the program halts?


def get_input_data():
    file = open('/02.12.2019 (done)/dataInput.txt', 'r')
    return file.read().split(',')


def generate_list_of_pairs():
    new_list = list()
    for i in range(0, 99):
        for j in range(0, 99):
            new_list.append([i, j])

    return new_list


def check_intcode(values, index, a, b):
    copy_value = values
    # for i in range(0, 99):
    #     for j in range(0, 99):
    copy_value[1] = a
    copy_value[2] = b

    if int(copy_value[index]) == 1:
        index_plus_one_value = int(copy_value[index + 1])
        index_plus_two_value = int(copy_value[index + 2])
        # print(str((index_plus_one_value * 100) + index_plus_two_value))
        result = int(copy_value[index_plus_one_value]) + int(copy_value[index_plus_two_value])
        copy_value[int(copy_value[index + 3])] = result

    elif int(copy_value[index]) == 2:
        index_plus_one_value = int(copy_value[index + 1])
        index_plus_two_value = int(copy_value[index + 2])
        # print(str((index_plus_one_value * 100) + index_plus_two_value))
        result = int(copy_value[index_plus_one_value]) * int(copy_value[index_plus_two_value])
        copy_value[int(copy_value[index + 3])] = result

    elif int(copy_value[index]) == 99:
        print(copy_value)
        return copy_value
    print(copy_value)
    if copy_value[0] == 19690720:
        xxx = (100 * a) + b
        print(xxx)
        print("<<<<<<>>>>>>>")
    return check_intcode(copy_value, index + 4, copy_value[1], copy_value[2])


def test():
    for i in range(0, 99):
        for j in range(0, 99):
            check_intcode(get_input_data(), 0, i, j)




# assert check_intcode([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 0) == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
# assert check_intcode([1, 0, 0, 0, 99], 0) == [2, 0, 0, 0, 99]
# assert check_intcode([2, 4, 4, 5, 99, 0], 0) == [2, 4, 4, 5, 99, 9801]
# assert check_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99], 0) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
test()
# check_intcode(get_input_data(), 0)

# Programy Intkod są podane jako lista liczb całkowitych; wartości te są używane jako stan początkowy pamięci
# komputera. Po uruchomieniu programu Intcode należy rozpocząć od zainicjowania pamięci na wartości programu.
# Pozycja w pamięci nazywana jest adresem (na przykład pierwsza wartość w pamięci to „adres 0”).
#
# Kody (takie jak 1, 2 lub 99) oznaczają początek instrukcji. Wartości użyte bezpośrednio po kodzie op, jeśli występują,
# są nazywane parametrami instrukcji. Na przykład w instrukcji 1, 2, 3, 4, 1 to kod operacji; 2, 3 i 4 są parametrami.
# Instrukcja 99 zawiera tylko kod operacji i nie ma parametrów.
#
# Adres bieżącej instrukcji nazywany jest wskaźnikiem instrukcji; zaczyna się od 0. Po zakończeniu instrukcji wskaźnik
# instrukcji zwiększa się o liczbę wartości w instrukcji; dopóki nie dodasz więcej instrukcji do komputera, zawsze jest
# to 4 (1 kod operacji + 3 parametry) dla instrukcji dodawania i mnożenia. (Instrukcja zatrzymania zwiększyłaby wskaźnik
# instrukcji o 1, ale zamiast tego zatrzymuje program.)
#
# „Nie znając terminologii, jesteśmy gotowi do kontynuowania. Aby ukończyć wspomaganie grawitacyjne, musisz ustalić,
# która para sygnałów wejściowych daje wynik 19690720”.
#
# Dane wejściowe powinny być nadal dostarczane do programu, zastępując wartości pod adresami 1 i 2, tak jak poprzednio.
# W tym programie wartość umieszczona w adresie 1 nazywana jest rzeczownikiem, a wartość umieszczona w adresie 2 nazywana
# jest czasownikiem. Każda z dwóch wartości wejściowych będzie zawierać się między 0 a 99 włącznie.
#
# Po zatrzymaniu programu jego wyjście jest dostępne pod adresem 0, tak jak poprzednio. Za każdym razem, gdy spróbujesz
# użyć pary wejść, pamiętaj, aby najpierw zresetować pamięć komputera do wartości w programie (układanki) - innymi słowy,
# nie używaj ponownie pamięci z poprzedniej próby.
#
# Znajdź rzeczownik i czasownik, które powodują, że program generuje wynik 19690720.
# Co to jest 100 * rzeczownik + czasownik?
# (Na przykład, jeśli rzeczownik = 12 i czasownik = 2, odpowiedź będzie wynosić 1202.)
