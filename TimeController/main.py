import discord
import keep_alive
import os
import asyncio


client = discord.Client()


@client.event
async def on_ready():
    print("listo")

@client.event
async def on_message(message):
    if message.content.find("?set timer") !=-1:
        inicioNombre = message.content.find("(")
        finalNombre = message.content.find(")")
        nombre = message.content[inicioNombre+1:finalNombre]
        print(len(message.content))
        if len(message.content) == 19:
          minutos = int(message.content[len        (message.content)-2:len(message.content)])
        else:
          minutos = int(message.content[len        (message.content)-3:len(message.content)])
        await message.channel.send(f"se ha iniciado el temporizador con una duración de {minutos} minutos, {nombre}")

    if message.content.find("se ha iniciado el temporizador con una duración de") !=-1:
        
        posicionComa = message.content.find(",")
        nombre = message.content[posicionComa+2:len(message.content)]
        autorViejo = []
        mensajes = await message.channel.history(limit=8).flatten()
        for mensaje in mensajes:
            if mensaje.content.find(nombre) != -1 and mensaje.content.find("?set timer") != -1:
                autorViejo.append(mensaje.author)
        horas = ""
        if posicionComa == 62:
            horas = message.content[51:54]
        if posicionComa == 61:
            horas = message.content[51:53]
        if posicionComa == 60:
            horas = message.content[50:52]



        
        horas = int(horas)
        
        while horas >= 0:
            if horas == 0:
                await message.channel.send("¡Se terminó el tiempo!")
                mensajes = await message.channel.history(limit=14).flatten()
                for mensaje in mensajes:
                    if mensaje.content.find(nombre)!=-1 and mensaje.content.find("?set timer")!=-1:

                        await message.channel.send(f"Se terminó el tiempo de tu temporizador: {nombre}, {mensaje.author.mention}!")
                        await message.delete()
                        break
            mensaje = discord.Embed(title=f"Temporizador: {nombre}, de {autorViejo[0].name}", description=f"Tiempo restante: {str(horas)} minutos")
            await message.edit(embed = mensaje)
            horas -= 1
            await asyncio.sleep(60)


Token = os.environ.get("token")
keep_alive.keep_alive()

client.run(Token)