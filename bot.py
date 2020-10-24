import discord
import json
import requests
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')  # Get-запрос
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Fox')  # Создание Embed'a
    embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
    await ctx.send(embed=embed)  # Отправляем Embed


@bot.command()  # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def who_is_landex(ctx):  # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author  # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(
        f'Landex is 100% gay, {author.mention}!')  # Выводим сообщение с упоминанием автора, обращаясь к переменной author.


bot.run(settings['token'])  # Обращаемся к словарю settings с ключом token, для получения токена
