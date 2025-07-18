def main():
    userList = input("Пожалуйста, напишите через пробел дату (только числа):\n")
    dateList = userList.split()
    print("Экзамен начнётся: ", dateList[0], '/',dateList[1], '/',dateList[2])

if __name__ == '__main__':
    main()
