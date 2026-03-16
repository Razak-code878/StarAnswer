from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# 1. Оферта (Вход в бота)
offerta = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="⚡ Согласен, погнали!", callback_data="contin")],
])

# 2. Главное меню (Исправлено: в ReplyKeyboard используем текст, а не callback)
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="🚀 Решить Робота"), KeyboardButton(text="📚 Шпаргалка")],
    [KeyboardButton(text="⚙️ Настройки/Инфо"), KeyboardButton(text="💎 Баланс (TON)")]
], resize_keyboard=True)

# 3. Справочник (Обучение)
learn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="✅ Условия (if/else)", callback_data="conditional")],
    [InlineKeyboardButton(text="🔁 Циклы (while/for)", callback_data="cycle")],
    [InlineKeyboardButton(text="💬 Строки и Робот", callback_data="strings")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
])

# 4. Информация и Безопасность (Твое меню с иконками)
# Сделал подписи понятнее, чтобы юзер знал, на что жмет
topic = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="💰 Прайс", callback_data="money_quest"),
        InlineKeyboardButton(text="❓ FAQ", callback_data="usually_questions"),
        InlineKeyboardButton(text="🛡️ Анонимность", callback_data="privacy")
    ],
    [InlineKeyboardButton(text="🆘 Техподдержка", callback_data="break")]
])

tasks_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📗 ДЗ: Базовые уровни (Бесплатно)", callback_data="tasks_free")],
    [InlineKeyboardButton(text="📘 ДЗ: Продвинутые уровни (Stars/TON)", callback_data="tasks_premium")],
    [InlineKeyboardButton(text="🔥 СР и Контрольные (TON/Stars)", callback_data="tasks_exam")],
    [InlineKeyboardButton(text="⬅️ Назад", callback_data="back_to_main")]
])