from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


b1 = KeyboardButton("Darsliklar 📙")
b2 = KeyboardButton("Badiiy kitoblar 📖")
b3 = KeyboardButton("Kitob qidirish 🔎")
b4 = KeyboardButton("Kutubxona hujjatlari 📑")

m = ReplyKeyboardMarkup(resize_keyboard=True)
m.add(b1).add(b2, b3).add(b4)


btn1 = KeyboardButton("1-Sinf darsliklari 📚")
btn2 = KeyboardButton("2-Sinf darsliklari 📚")
btn3 = KeyboardButton("3-Sinf darsliklari 📚")
btn4 = KeyboardButton("4-Sinf darsliklari 📚")
btn5 = KeyboardButton("5-Sinf darsliklari 📚")
btn6 = KeyboardButton("6-Sinf darsliklari 📚")
btn7 = KeyboardButton("7-Sinf darsliklari 📚")
btn8 = KeyboardButton("8-Sinf darsliklari 📚")
btn9 = KeyboardButton("9-Sinf darsliklari 📚")
btn10 = KeyboardButton("10-Sinf darsliklari 📚")
btn11 = KeyboardButton("11-Sinf darsliklari 📚")
btn12 = KeyboardButton("🔙 Asosiy menyuga")
mr = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
mr.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10).add(btn11).add(btn12)
