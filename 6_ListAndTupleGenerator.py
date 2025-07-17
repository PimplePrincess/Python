def main():
    print("Пожалуйста, введите числа:")
    numbers = input()
    createdList = []
    createdTuple = ()
    for i in numbers:
        if i != ' ':
            createdList.append(i)
    createdTuple = tuple(j for j in numbers if j != ' ')
    print("List: ", createdList)
    print("Tuple: ", createdTuple)


if __name__ == '__main__':
    main()

# values = input("Input some comma-separated numbers: ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ', list)
# print('Tuple : ', tuple)