def checkio(words: str) -> bool:
    count = 0
    # Получаем список из строки с разделением по пробелу.
    words = words.split()
    # Проходим по списку.
    for now in words:
        if now.isalpha():
            # Если значение состоит только из букв, увеличиваем счетчик на + 1.
            count += 1
            # Если счетчик >= 3, прерываем цикл.
            if count >= 3:
                break
        else:
            count = 0
    return True if count >= 3 else False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
