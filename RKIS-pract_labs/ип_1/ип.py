import telebot
from telebot import types
import random
import json
import os
bot = telebot.TeleBot("7877660982:AAEpHiwXd--QNn-Ca02YrK5MyTK7U61BgiM")
user_data = {}
game_facts = [
    "Игра 'Камень, ножницы, бумага' появилась в Китае во времена династии Хань (206 до н.э. - 220 н.э.).",
    "В Японии игра называется 'Дзян-кэн' и часто используется для принятия решений.",
    "Существует чемпионат мира по игре 'Камень, ножницы, бумага' с 2002 года.",
    "В стандартной версии игры камень побеждает в 80% случаев, если игроки неопытные.",
    "Некоторые игроки используют психологические стратегии, например, повторение одного и того же хода несколько раз подряд.",
    "Существуют расширенные версии игры с дополнительными элементами, например 'Камень, ножницы, бумага, ящерица, Спок'.",
    "В 2006 году федеральный судья США приказал решить спорный случай с помощью этой игры.",
    "Математики доказали, что оптимальная стратегия - случайный выбор с равной вероятностью.",
    "В Малайзии дети играют в версию с жуком, который побеждает бумагу (потому что ест её), но проигрывает камню.",
    "Роботы могут обыгрывать людей в эту игру, анализируя движения руки человека перед ходом."
]
main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard.row(" Играть", " Факт")
main_keyboard.row(" Статистика", " Победы", "⚙ Настройки")
game_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
game_keyboard.row(" Камень", "✌ Ножницы", " Бумага")
game_keyboard.row(" Главное меню")
mode_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
mode_keyboard.row("До 1 победы", "До 3 побед")
mode_keyboard.row(" Главное меню")
def load_user_data():
    global user_data
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            user_data = json.load(file)
def save_user_data():
    with open("user_data.json", "w") as file:
        json.dump(user_data, file)
def init_user(user_id):
    if str(user_id) not in user_data:
        user_data[str(user_id)] = {
            "games_played": 0,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "current_streak": 0,
            "max_streak": 0,
            "game_history": [],
            "game_mode": "1",  # 1 или 3
            "current_game": {
                "user_wins": 0,
                "bot_wins": 0,
                "moves": []
            }
        }
def determine_winner(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "draw"
    elif (user_choice == " Камень" and bot_choice == " Ножницы") or \
            (user_choice == " Ножницы" and bot_choice == " Бумага") or \
            (user_choice == " Бумага" and bot_choice == " Камень"):
        return "user"
    else:
        return "bot"
def get_bot_choice():
    choices = [" Камень", " Ножницы", " Бумага"]
    return random.choice(choices)
def update_stats(user_id, result):
    user = user_data[str(user_id)]
    if result == "user":
        user["wins"] += 1
        user["current_streak"] += 1
        if user["current_streak"] > user["max_streak"]:
            user["max_streak"] = user["current_streak"]
    elif result == "bot":
        user["losses"] += 1
        user["current_streak"] = 0
    else:
        user["draws"] += 1
    user["games_played"] += 1
def reset_current_game(user_id):
    user_data[str(user_id)]["current_game"] = {
        "user_wins": 0,
        "bot_wins": 0,
        "moves": []
    }
def get_stats_message(user_id):
    user = user_data[str(user_id)]
    total = user["wins"] + user["losses"] + user["draws"]
    win_rate = (user["wins"] / total * 100) if total > 0 else 0
    return (
        f" Ваша статистика:\n\n"
        f" Всего игр: {total}\n"
        f" Побед: {user['wins']}\n"
        f" Поражений: {user['losses']}\n"
        f" Ничьих: {user['draws']}"
    )
def get_wins_stats_message(user_id):
    user = user_data[str(user_id)]
    total = user["wins"] + user["losses"] + user["draws"]
    win_rate = (user["wins"] / total * 100) if total > 0 else 0

    return (
        f" Статистика побед:\n\n"
        f" Процент побед: {win_rate:.1f}%\n"
        f" Текущая серия побед: {user['current_streak']}\n"
        f" Максимальная серия побед: {user['max_streak']}"
    )
def get_random_fact():
    return random.choice(game_facts)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    init_user(message.from_user.id)
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для игры в 'Камень, ножницы, бумага'.\n"
        "Выбери действие:",
        reply_markup=main_keyboard
    )
@bot.message_handler(func=lambda message: message.text == "🏠 Главное меню")
def main_menu(message):
    init_user(message.from_user.id)
    bot.send_message(
        message.chat.id,
        "Главное меню:",
        reply_markup=main_keyboard
    )
@bot.message_handler(func=lambda message: message.text == " Играть")
def play_game(message):
    init_user(message.from_user.id)
    reset_current_game(message.from_user.id)
    user_data[str(message.from_user.id)]["current_game"]["game_mode"] = user_data[str(message.from_user.id)][
        "game_mode"]
    bot.send_message(
        message.chat.id,
        "Выбери свой ход:",
        reply_markup=game_keyboard
    )
@bot.message_handler(func=lambda message: message.text == " Факт")
def show_fact(message):
    fact = get_random_fact()
    bot.send_message(
        message.chat.id,
        f" Интересный факт:\n\n{fact}",
        reply_markup=main_keyboard
    )
@bot.message_handler(func=lambda message: message.text == " Статистика")
def show_stats(message):
    init_user(message.from_user.id)
    bot.send_message(
        message.chat.id,
        get_stats_message(message.from_user.id),
        reply_markup=main_keyboard
    )
@bot.message_handler(func=lambda message: message.text == " Победы")
def show_wins_stats(message):
    init_user(message.from_user.id)
    bot.send_message(
        message.chat.id,
        get_wins_stats_message(message.from_user.id),
        reply_markup=main_keyboard
    )
@bot.message_handler(func=lambda message: message.text == " Настройки")
def settings(message):
    init_user(message.from_user.id)
    current_mode = "До 1 победы" if user_data[str(message.from_user.id)]["game_mode"] == "1" else "До 3 побед"
    bot.send_message(
        message.chat.id,
        f"Текущий режим игры: {current_mode}\nВыбери новый режим:",
        reply_markup=mode_keyboard
    )
@bot.message_handler(func=lambda message: message.text in ["До 1 победы", "До 3 побед"])
def set_game_mode(message):
    init_user(message.from_user.id)
    mode = "1" if message.text == "До 1 победы" else "3"
    user_data[str(message.from_user.id)]["game_mode"] = mode
    bot.send_message(
        message.chat.id,
        f"Режим игры изменён на: {message.text}",
        reply_markup=main_keyboard
    )
    save_user_data()
@bot.message_handler(func=lambda message: message.text in [" Камень", " Ножницы", " Бумага"])
def game_move(message):
    user_id = message.from_user.id
    init_user(user_id)
    user = user_data[str(user_id)]
    user_choice = message.text
    bot_choice = get_bot_choice()
    result = determine_winner(user_choice, bot_choice)
    user["current_game"]["moves"].append({
        "user_choice": user_choice,
        "bot_choice": bot_choice,
        "result": result
    })
    if result == "user":
        user["current_game"]["user_wins"] += 1
    elif result == "bot":
        user["current_game"]["bot_wins"] += 1
    target_wins = int(user["game_mode"])
    user_wins = user["current_game"]["user_wins"]
    bot_wins = user["current_game"]["bot_wins"]
    if user_wins >= target_wins or bot_wins >= target_wins:
        if user_wins > bot_wins:
            game_result = "Победа!"
            update_stats(user_id, "user")
        else:
            game_result = "Поражение."
            update_stats(user_id, "bot")
        user["game_history"].append(user["current_game"])
        if len(user["game_history"]) > 10:  # Ограничиваем историю
            user["game_history"] = user["game_history"][-10:]
        bot.send_message(
            message.chat.id,
            f"{game_result}\n"
            f"Ты: {user_choice}\n"
            f"Бот: {bot_choice}\n\n"
            f"Счёт: {user_wins}-{bot_wins}\n\n"
            f"Хочешь сыграть ещё?",
            reply_markup=main_keyboard
        )
        reset_current_game(user_id)
        save_user_data()
    else:
        result_text = {
            "user": "Ты выиграл этот раунд!",
            "bot": "Бот выиграл этот раунд.",
            "draw": "Ничья!"
        }[result]
        bot.send_message(
            message.chat.id,
            f"{result_text}\n"
            f"Ты: {user_choice}\n"
            f"Бот: {bot_choice}\n\n"
            f"Счёт: {user_wins}-{bot_wins}\n"
            f"Игра до {target_wins} побед.\n\n"
            f"Выбери следующий ход:",
            reply_markup=game_keyboard
        )
load_user_data()
bot.infinity_polling()