#1 Дано натуральное число n. Написать функцию, которая сумму его цифр

def summa(n):
    '''
    Функция принимает натуральное число и
    возвращает сумму его цифр
    '''
    return n%10 + summa(n//10) if n>0 else 0
    
#2 Дано натуральное число. Записать число в обратном порядке
def reverse(n):
    """
    Функция принимает натуральное число и
    вовращает его перевернутую версию
    """
    if n<10:
        return str(n)
    return (str(n%10)+reverse(n//10))

#3 Проверить простоту числа.

def prime(n,i=2):
    """
    Функция принимает число и проверяет его на простоту
    и возвращает Истину или Ложь
    """
    if n<=2:
        return True if n == 2 else False
    if n% i == 0:
        return False
    if i*i > n:
        return True
    return prime(n, i+1)

#4 Написать функцию, которая будет принимать натуральное число n и возвращать n-ую строку треугольника Паскаля.

def pascal(n):
    """
    Функция принимает натуральное число и
    возвращает n-ую строку треугольника
    паскаля
    """
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        prev_row = pascal(n - 1)
        row = [1]
        for i in range(len(prev_row) - 1):
            row.append(prev_row[i] + prev_row[i + 1])
        row.append(1)
        return row


#5 Написать функцию генерации перестановок из заданного массива заданной длины
def perm(arr, n, L=[]):
    """
    Функция принимает массив в виде списка, 
    длинну массива в виде натурального числа и
    возвращает всевозможные перестановки
    """
    if len(L) == n:
        print(L)
        return
    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        perm(new_arr, n, L + [arr[i]])




if __name__ == '__main__':
    print(summa(115))
    print(reverse(15))
    print(prime(5))
    print(pascal(4))
    print(perm([1,2,3], 2))
    