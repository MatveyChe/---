from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from states import Form
from aiogram.fsm.context import FSMContext


router = Router()

data = ['1', '2', '3', '4', '5']
i = 0
s = ''


@router.message(Command('start'))
async def start(message: Message, state: FSMContext):
    await message.reply(f'Привет! Я бот-литератор. Я буду скидывать строки стихотворения, а ты должен их правильно повторить. Сейчас я скину первую строку')
    global i
    i = 0
    await message.reply(data[i])
    await state.set_state(Form.bot_str)


@router.message(Command('stop'))
async def start(message: Message, state: FSMContext):
    await message.reply(f'Всего доброго! Хочешь повторить? Тогда нажимай снова /start')
    await state.set_state()
    global i
    i = 0


@router.message(Form.suphler)
async def suphler(message: Message, state: FSMContext):
    k = 0
    global s, i
    s += ' ' * (len(data[i]) - len(s))
    for j in range(len(data[i])):
        if s[j] != data[i][j]:
            k += 1
    await state.set_state(Form.bot_str)
    await message.reply(f'у тебя ошибка в {k} символах, сейчас я ещё раз выведу строку, попробуй еще раз')
    await message.reply(data[i])


@router.message(Form.bot_str)
async def send_str(message: Message, state: FSMContext):
    global i
    txt = message.text
    if i + 1 < len(data):
        if txt == data[i]:
            i += 1
            await message.reply(f'Молодец! вот следующая строка')
            await message.reply(data[i])
        else:
            await message.reply(f'Неправильно( Напиши ок, чтобы продолжить')
            await state.set_state(Form.suphler)
    else:
        await message.reply(f'Ты прошёл, поздравляю! Хочешь повторить? Тогда снова нажимай /start')
        await state.set_state()
        i = 0
