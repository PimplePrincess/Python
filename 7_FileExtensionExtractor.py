def main():
    print("Пожалуйста, напишите имя файла:")
    fileName = input()
    dot = fileName.rfind('.')
    result = ""

    if '.' not in fileName:
        print("У файла нет расширения!")
        return 0
    else:
        if dot != 0:
            result = fileName[dot+1:]
    if not result.isdigit():
        print(result)
    else:
        print("Неверный формат!")




if __name__ == '__main__':
    main()
