from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
import keyboard as kb
from aiogram.types import LinkPreviewOptions # Импортируем для управления ссылками
import aiosqlite
import os

import key_homew as kb_h
from crib import *
from free_level import *

router = Router()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "users_data.db")


async def init_db():
    async with aiosqlite.connect(DATABASE_PATH) as db:  # Используй полный путь
        await db.execute("CREATE TABLE IF NOT EXISTS accepted (user_id INTEGER PRIMARY KEY)")
        await db.commit()


async def is_user_accepted(user_id):
    async with aiosqlite.connect(DATABASE_PATH) as db:  # Используй полный путь
        async with db.execute("SELECT user_id FROM accepted WHERE user_id = ?", (user_id,)) as cursor:
            res = await cursor.fetchone()
            return res is not None


# 2. Объединенный хендлер принятия оферты
@router.callback_query(F.data == "contin")
async def contin(callback: CallbackQuery):
    user_id = callback.from_user.id

    # Сразу убираем состояние загрузки на кнопке
    await callback.answer()

    try:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute("INSERT OR IGNORE INTO accepted (user_id) VALUES (?)", (user_id,))
            await db.commit()

        # Редактируем старое сообщение, чтобы не спамить
        await callback.message.answer("Оферта принята! ✅\nЧем могу помочь?", reply_markup=kb.main)
        await callback.message.delete()  # Чтобы старая оферта не мозолила глаза

    except Exception as e:
        print(f"Ошибка в БД: {e}")
        await callback.message.answer("Ошибка доступа к базе данных.")

@router.message(CommandStart())
async def start(message: Message):

    user_id = message.from_user.id

        # ВАЖНО: добавлен await
    if await is_user_accepted(user_id):
        await message.answer("С возвращением! Чем займемся сегодня?", reply_markup=kb.main)
        return

    await message.answer(
        "Привет! Я **StarAnswersBot** 🎓 — твой быстрый помощник с учебой.\n\n"
        "Здесь ты найдешь готовые решения и учебные материалы в один клик.\n\n"
        "🚀 **Почему выбирают нас:**\n"
        "• Мгновенный доступ после оплаты.\n"
        "• Оплата в Telegram Stars или TON.\n"
        "• Полная анонимность.\n\n"
        "Нажимая кнопку «Продолжить», вы подтверждаете, что ознакомились и принимаете условия "
        "[Публичной оферты](https://telegra.ph/Publichnaya-oferta-na-ispolzovanie-servisa-StarAnswersBot-02-15) "
        "и подтверждаете свою дееспособность.\n\n"
        "По всем вопросам: StarAnswers176@duck.com",
        reply_markup=kb.offerta,
        parse_mode="Markdown", # Чтобы ссылка была кликабельной в тексте
        link_preview_options=LinkPreviewOptions(is_disabled=True) # Отключаем большой блок ссылки
    )

@router.message(F.text == "📚 Шпаргалка")
async def learn(message: Message):
    if not await is_user_accepted(message.from_user.id):
        await message.answer("⚠️ Пожалуйста, примите оферту в меню /start")
        return

    await message.answer("Выберите тему:", reply_markup=kb.learn)

@router.callback_query(F.data == "conditional")
async def conditional(callback: CallbackQuery):
    await callback.message.answer(CONDITIONAL1)

@router.callback_query(F.data == "cycle")
async def cycle(callback: CallbackQuery):
    await callback.message.answer(CYCLE1)
    await callback.message.answer(CYCLE2)

@router.callback_query(F.data == "strings")
async def sring(callback: CallbackQuery):
    await callback.message.answer(STRING1)
    await callback.message.answer(STRING2)

@router.message(F.text == "⚙️ Настройки/Инфо")
async def info_handler(message: Message):
    # Проверка на оферту (как в других твоих хендлерах)
    if not await is_user_accepted(message.from_user.id):
        await message.answer("⚠️ Пожалуйста, примите оферту в меню /start")
        return

    await message.answer(
        "⚙️ **Помощь и Инфо**\n\n"
        "Ты здесь, чтобы быстро закрыть задачи по Информатике. Вот как всё устроено:\n\n"
        "🚀 **Как получить код?**\n"
        "Выбираешь задание в главном меню, оплачиваешь (Stars или TON) и бот мгновенно кидает тебе готовое решение.\n\n"
        "🛡️ **Анонимность на 100%:**\n"
        "Мы не храним твои данные. Оплата в крипте или звездах не оставляет следов в истории твоих банковских карт.\n\n"
        "👇 *Выбери нужный раздел ниже:*",
        reply_markup=kb.topic, # Прикрепляем нашу клавиатуру с кнопкой-ссылкой
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "usually_questions")
async def usul_questions(cal: CallbackQuery):
    await cal.message.answer(text=""" О боте и его возможностях
❓ А училка поймет, что я списал?
Ответ: Мы пишем код «по-человечески». В нем нет заумных структур, которые не проходят в 8 классе. Код выглядит так, будто ты сам сидел и потел над ним час. Плюс, мы даем краткое пояснение — если тебя вызовут к доске, ты будешь знать, что ответить.

❓ Что если код не сработает?
Ответ: Весь код проверен на актуальных задачах Яндекс Учебника. Если Робот врежется — пиши в саппорт, разберемся или вернем TON.""")


@router.callback_query(F.data == "money_quest")
async def money_quest(cal: CallbackQuery):
    await cal.message.answer("""Почему стоит взять платное решение? 💎

Анти-палево: Мы пишем код «человеческим» языком. Училка не догадается, что это сделал ИИ или бот.

Гарантия прохода: Если что-то пойдет не так — наша поддержка решит вопрос или вернет деньги. Мы не бросаем своих.

Твои нервы: Вместо того чтобы 2 часа тупить в лабиринт, потрать 5 минут и иди гулять/играть.

Можно ли получить скидку? 💎
Ответ: Да! Приводи друга: если он купит решение, ты получишь бонус на баланс. Дешевле только делать самому (но это долго).""")


@router.callback_query(F.data == "privacy")
async def privacy(cal: CallbackQuery):
    await cal.message.answer("""🛡️ Это безопасно? Меня не вычислят?
Ответ: Нам не нужны твои ФИО, номер школы или телефон. Оплата в TON или Stars не видна в банковской истории твоих родителей (никаких чеков «За ГДЗ» в приложении банка). Для всех ты просто «инкогнито», который очень хорошо шарит в информатике.""")


@router.callback_query(F.data == "break")
async def teh_help(callback: CallbackQuery):
    await callback.message.answer(f"""📞 Техподдержка

Столкнулся с проблемой? Мы поможем!

📩 Связь через Email: StarAnswers176@duck.com
Анонимка: t.me/anonaskbot?start=wbhd66z

Чтобы мы решили твой вопрос быстро, укажи в письме:

Твой Telegram ID: {callback.from_user.id}

Скриншот задачи или ошибки.

Описание того, что случилось.

Мы отвечаем в течение дня. Твои данные используются только для решения проблемы и не хранятся после закрытия вопроса.""")

@router.message(F.text == "🚀 Решить Робота")
async def decisions(message: Message):
    if not await is_user_accepted(message.from_user.id):
        await message.answer("⚠️ Пожалуйста, примите оферту в меню /start")
        return

    await message.answer(
        " Выбирай нужный тип заданий:\n\n"
        "🟢 **Бесплатное ДЗ**\n"
        "Первые шаги и простые лабиринты. Попробуй бота в деле!\n\n"
        "🟡 **Платное ДЗ**\n"
        "Сложные задания, где нужно много условий и циклов. Готовый код + комментарии.\n\n"
        "🔴 **Самостоятельные и КР**\n"
        "Самые объемные работы. Гарантированный проход лабиринта и защита от вопросов учителя.",
        reply_markup=kb.tasks_kb,
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "tasks_free")
async def free(callback: CallbackQuery):
    await callback.message.edit_text("""Здесь собраны решения для вводных уроков.

Пользуйся, проверяй код и привыкай к пятёркам! Если робот застрянет на более сложных темах — заглядывай в платные разделы 💡
""",
                                  reply_markup=kb_h.free_main)

@router.callback_query(F.data == "tasks_premium")
async def premium(callback: CallbackQuery):
     await callback.message.edit_text("""🕒 Этот раздел находится в процессе доработки. 🔧

Следите за обновлениями! ⏰""")

@router.callback_query(F.data == "tasks_exam")
async def exam(callback: CallbackQuery):
    await callback.message.edit_text("""🤫 Это твой 'билет' в спокойную четверть.
Контрольные работы/Самостоятельные в Яндекс.Учебнике требуют идеальной логики. Мы подготовили решения, которые проходят проверку системы с первого раза.

Бонус: Если препод спросит, почему ты так быстро решил — внутри есть краткая 'шпаргалка-объяснение' алгоритма""")

@router.message(F.text == "💎 Баланс (TON)")
async def tone(message: Message):
    if not await is_user_accepted(message.from_user.id):
        await message.answer("⚠️ Пожалуйста, примите оферту в меню /start")
        return
    await message.answer("""🎁 Бонусная программа в разработке

Мы готовим систему подарков для тех, кто помогает проекту расти! Совсем скоро здесь появятся эксклюзивные решения и бесплатные доступы к платным темам за каждого приглашенного друга.""")

# ---- Decision Handlers ---- #

@router.callback_query(F.data == "back_to_levels")
async def back_to_levels(callback: CallbackQuery):
    await callback.message.edit_text(
        " Выбирай нужный тип заданий:\n\n"
        "🟢 **Бесплатное ДЗ**\n"
        "Первые шаги и простые лабиринты. Попробуй бота в деле!\n\n"
        "🟡 **Платное ДЗ**\n"
        "Сложные задания, где нужно много условий и циклов. Готовый код + комментарии.\n\n"
        "🔴 **Самостоятельные и КР**\n"
        "Самые объемные работы. Гарантированный проход лабиринта и защита от вопросов учителя.",
        reply_markup=kb.tasks_kb,
        parse_mode="Markdown"
    )

@router.callback_query(F.data == "f_1")
async def f_1(callback: CallbackQuery):
    await callback.message.edit_text("""Выберите работу ниже
👇""",
                                     reply_markup=kb_h.Simple_cycle,)

@router.callback_query(F.data == "simp_cyc1")
async def simp_cyc1(callback: CallbackQuery):
    await callback.message.answer(f"№1\n{simp_cyc1_1}")
    await callback.message.answer(f"№2\n{simp_cyc1_2}")
    await callback.message.answer(f"№3\n{simp_cyc1_3}")
    await callback.message.answer(f"№4\n{simp_cyc1_4}")
    await callback.message.answer(f"№5\n{simp_cyc1_5}")
    await callback.answer()

@router.callback_query(F.data == "simp_cyc2")
async def simp_cyc2(callback: CallbackQuery):
    await callback.message.answer(f"№1\n{simp_cyc2_1}")
    await callback.message.answer(f"№2\n{simp_cyc2_2}")
    await callback.message.answer(f"№3\n{simp_cyc2_3}")
    await callback.message.answer(f"№4\n{simp_cyc2_4}")
    await callback.answer()

# @router.callback_query(F.data == "m_1")
# async def m_1(callback: CallbackQuery):
#     await callback.message.edit_text()







