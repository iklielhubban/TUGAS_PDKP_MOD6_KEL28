from abc import ABC, abstractmethod
import math

class Calculator(ABC):
    def __init__(self):
        self._number = []

    def getNumber(self):
        return self._number

    def setNumber(self, numbers):
        self._number = numbers

    def add(self, *args):
        pass   

    def __str__(self):
        return str(self._number)
    
    def subtract(self, *args):
        pass
    
    def multiply(self, *args):
        pass

    def divide(self, *args):
        pass
    
    def clear(self):
        self._number.clear()

class BasicCalculator(Calculator):
    def add(self):
        return sum(self._number)

    def subtract(self):
        result = self._number[0]
        for num in self._number[1:]:
            result -= num
        return result

    def multiply(self):
        result = 1
        for num in self._number:
            result *= num
        return result

    def divide(self):
        result = self._number[0]
        for num in self._number[1:]:
            result /= num
        return result
    
class ScientificCalculator(Calculator):
    def exponentiation(self):
        result = 1
        for num in self._number:
            result **= num
        return 
    
    def factorial(self, num):
        result = 1
        for i in range(1, num+1):
            result *= i
        return 
    
    def add(self, num1, num2):
        return num1 + num2

    def squareroot(self, num):
        return math.sqrt(num)

while True:
    print("--- Kalkulator ---")
    print("1. Kalkulator basic")
    print("2. Kalkulator ilmiah")
    print("Pilih kalkulator (keluar tekan F): ")
    choice = input()
    if choice == 'F':
        break
    elif choice == '1':
        basic = BasicCalculator()
        numbers = input("Masukkan angka (jika lebih dari satu dipisahkan koma): ")
        basic.setNumber([int(num) for num in numbers.split(',')])
        print("Angka:", basic.getNumber())
        print("Penjumlahan:", basic.add())
        print("Pengurangan:", basic.subtract())
        print("Perkalian:", basic.multiply())
        print("Pembagian:", basic.divide())
    elif choice == '2':
        scientific = ScientificCalculator()
        numbers = input("Masukkan angka (jika lebih dari satu dipisahkan koma): ")
        scientific.setNumber([int(num) for num in numbers.split(',')])
        print("Angka:", scientific.getNumber())
        print("Penjumlahan:", scientific.add(20, 7))
        print("Eksponensial:", scientific.exponentiation())
        print("Faktorial:", scientific.factorial(5))
        print("Akar pangkat dua:", scientific.squareroot(16))
    else:
        print("Input tidak sesuai, mohon coba lagi.")
