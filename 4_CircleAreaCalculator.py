import math
def main():
    print("Пожалуйста, введите значение радиуса круга:")
    radius = float(input())
    area = math.pi * radius**2
    print("Вы ввели радиус, равный ", area)

if __name__ == '__main__':
    main()

