import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from discord import Activity, ActivityType
import random
from discord import Embed, Member
from discord.ext import commands
from asyncio import TimeoutError
import datetime, pyowm
import json
import nekos
from discord.utils import get

import os
from time import sleep
import requests


Bot = commands.Bot(command_prefix="#")
Bot.remove_command('help')

Arguments = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof']
def is_nsfw():
    async def predicate(ctx):
        return ctx.channel.is_nsfw()
    return commands.check(predicate)

@Bot.command()
@is_nsfw()
async def cum(ctx):
    emb = discord.Embed(color=0xebebeb)
    emb.set_image(url=nekos.img('cum'))
    await ctx.send(embed=emb)

@Bot.command()
async def actions(ctx):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    emb = discord.Embed(title='Действия',color = random.choice(colours5))
    emb.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field( name = '`{}hug`'.format( "#" ), value = 'Обнять.')
    emb.add_field( name = '`{}tickle`'.format( "#" ), value = 'Пощекотать.')
    emb.add_field( name = '`{}cuddle`'.format( "#" ), value = 'Прижаться.')
    emb.add_field( name = '`{}kiss`'.format( "#" ), value = 'Поцеловать.')
    emb.add_field( name = '`{}pat`'.format( "#" ), value = 'Гладить.')
    emb.add_field( name = '`{}slap`'.format( "#" ), value = 'Пощечина.')
    emb.add_field( name = '`{}wink`'.format( "#" ), value = 'Подмигнуть.')
    emb.add_field( name = '`{}sex`'.format( "#" ), value = 'Занятся сексом.')
    emb.add_field( name = '`{}vrot`'.format( "#" ), value = 'Дать в рот.')
    emb.add_field( name = '`{}otliz`'.format( "#" ), value = 'Лизнуть.')
    emb.add_field( name = '`{}smoke`'.format( "#" ), value = 'Курить.')
    emb.add_field( name = '`{}hello`'.format( "#" ), value = 'Передать привет через бота в ЛС.')
    emb.add_field( name = '`{}gey`'.format( "#" ), value = 'Проверь сам.')
    await ctx.send(embed=emb)

@Bot.command()
async def hug(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    huggg = ['https://i.some-random-api.ml/zSKMG85bIg.gif', 'https://acegif.com/wp-content/gif/anime-hug-20.gif', 'https://acegif.com/wp-content/gif/anime-hug-83.gif', 'https://pa1.narvii.com/6392/c5365d892718425ea58371b8d4e6fc64e29f6902_hq.gif', 'https://anime-chan.me/uploads/posts/2014-09/1411477272_jinsei-episode12-omake-6.gif']

    embed = discord.Embed(color = random.choice(colours5), title = 'Обнятие.')
    embed.description = f"{ctx.author.mention} Вы обняли {member.mention}."
    embed.set_image(url = random.choice(huggg)) 
    await ctx.send(embed = embed) 


@Bot.command()
async def pat(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    patt = ['https://i.some-random-api.ml/eT58KYZl8I.gif', 'https://pa1.narvii.com/6390/65b91c940fecd2659b194c51351950358cb9d047_hq.gif', 'https://kinogud.files.wordpress.com/2019/08/original.gif']

    embed = discord.Embed(color = random.choice(colours5), title = 'Погладить.')
    embed.description = f"{ctx.author.mention} гладит {member.mention}."
    embed.set_image(url = random.choice(patt))
    await ctx.send(embed = embed)

@Bot.command()
async def wink(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    winkk =('https://i.some-random-api.ml/yoPiQCP6DM.gif', 'https://i.gifer.com/4Z2R.gif', 'https://pa1.narvii.com/6389/da61d5d8b4bc7b8fa5f5da49016b4d9c5a1a1893_hq.gif')
    
    embed = discord.Embed(color = random.choice(colours5), title = 'Подмигивать.')
    embed.description = f"{ctx.author.mention} подмигивает {member.mention}."
    embed.set_image(url = random.choice(winkk))
    await ctx.send(embed = embed)

@Bot.command()
async def tickle(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    tickkle = ['https://i.gifer.com/KVjQ.gif', 'https://i.gifer.com/O4QR.gif', 'https://66.media.tumblr.com/e6d1a1cd2499e37f14118a75d5e36da4/tumblr_og7p24fa3R1vpbklao6_500.gifv']

    embed = discord.Embed(color = random.choice(colours5), title = 'Пощекотать.')
    embed.description = f"{ctx.author.mention} щекочет {member.mention}."
    embed.set_image(url = random.choice(tickkle)) 
    await ctx.send(embed = embed) 
@Bot.command()
async def cuddle(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    cuddlee = ['https://data.whicdn.com/images/241295638/original.gif', 'https://im0-tub-ru.yandex.net/i?id=26fa1e1f6e191b598ce4148c6bab699e-srl&n=13']

    embed = discord.Embed(color = random.choice(colours5), title = 'Прижаться.')
    embed.description = f"{ctx.author.mention} прижимается к {member.mention}."
    embed.set_image(url = random.choice(cuddlee)) 
    await ctx.send(embed = embed) 

@Bot.command()
async def slap(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    slappp = ['https://i.gifer.com/79zo.gif', 'https://safebooru.org/images/1882/605143df221803e99f3b5423f1df4c8b76bd8ae9.gif?1964756', 'https://i.kym-cdn.com/photos/images/original/001/040/951/73e.gif']

    embed = discord.Embed(color = random.choice(colours5), title = 'Пощечина.')
    embed.description = f"{ctx.author.mention} дал(а) леща {member.mention}."
    embed.set_image(url = random.choice(slappp)) 
    await ctx.send(embed = embed) 

@Bot.command()
async def kiss(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    kisss = ['https://data.whicdn.com/images/294084710/original.gif', 'https://im0-tub-ru.yandex.net/i?id=891bd2b6228afa51bd76bc2c61050a17&n=13']

    embed = discord.Embed(color = random.choice(colours5), title = 'Поцеловать.')
    embed.description = f"{ctx.author.mention} поцеловал(а) {member.mention}."
    embed.set_image(url = random.choice(kisss)) 
    await ctx.send(embed = embed)

@Bot.command()
async def sex(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    sexx = ['https://erogif.ru/wp-content/uploads/2020/04/Hentaj-porno-anime-gifki-anal-ebut-v-popu-12.gif', 'https://images-ext-1.discordapp.net/external/eOp5lNxwwNY1QZCc-PZnCFdptfY24qf9axDqyoqKn84/https/cdn.nekos.life/cum/Cum_114.gif', 'https://images-ext-1.discordapp.net/external/CfEwRVLWN-fk0j5Y5APrA4a9BtUGUoQ72OHpE4GjJRw/https/cdn.nekos.life/cum/Cum_162.gif']
    embed = discord.Embed(color = random.choice(colours5), title = 'Sexy.')
    embed.description = f"{ctx.author.mention} выкимал(а) {member.mention}."
    embed.set_image(url = random.choice(sexx)) 
    await ctx.send(embed = embed)

@Bot.command()
async def vrot(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    vrott = ['', 'https://media.discordapp.net/attachments/851844222046961705/858753450074832896/image0.jpg', 'https://media.discordapp.net/attachments/851844222046961705/858752299298848798/image0.jpg']

    embed = discord.Embed(color = random.choice(colours5), title = 'Высунул и.')
    embed.description = f"{ctx.author.mention} дал в ротик {member.mention}."
    embed.set_image(url = random.choice(vrott))
    await ctx.send(embed = embed)

@Bot.command()
async def otliz(ctx, member: discord.Member):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    otlizz = ['https://i.imgur.com/7dPB1Zt.gif']

    embed = discord.Embed(color = random.choice(colours5), title = 'Лизнул(а).')
    embed.description = f"{ctx.author.mention} отлизал(а) пятку {member.mention}."
    embed.set_image(url = random.choice(otlizz))
    await ctx.send(embed = embed)

@Bot.command()
async def smoke(ctx):
    await ctx.message.delete()
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    smokee = ['https://pa1.narvii.com/6545/8e93c0dddb94961912a7c1dd60a5dfae243ddaf5_hq.gif', 'https://99px.ru/sstorage/86/2015/07/image_861307151145351751585.gif', 'https://thumbs.gfycat.com/CanineElderlyAmazonparrot-size_restricted.gif']

    embed = discord.Embed(color = random.choice(colours5), title = 'Поджег сигарету указательным пальчиком.')
    embed.description = f"{ctx.author.mention} сигарета прикурилась, вокруг масса смол."
    embed.set_image(url = random.choice(smokee))
    await ctx.send(embed = embed)

@Bot.command(aliases=['бан'])
@commands.has_permissions(view_audit_log=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason = reason)
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969] #цвет в формате 0xHEX
    emb = discord.Embed(title=f':octagonal_sign: | Блокировка Пользователя __{member.name}__',description=f'\n:red_square: **Подробная информация про бан:**',color = random.choice(colours5))
    emb.set_footer(text=f'| Вызвано Администратором: {ctx.author.name}', icon_url= ctx.author.avatar_url)
    emb.set_thumbnail(url= member.avatar_url)
    emb.add_field(name=':shield:| Имя Нарушителя:',value = member.mention)
    emb.add_field(name=':drum:| Айди Нарушителя:',value = member.id)
    emb.add_field(name=':ring:| Тег Нарушителя:',value = member.discriminator)
    emb.add_field(name=':joystick:| Причина Нарушения:',value = reason)
    emb.add_field(name=':beginner:| Дата регестрации аккаунта:',value = ctx.author.created_at.strftime("%d.%m.%Y %H:%M:%S"))
    emb.add_field(name=':notebook:| Дата присоедениния: ', value = f'{ctx.author.joined_at.strftime("%d.%m.%Y %H:%M:%S")}')
    await member.send( f'{ member.mention }, Вы получили **бан** на сервере **ST Comunity!** **Выдал бан:** { ctx.author.mention }')
    await ctx.send(embed=emb)

@Bot.command(aliases=['кик'])
@commands.has_permissions(view_audit_log=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason = reason)
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969] #цвет в формате 0xHEX
    emb = discord.Embed(title=f':octagonal_sign: | Кик Пользователя __{member.name}__',description=f'\n:red_square: **Подробная информация про Кик:**',color = random.choice(colours5))
    emb.set_footer(text=f'| Вызвано Администратором: {ctx.author.name}', icon_url= ctx.author.avatar_url)
    emb.set_thumbnail(url= member.avatar_url)
    emb.add_field(name=':shield:| Имя Нарушителя:',value = member.mention)
    emb.add_field(name=':drum:| Айди Нарушителя:',value = member.id)
    emb.add_field(name=':ring:| Тег Нарушителя:',value = member.discriminator)
    emb.add_field(name=':joystick:| Причина Нарушения:',value = reason)
    emb.add_field(name=':beginner:| Дата регестрации аккаунта:',value = ctx.author.created_at.strftime("%d.%m.%Y %H:%M:%S"))
    emb.add_field(name=':notebook:| Дата присоедениния: ', value = f'{ctx.author.joined_at.strftime("%d.%m.%Y %H:%M:%S")}')
    await member.send( f'{ member.mention }, Вас **выгнали** из сервера **ST Comunity!** **Выгнал:** { ctx.author.mention }')
    await ctx.send(embed=emb)

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def mute(ctx,member:discord.Member,time:int,reason):
    await member.send( f'{ member.mention }, Вы получили **мут** на сервере **ST Comunity!** **Выдал мут:** { ctx.author.mention }')
    await ctx.message.delete()
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969] #цвет в формате 0xHEX
    muterole = discord.utils.get(ctx.guild.roles,id=858397358415675442)
    emb = discord.Embed(title=f':octagonal_sign: | Мут Пользователя __{member.name}__',description=f'\n:red_square: **Подробная информация про мут:**',color = random.choice(colours5))
    emb.set_footer(text=f'| Вызвано Администратором: {ctx.author.name}', icon_url= ctx.author.avatar_url)
    emb.set_thumbnail(url= member.avatar_url)
    emb.add_field(name=':shield:| Имя Нарушителя:',value = member.mention)
    emb.add_field(name=':drum:| Айди Нарушителя:',value = member.id)
    emb.add_field(name=':ring:| Тег Нарушителя:',value = member.discriminator)
    emb.add_field(name=':joystick:| Причина Нарушения:',value = reason)
    emb.add_field(name=':beginner:| Дата регестрации аккаунта:',value = ctx.author.created_at.strftime("%d.%m.%Y %H:%M:%S"))
    emb.add_field(name=':notebook:| Дата присоедениния: ', value = f'{ctx.author.joined_at.strftime("%d.%m.%Y %H:%M:%S")}')
    await member.add_roles(muterole)
    await ctx.send(embed=emb)
    await asyncio.sleep(time * 60)
    await member.remove_roles(muterole)

@Bot.command()
async def unban(ctx,*,member):
    await ctx.message.delete()
    banned_users=await ctx.guild.bans()
    member_name, member_discriminator=member.split('#')
    for ban_entry in banned_users:
        user=ban_entry.user
        if (user.name, user.discriminator)==(member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Разбанен {user}')
            return


@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def unmute(ctx,member:discord.Member,reason):
    await ctx.message.delete()
    channel = Bot.get_channel(858405446510575666)
    muterole = discord.utils.get(ctx.guild.roles,id=858397358415675442)
    emb = discord.Embed(title="Анмут",color=0x2f3136)
    emb.add_field(name='Модератор',value=ctx.message.author.mention,inline=False)
    emb.add_field(name='Не нарушитель',value=member.mention,inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Выдал анмут: {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await channel.send (embed = emb)
    await member.remove_roles(muterole)
    await member.send( f'{ member.mention }, С вас сняли **мут** на сервере **ST Comunity!** **Снял мут:** { ctx.author.mention }')

@Bot.event
async def on_ready():
    print("Бот ахуенно работает бро!")
    await Bot.change_presence(status=discord.Status.idle,activity=Activity(name="за сервером.",type=ActivityType.watching))

@Bot.command()
@commands.has_permissions(view_audit_log=True)
async def clear(ctx,amount=10):
    deleted = await ctx.message.channel.purge(limit=amount)

@Bot.command()
async def info(ctx,member:discord.Member):
    emb = discord.Embed(title='Информация о пользователе',color=0x2f3136)
    emb.add_field(name='Имя',value=member.display_name,inline=False)
    emb.add_field(name="Когда присоединился:",value=member.joined_at.strftime('%d.%m.%Y %H:%M:%S'),inline=False)
    emb.add_field(name='Айди:',value=member.id,inline=False)
    emb.add_field(name='Аккаунт был создан:',value=member.created_at.strftime("%d.%m.%Y %H:%M:%S"),inline=False)
    emb.add_field(name='Самая высокая роль:',value=member.top_role.mention,inline=False)
    emb.set_thumbnail(url=member.avatar_url)
    emb.set_footer(text=f"Вызвано: {ctx.message.author}",icon_url=ctx.message.author.avatar_url)
    emb.set_author(name=ctx.message.author,icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed = emb)

@Bot.command(name="pravda")
async def _8ball(ctx, *, question: str = None):
    if question == None:
        RANDOM = str(1)
    else:
        RANDOM = str(random.randint(2,16))
    answer = {'1' : 'Это правда.',
             '2' : 'Это не правда.',
             '3' : 'Хуй знает',
             '4' : 'Это правда.',
             '5' : 'Это не правда.',
             '6' : 'Хуй знает',
             '7' : 'Это правда.:',
             '8' : 'Это не правда.',
             '9' : 'Хуй знает.',
            '10' : 'Это правда.',
            '11' : 'Это не правда.',
            '12' : 'Хуй знает.',
            '13' : 'Это правда.',
            '14' : 'Это не правда.',
            '15' : 'Хуй знает.',
            '16' : 'Это правда.'}
    await ctx.send(answer[RANDOM])

@Bot.command()
async def say(ctx, *, message):
    colours5 = [0xff0000, 0xff9f00, 0x72ff00, 0x00ff6d, 0x00acff, 0x0200ff, 0xc500ff, 0xff0053, 0xFA8072, 0xFF7F50, 0x00CED1, 0x800080, 0x696969]
    await ctx.message.delete()
    emb = discord.Embed(title='📌  | Cообщение', description=message, color=random.choice(colours5))
    emb.set_author(name=ctx.author.name, icon_url = ctx.author.avatar_url)

    await ctx.send(embed=emb)

@Bot.command(pass_context = True)

async def help(ctx):
    await ctx.message.delete()
    emb = discord.Embed(title=':compass:    |   Навигация по командам.',color=0x2f3136)
    emb.set_footer(text=f'| Вызвано: {ctx.author.name}', icon_url= ctx.author.avatar_url)
    emb.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field( name =':people_wrestling:    | `{}actions`'.format( "#" ), value = '**RolePlay.**')
    emb.add_field( name =':ring:    | `{}ban`'.format( "#" ), value = '**Ограничение доступа к серверу.**')
    emb.add_field( name =':drum:    | `{}unban`'.format( "#" ), value = '**Удаления ограничения к серверу.**')
    emb.add_field( name =':beginner:    | `{}kick`'.format( "#" ), value = '**Выгнать с сервера.**')
    emb.add_field( name =':mountain_snow:    | `{}clear`'.format( "#" ), value = '**Очистить чат.**')
    emb.add_field( name =':notebook:    | `{}mute`'.format( "#" ), value = '**Ограничение к чату сервера.**')
    emb.add_field( name =':smoking:    | `{}unmute`'.format( "#" ), value = '**Удаления ограничения к чату сервера.**')
    emb.add_field( name =':crossed_swords:    | `{}pravda`'.format( "#" ), value = '**Правда либо Не Правда.**')
    emb.add_field( name =':dagger:    | `{}info`'.format( "#" ), value = '**Информация о пользователе.**')
    emb.add_field( name =':knife:    | `{}say`'.format( "#" ), value = '**Сообщение от имени бота.**')
    emb.add_field( name =':musical_note:    | `{}music`'.format( "#" ), value = '**Музыка**')
    await ctx.send(embed=emb)

@Bot.command()
async def gey( ctx ):
    await ctx.message.delete()
    await ctx.author.send(f'{ ctx.author.mention }, Ты гей ебанный, ХАХАХАХХААХХАХА')

@Bot.command()
async def hello( ctx, member: discord.Member ):
    await ctx.message.delete()
    await member.send( f'{ member.mention }, привет от { ctx.author.mention }')

@Bot.command()
@commands.has_permissions(administrator = True)
async def jertva( ctx, member: discord.Member ):
    await member.send( f'{ member.mention }, алё хуесос тебя зовёт очень крутой человек { ctx.author.mention }')
    await ctx.message.delete()

@Bot.command()
@commands.has_permissions(administrator = True)
async def love( ctx, member: discord.Member ):
    await member.send( f'{ member.mention }, Я тебя люблю кисочка моя :heart: от { ctx.author.mention }')
    await ctx.message.delete()

@Bot.command()
async def music(ctx):
    await ctx.message.delete()
    emb = discord.Embed(title=':musical_note:    |   Музыка.',color=0x2f3136)
    emb.set_footer(text=f'| Вызвано: {ctx.author.name}', icon_url= ctx.author.avatar_url)
    emb.set_author(name= ctx.author.name, icon_url = ctx.author.avatar_url)
    emb.add_field( name = ':yellow_square:    | `{}play`'.format( "#" ), value = '**Включить песню.**')
    emb.add_field( name = ':blue_square:    | `{}stop`'.format( "#" ), value = '**Выключить песню..**')
    emb.add_field( name = ':green_square:    | `{}skip`'.format( "#" ), value = '**Скипнуть песню которая играет.**')
    emb.add_field( name = ':purple_square:    | `{}playing`'.format( "#" ), value = '**Посмотреть что сейчас играет.**')
    emb.add_field( name = ':brown_square:    | `{}volume`'.format( "#" ), value = '**Изменить громкость.**')
    emb.add_field( name = ':orange_square:    | `{}summon`'.format( "#" ), value = '**Переместить бота.**')
    emb.add_field( name = ':white_large_square:    | `{}queue`'.format( "#" ), value = '**Очередь.**')
    await ctx.send(embed=emb)

Bot.run("ODU4MzcyMjE4NjI2NTA2NzUy.YNdLbA.Tdwsul4TGpidnRqngotpCp-UOuE")
