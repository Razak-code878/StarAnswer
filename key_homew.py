from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# -- Free-level of study
free_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="№1: Простые циклы", callback_data="f_1")],
    [InlineKeyboardButton(text="⬅️ К уровням", callback_data="back_to_levels")]
])

Simple_cycle = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Домашняя работа «Цикл FOR»"
                               "(5 карточек)", callback_data="simp_cyc1")],
    [InlineKeyboardButton(text="Практическая работа «Цикл FOR»"
                               "(4 карточки)", callback_data="simp_cyc2")],
    [InlineKeyboardButton(text="⬅️ К уровням", callback_data="back_to_levels")]
])

# -- Medium_level of study --
medium_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="№1: Циклы 💎", callback_data="m_1")],
    [InlineKeyboardButton(text="⬅️ К уровням", callback_data="back_to_levels")]
])

# -- Hard-level of study --
hard_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🏆«Цикл FOR»"
                               "(5 карточек)", callback_data="h_exam2")],
    [InlineKeyboardButton(text="СР «Цикл WHILE»"
                               "(11 карточек)")],
    [InlineKeyboardButton(text="⬅️ К уровням", callback_data="back_to_levels")]
])