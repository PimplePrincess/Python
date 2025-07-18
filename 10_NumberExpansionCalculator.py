def main():
    userInput = input("Пожалуйста, введите значение (n):\n")
    num1 = int(userInput)
    num2 = int(userInput * 2)
    num3 = int(userInput * 3)
    result = num1 + num2 + num3
    print("Результат:", result)

if __name__ == '__main__':
    main()
