import discord
from discord.ext import commands
from bot import main.py

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def on_Kirlilik(ctx):
    await ctx.send("Eski eşyalari çöpe atmak yerine geri dönüştürün") 

@bot.command()
async def on_Araba(ctx):
    await ctx.send("Bazen Araba yerine Bisiklet sürebilirsiniz")
    
@bot.command()
async def on_Su(ctx):
    await ctx.send("Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın")     

@bot.command()
async def on_Yemek(ctx):
    await ctx.send("Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.")
    
@bot.command()
async def on_Cihazlar(ctx):
     await ctx.send("Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın.")       


bot.run(token)