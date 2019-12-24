from config import bot
import qrcode
import time

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'''
👋 Привет, {message.chat.username}.
Мое имя QRcodeBot, и я умею делать QR-code из текста который вы отправите мне :)
Отправьте мне любой текст и я в миг сделаю для вас QR-code.
''', parse_mode='Markdown')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'''
Что бы сделать QR-code напиши мне любое сообщение и я со скоростью света реализую его тебе
    ''')


@bot.message_handler(content_types=['text'])
def create_qrcode(message):
    do = message.text
    bot.send_message(message.chat.id, 'Начинаю делать QR-code по слову: ' + do)
    img = qrcode.make(do)
    img.save('QR-code.png')

    bot.send_photo(message.chat.id, photo=open('/home/dizinnes/PycharmProjects/QRcodeBot/QR-code.png', 'rb'))


@bot.message_handler(content_types=['photo'])
def know_qrcode(message):
    bot.send_message(message.chat.id, 'Вы отрпавили фото!')
    photo = message.chat.photo
    bot.send_message(message.chat_id, 'Принял фото сейчас же буду рассшифрововать: ' + photo)


bot.polling()