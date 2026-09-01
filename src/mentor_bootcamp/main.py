def divide_numbers(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Нельзя делить на 0")
        return None
    except TypeError:
        print(f"Одно и чисел не число: {a, b}")
        return None
    else:
        return res
    finally:
        print("Операция завершена")

print(divide_numbers(10, 2))
print(divide_numbers(10, "два"))
print(divide_numbers(10, 0))