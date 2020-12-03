def custom_split(val, delimiter):
    return val.split(delimiter)

password_list = []
with open("password_list.txt", "r") as report_repair:
    password_list = list(report_repair.readlines())

count = 0
for password in password_list:
    pswd_all = custom_split(password, " ")
    config = custom_split(pswd_all[0], "-")
    min = int(config[0])
    max = int(config[1])
    config_letter = pswd_all[1].rstrip(":")
    password = pswd_all[2].rstrip("\n")
    if min <= password.count(config_letter) <= max:
        print("----------------------")
        print(password)
        print(config_letter)
        print(f"min {min} max {max}")
        print(f"Letter Count {password.count(config_letter)}")
        print("----------------------")
        count += 1
    #Answer 445

