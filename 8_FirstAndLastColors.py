def main():
    userList = input("Пожалуйста, напишите через пробел цвета:\n")
    colorsList = userList.split()
    print("Первый цвет: ", colorsList[0])
    print("Второй цвет: ", colorsList[-1])

if __name__ == '__main__':
    main()
