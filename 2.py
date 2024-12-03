logs = [
    "May 18 11:59:18   PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated",
    "May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.",
    "May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...",
    "May 20 11:01:12   PC-00102 PackageKit: daemon start",
    "May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...",
    "May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00",
    "May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: \"/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4\"",
    "May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device",
    "May 23 08:06:14   PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio",
    "May 24 16:19:52   PC-00233 systemd[1116]: Reached target Sound Card.",
    "May 24 19:26:40   PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users."
]
#Создайте алгоритм заполнения словаря, подходящий для любой строчки лога. Словарь должен содержать в себе такую информацию:

# 'time': <дата/время>
# 'pc_name': <имя компьютера>
# 'service_name': <имя сервиса>
# 'message': <сообщение лога>

def parse_log_entry(log_entry):
    parts = log_entry.split(maxsplit=3)
    time = f"{parts[0]} {parts[1]} {parts[2]}"
    pc_name = parts[3].split()[0]
    service_message = ' '.join(parts[3].split()[1:])
    service_name = service_message.split(':')[0]
    message = ':'.join(service_message.split(':')[1:]).strip()
    log_dict = {
        'time': time,
        'pc_name': pc_name,
        'service_name': service_name,
        'message': message
    }
    return log_dict

parsed_logs = [parse_log_entry(entry) for entry in logs]

for log in parsed_logs:
    print(log)


#Заполните словарь для одной из строк лога с помощью данного алгоритма, запросив у пользователя номер строки с помощью input().

try:
    line_number = int(input("Введите номер строки лога (от 1 до {}): ".format(len(logs))))
    if 1 <= line_number <= len(logs):
        log_entry = logs[line_number - 1]
        log_dict = parse_log_entry(log_entry)
        print(f"{log_dict['pc_name']}: {log_dict['message']}")
    else:
        print("Неверный номер строки.")
except ValueError:
    print("Пожалуйста, введите целое число.")

#Список
literal_list = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']

# Создайте список ключей
keys = ['time', 'pc_name', 'service_name', 'message']

#Используя функцию zip(), создайте словарь из этих двух списков
result_dict = dict(zip(keys, literal_list))

print(result_dict)

# Создаем список словарей из последнего элемента parsed_logs и result_dict
list_of_dicts = [parsed_logs[-1], result_dict]
print(list_of_dicts)

# Преобразуем значения словарей во множества и находим совпадающие значения
set_values_1 = set(parsed_logs[-1].values())
set_values_2 = set(result_dict.values())

common_values = set_values_1.intersection(set_values_2)
common_values_list = list(common_values)

print(common_values_list)