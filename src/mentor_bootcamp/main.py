def devibe_numbers(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        print("Нельзя делить на 0")
        return None
    except TypeError:
        print(f"Одно и чисел не число: {a, b}")
        return None
    finally:
        print("Операция завершена")

devibe_numbers(10, "два")