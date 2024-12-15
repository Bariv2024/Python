storage_devices = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

def convert_bytes(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:          #переводим в более удобные измерения
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024

try:
    device_number = int(input("Введите номер накопителя (от 1 до {}): ".format(len(storage_devices))))  #запрашиваем у пользователя номер накопителя
    if device_number < 1 or device_number > len(storage_devices):
        raise ValueError
except ValueError:
    print("Неверный номер накопителя. Пожалуйста, введите число от 1 до {}.".format(len(storage_devices)))
    exit(1)

selected_device = storage_devices[device_number - 1]                 #информация о накопителе
total_memory = selected_device['total']
used_memory = selected_device['used']
free_memory = total_memory - used_memory
free_memory_percent = (free_memory / total_memory) * 100

free_memory_gb = free_memory / (1024 ** 3)  # вычисляем количество и процент свободной памяти и переводим байты в гигабайты

if free_memory_gb < 10 or free_memory_percent < 5:
    print(f"На накопителе {device_number} критически мало свободного места")             #вывод сообщения
elif free_memory_gb < 30 or free_memory_percent < 10:
    print(f"На накопителе {device_number} мало свободного места")
else:
    print(f"На накопителе {device_number} достаточно свободного места")