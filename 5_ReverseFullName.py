import math
def main():
    changedPhrase = []
    print("Пожалуйста, введите имя:")
    name = (str(input()))
    print("Пожалуйста, введите фамилию:")
    surname = (str(input()))

    phrase = name + ' ' + surname
    lenPhrase = len(phrase)

    for i in range(lenPhrase):
        changedPhrase.append(phrase[lenPhrase - 1 - i])

    print("".join(changedPhrase))


if __name__ == '__main__':
    main()

