import telebot
import random
import os
from пароли import pp
from calculator import c   
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7949420172:AAFFtNiIaYmMhwrFDsxNPS5xEWfHm_tMJuk")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши /hello,/mem,/calculator,/passford,/факт,/duck")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['mem'])
def send_mem(message):
     list=os.listdir('images')
     img_name=random.choice(list)
     with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  
@bot.message_handler(commands=["calculator"])
def send_calculator(message):
    bot.reply_to(message,"Напишите пример:")
    bot.register_next_step_handler(message,calculator)
def calculator(message):
    l=message.text 
    n1=l[0]
    n2=l[2]
    z=l[1]
    result=c(int(n1),int(n2),z)
    bot.reply_to(message, f" Результат: {result}")
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


     

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['passford'])
def lenn(message):
    bot.reply_to(message,"Какая длина пароля?")
    bot.register_next_step_handler(message,send_passford)
def send_passford(message):
    p=pp(int(message.text))
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {p}")

@bot.message_handler(commands=['факт'])
def send_fact(message):
    f=["Недавно на черном море произошла огромная экологическая проблема. С этим работают большое количество экологов и волонтеров из разных городов",
     "Истощение природных ресурсов. Для этого людт сажают деревья, обагащаются поля с рожью.",
     "Загрезнение атмосферного воздуха. Чтобы исправить эту ситуацию люди придумали электрическиемашины, ставят фильтры на трубя заводов",
     "Сокращение популяции некоторых видов животных, что приводит к нарушению большой биологической цепочки. Для этого люди ставят заповедники где нельзя охотиться на этих животных.",
     "Загрезнение водоемов. Чтобы устранить эту проблему сделали огромный щтраф нарушителю, а также запускают разные виды жителей водоемов кто ест этот мусор"]
    r=random.choice(f)
    bot.reply_to(message, f" факт: {r}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
def get_images_url():
    url="https://random-d.uk/api/random"
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=["duck"])
def duck(message):
    image_url=get_images_url
    bot.set_message(message.chat.id,image_url)







bot.polling()