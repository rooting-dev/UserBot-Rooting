from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import ChatPermissions
import time
from time import sleep
import random
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

api_id = config["pyrogram"]["api_id"]
api_hash = config["pyrogram"]["api_hash"]

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = ""
    typing_symbol = "▒"

    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)

        except FloodWait as e:
            sleep(e.x)

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0

    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 3)
            sleep(0.1)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)

    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0

    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)

            perc += random.randint(1, 5)
            sleep(0.15)

        except FloodWait as e:
            sleep(e.x)

    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    chat = msg.text.split(".thanos ", maxsplit=1)[1]

    members = [
        x
        for x in app.iter_chat_members(chat)
        if x.status not in ("administrator", "creator")
    ]

    random.shuffle(members)

    app.send_message(chat, "Щелчок Таноса ... *щёлк*")

    for i in range(len(members) // 2):
        try:
            app.restrict_chat_member(
                chat_id=chat,
                user_id=members[i].user.id,
                permissions=ChatPermissions(),
                until_date=int(time.time() + 86400),
            )
            app.send_message(chat, "Исчез " + members[i].user.first_name)
        except FloodWait as e:
            print("> waiting", e.x, "seconds.")
            time.sleep(e.x)

    app.send_message(chat, "Но какой ценой?")

@app.on_message(filters.command("snos", prefixes=".") & filters.me)
def snos(_, msg):
    try:
        username = msg.text.split(".snos ", maxsplit=1)[1]
    except:
        msg.edit("❌ Использование: .snos username")
        return
    
    msg.edit(f"🎯 Начинаю отправку репортов на аккаунт @{username}...")
    sleep(2)
    
    msg.edit(f"🎯 Начинаю отправку репортов на аккаунт @{username}..")
    sleep(2)
    
    msg.edit(f"🎯 Начинаю отправку репортов на аккаунт @{username}.")
    sleep(2)
    
    steps = ["Подготовка прокси...", "Обход защиты...", "Маскировка запросов...", "Отправка жалоб..."]
    for step in steps:
        msg.edit(f"🎯 {step}")
        sleep(random.uniform(1.5, 2.5))
    
    sent = random.randint(700, 930)
    failed = random.randint(400, 686)
    
    result = f"""✅ Отчет по репортам @{username}

📤 Отправлено: {sent}
❌ Не дошло: {failed}
📊 Всего попыток: {sent + failed}

🔞 Аккаунт получил ограничения!
⚡️ Работа завершена."""
    
    msg.edit(result)

app.run()