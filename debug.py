my_list = [1, 2, 3, 4, 5]

# Повторяем список нужное количество раз
repeated_list = my_list * 3

for i, item in enumerate(repeated_list):
    # Используем оператор % (остаток от деления) для получения индекса элемента в оригинальном списке
    original_index = i % len(my_list)
    original_item = my_list[original_index]
    print(original_item)