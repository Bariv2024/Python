#Вы получили такую строку логов:
#'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
#Совершите над ней следующие действия:

#1.1. Выделите и выведите на экран дату и время.

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
data_time = logs.split()
data_time_pr = ' '.join(data_time[0:3])
print('Дата и время:', data_time_pr)

#1.2. Выделите и выведите на экран название сервиса (systemd[1]), записавшего лог.

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
service = logs.split()
service_systemd = service[4].split(':')[0]
print('Название сервиса:', service_systemd )

#1.3. Замените название ПК (ideapad) на   PC-12092 , выведите полученную строку на экран.

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
logs_new = logs.replace('ideapad', 'PC-12092')
print(logs_new)

#1.4. Найдите в логе слово failed и выведите его позицию, если такого слова нет, выведите -1.

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
if 'failed' in logs:
    print(logs.find('failed'))
else:
    print('-1')

#1.5. Посчитайте количество букв 'S' в строке вне зависимости от регистра (и прописных, и заглавных).

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
total = logs.lower().count('s')
print(total)

#1.6. Выделите из строки значения часов, минут и секунд, суммируйте эти 3 числа и выведите полученное число на экран.

logs = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'
time = logs.find('12:48:31')
timers = logs[time:time + 8]
hours, minutes, seconds = timers.split(':')
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)
summa = hours + minutes + seconds
print(summa)

#Вы получили такую строку логов:
#'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'
#Нужно сформировать и вывести сообщение в таком формате:

#The PC "<имя ПК>" receive message from service "<имя сервиса>" what says "<сообщение>" because "<причина ошибки>" at <дата, время>

logs = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'

parts = logs.split()

pc = parts[3]

service = parts[4].split('[')[0]

message = ' '.join(parts[5:9])

error = ' '.join(parts[11:14])

date_time = ' '.join(parts[:3])

formatted_message = f'The PC "{pc}" receive message from service "{service}" what says "{message}" because "{error}" at {date_time}'

print(formatted_message)

