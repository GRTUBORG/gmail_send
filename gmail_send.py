import smtplib

from email.mime.multipart import MIMEMultipart  # Многокомпонентный объект
from email.mime.text import MIMEText  # Текст/HTML

print('Внимание! Пока что доступна отправка только с почты Google.')
addr_from = input('Введите почту отправителя (только gmail): ')
addr_to = input('Введите почту адресата: ')
password = input('Введите пароль для почты отправителя: ')

msg = MIMEMultipart()  # Создаем сообщение
msg['From'] = addr_from  # Адресат
msg['To'] = addr_to  # Получатель
msg['Subject'] = input('Введите тему сообщения: ')

body = input('Введите текст Вашего сообщения: ')
msg.attach(MIMEText(body, 'plain'))

print('Пожалуйста, подождите. Пытаюсь подключиться к серверу Google по вашим данным.')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
try:
    server.login(addr_from, password)
    print('CONNECTION [OK]')
    server.send_message(msg)
    print('SEND MAIL [OK]')
    server.quit()
    print('DONE!')
except:
    print('CONNECTION [NO] \nПроверьте правильность введённых данных!')
