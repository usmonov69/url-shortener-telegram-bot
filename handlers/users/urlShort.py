from aiogram import types 
from aiogram.dispatcher.filters import Regexp

from loader import dp
from utils.misc.urlShortener import shortener

URL_CHECK=r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"



@dp.message_handler(content_types=['photo','sticker','video','audio'])
async def unknow_img(message:types.Message):
	await message.reply("Iltimos URL manzil yuboring! \n\n<i>masalan</i>: https://www.youtube.com/c/LofiGirl")


@dp.message_handler()
async def check_url(msg:types.Message):
	word_id = msg.text
	get_urls = shortener(word_id)
	result = []
	if get_urls:
		await msg.answer(get_urls)
	else:
		await msg.reply("Iltimos URL manzil yuboring! \n\n<i>masalan</i>: https://www.youtube.com/c/LofiGirl")

