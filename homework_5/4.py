src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]  # дан список
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]  # создаем новый список через однострочное выражение
print(result)
