# برنامه ای بنویسید که از کاربر یوزنیم و پسورد بگیرد و درست و غلط را نشان دهد

username = "ershiatjn"
password = "ershia153624"

while True:

    user_guess = input("enter your username: ")
    pass_guess = input("enter your password: ")

    if password == pass_guess and user_guess == username:
        print("user and password is correct you entered")
        break

    elif pass_guess != password or user_guess != username:
        print("wrong user and password please try again")
        continue




