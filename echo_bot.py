import telebot
import random 


shadow_word = "WE WILL MAKE AMERICA GREAT AGAIN" 
bot = telebot.TeleBot("1561483182:AAFTLgf0yygyMR2kOJJxJJW_PM-b8a6BVVM")
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я -  emodji bot.Я посылаю тебе эмоджи в качестве ответов. Также я храню один секрет, который узнает только избранный')
    

@bot.message_handler(commands = ['give'])
def get_text_messages(message):
    global mess
    mess = ""
    global smile_array
    global sad_array
    smile_array = ["😂","😀","😄","😁","😆","😂","🤣","😊"]
    sad_array = ["😡","😕","😟","😞","😔","😣","😖"]
    lensad = len(sad_array)
    lensmile = len(smile_array)
    for word in shadow_word:
        if word != " ": 
            encryel = ord(word) - 65
            encryel=bin (encryel)
            for element in range(2,len(encryel)):
                if encryel[element] == '0':
                    randel = random.randint (0,lensad-1)
                    mess = mess + sad_array[randel]
                    #bot.reply_to(message, sad_array[randel])
                else:
                    randel1 = random.randint (0,lensmile-1)
                    mess = mess + smile_array[randel1]
                    #bot.reply_to(message, smile_array[randel1])
            mess = mess + "🔑"
        # else:
        #     #bot.reply_to(message,"🙅‍♀️")
        #     mess = mess + "🙅‍♀️"
        #     mess = mess + "🔑"
    bot.send_message(message.from_user.id, mess)

@bot.message_handler(commands = ['translate'])
def encrypt_text(message):
    decasci = []
    word2=""
    for element in range(0,len(mess)):
        if mess[element] in smile_array:
            word2 = word2+"1"
        elif mess[element] in sad_array:
            word2 = word2+"0"
        elif mess[element] == "🙅‍♀️":
            decasci.append(" ")
            continue
        elif mess[element]=="🔑":
            word2 = int(word2,2) + 65
            word2 = chr(word2)
            decasci.append(word2)
            word2 = ""

            

    finish = ""
    for el in decasci:
        finish = finish + el
    bot.send_message(message.from_user.id, finish)       
        

@bot.message_handler(content_types=['text','document'])
def hello(message): 
    if message.text == 'hello' or message.text == 'hi':
        bot.send_message(message.from_user.id, "✌️")
    if message.text == 'goodbye':
        bot.send_message(message.from_user.id, "🙋‍♂️")

bot.polling()
 
## 'message' -> encryption -> ascii-> emodjination -> send in chat
