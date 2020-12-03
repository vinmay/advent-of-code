def custom_split(val, delimiter):
    return val.split(delimiter)

password_list = []
with open("password_list.txt", "r") as report_repair:
    password_list = list(report_repair.readlines())

count = 0

for password in password_list:
    letter_count = 0
    pswd_all = custom_split(password, " ")
    config = custom_split(pswd_all[0], "-")
    pos1 = int(config[0])
    pos2 = int(config[1])
    config_letter = pswd_all[1].rstrip(":")
    password = pswd_all[2].rstrip("\n")
    if password[pos1 - 1] == config_letter:
        letter_count += 1
    if password[pos2 - 1] == config_letter:
        letter_count += 1

    if letter_count == 1:
        count += 1
    #Answer 491