# Решение 2: Сортируй и сравнивай
#
# Следующее решение задачи про анаграммы будет использовать
# тот факт, что даже если s1 и s2 различны, они будут анаграммами только если состоят
# из одинаковых символов. Следовательно, если мы отсортируем каждую строку в алфавитном
# порядке от a до z, то в итоге получим одинаковые строки (если, конечно, s1 и s2 - анаграммы).
# Опять же, в Python мы можем использовать встроенный метод sort
# для списков, полученных в начале функции конвертацией каждой строки.

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    print('before sorting alist1=', alist1)
    print('before sorting alist2=', alist2)

    alist1.sort()
    print('alist1 after sorting', alist1)
    alist2.sort()
    print('alist2 after sorting', alist2)

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        print('alist1[pos]=', alist1[pos])
        print('alist2[pos]=', alist2[pos])
        if alist1[pos]==alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches

print(anagramSolution2('abcde','edcba'))