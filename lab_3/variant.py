from pygost import gost34112012256
print(gost34112012256.new("Дубинин Артем Олегович".encode('utf-8')).digest().hex()[-1])
