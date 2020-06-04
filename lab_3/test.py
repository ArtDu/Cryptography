import ctypes
 
# Загрузка библиотеки в ctypes.
libc = ctypes.CDLL("./libsha256.so")
 
# Вызов функции С из библиотеки.
# ans = libc.sha2("abc", 64)
# print(ans)


# Указываем, что функция возвращает char
libc.sha2.restype = ctypes.c_char
# Указываем, что функция принимает аргументы int, double. char, short
libc.sha2.argtypes = [ctypes.c_char, ctypes.c_int]

print(libc.sha2("a".encode('utf-8'), 64).decode("utf-8"))