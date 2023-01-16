from aiogram import Bot, Dispatcher, types, executor
import config
import sqlite3

bot = Bot(token = config.token)
dp = Dispatcher(bot)

connect = sqlite3.connect('users.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    id_user INTEGER,
    chat_id INTEGER
    );
    """)
connect.commit()


@dp.message_handler(commands= ['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text='Backend'),
        types.KeyboardButton(text='Frontend'),
        types.KeyboardButton(text='UXUI'),
        types.KeyboardButton(text='Android'),
        types.KeyboardButton(text='IOS')
    )
    


    cursor = connect.cursor()
    cursor.execute(f"SELECT id_user FROM users WHERE id_user = {message.from_user.id};")
    res = cursor.fetchall()
    if res == []:
        cursor.execute(f"""INSERT INTO users VALUES ('{message.from_user.username}', 
                        '{message.from_user.first_name}', '{message.from_user.last_name}', 
                        {message.from_user.id}, {message.chat.id})""")
    connect.commit()
    await message.answer(
        text= f"Здраствуйте, {message.from_user.full_name}!",
        reply_markup=keyboard
        )
    
@dp.message_handler(text='Backend')
async def backend(message: types.Message):
    await message.answer(
        text= "Backend — это внутренняя часть сайта и сервера и т.д Стоимость 10000 сом в месяц  Обучение: 5 месяц"
    )
@dp.message_handler(text='Frontend')
async def frontend(message: types.Message):
    await message.answer(
        text= "FrontEnd разработчик создает видимую для пользователя часть веб-страницы и его главная задача – точно передать в верстке то, что создал дизайнер, а также реализовать пользовательскую логику. Стоимость 10000 сом в месяц  Обучение: 5 месяц"
    )
    
@dp.message_handler(text='UXUI')
async def uxui(message: types.Message):
    await message.answer(
        text= "UX/UI-дизайнер ― одна из самых востребованных сегодня профессий на рынке. В этом материале мы подробно разбираем, кто такой UX/UI-дизайнер и почему UX/UI-дизайн ― не только про графику. Стоимость 10000 сом в месяц  Обучение: 5 месяц"
    )
    
@dp.message_handler(text='Android')
async def android(message: types.Message):
    await message.answer(
        text= "Он пишет код для устройств, которые работают на операционной системе Android. Стоимость 10000 сом в месяц  Обучение: 5 месяц"
    )
    
@dp.message_handler(text='IOS')
async def ios(message: types.Message):
    await message.answer(
        text= "iOS-разработчик создаёт приложения для устройств Apple. Стоимость 10000 сом в месяц  Обучение: 5 месяц"
    )

@dp.message_handler(commands='help')
async def help(message: types.Message):
    await message.reply(f"Вот мои комманды: ")
    
   
executor.start_polling(dp)