import discord
import random
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)


eco_tips = [
    "Usa menos plástico: lleva tu propia bolsa reutilizable cuando hagas compras.",
    "Apaga las luces cuando no las necesites para ahorrar energía.",
    "Recicla tus baterías en centros de reciclaje especializados.",
    "Usa transporte público o comparte coche para reducir la huella de carbono.",
    "Compra productos locales y orgánicos para apoyar a los agricultores y reducir el impacto ambiental.",
    "Desenchufa los aparatos electrónicos que no estés utilizando para ahorrar energía.",
    "Recicla papel, vidrio y plástico correctamente en los puntos de reciclaje de tu área.",
    "Reduce, reutiliza y recicla: tres claves para un mundo más verde.",
    "Usa bombillas LED de bajo consumo para ahorrar energía y dinero.",
    "Compra ropa de segunda mano o intercambia ropa con amigos en lugar de comprar nueva."
]


decomposition_times = {
    "botella de plástico": "450 años",
    "papel": "2 a 5 meses",
    "vidrio": "1 millón de años",
    "lata de aluminio": "200 a 500 años",
    "pañal desechable": "500 años",
    "colilla de cigarro": "1 a 10 años",
    "bolsa de plástico": "150 años",
    "cartón": "2 meses",
    "manzana": "2 meses",
    "cáscara de plátano": "3 a 4 semanas"
}


@bot.event
async def on_ready():
    print(f'Bot {bot.user} ha iniciado sesión.')


@bot.command()
async def biohelp(ctx):
    eco_tip = random.choice(eco_tips)  
    await ctx.send(f"🌱 Consejo ecológico: {eco_tip}")


@bot.command()
async def descomposicion(ctx, *, objeto: str):
    objeto = objeto.lower()  
    if objeto in decomposition_times:
        tiempo = decomposition_times[objeto]
        await ctx.send(f"🕒 El tiempo de descomposición de **{objeto}** es aproximadamente: {tiempo}.")
    else:
        await ctx.send(f"❌ Lo siento, no tengo información sobre el tiempo de descomposición de **{objeto}**.")


bot.run("YOUR-TOKEN-HERE")
