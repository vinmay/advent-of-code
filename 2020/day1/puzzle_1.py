number_list = []
with open("puzzle_1_input.txt", "r") as report_repair:
    number_list = list(map(int, report_repair.readlines()))

for i in range(0, len(number_list)):
    for j in range(i+1, len(number_list)):
        if (number_list[i] + number_list[j] == 2020):
            print(number_list[i] * number_list[j])
            #Answer 1015476
