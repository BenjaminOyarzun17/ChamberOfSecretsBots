import discord
import asyncio
import keep_alive
import os
import random
import time
import datetime


client = discord.Client()

@client.event
async def on_ready():
  print("listo")


tipps = ["En las salas que dice relajo no se pueden ganar puntos ni xp. ","Si encuentras un easteregg nuevo puedes ganar xp y puntos extra para tu casa.","Esto puede sonar raro, pero tenemos tres sistemas de rankings. El primero es el de nivel personal, que mide tu participación en general (mensajes, horas conectado en channels de voz, etc...). Puedes ver tu experiencia en #chat-top. \nEl segundo mide tu actividad en canales de voz mensualmente, en donde los puntos que ganas se juntan con los de tu casa de Hogwarts para el torneo de casas. Esto lo puedes ver en #torneo-de- casas. \nFinalmente está el ranking de casas medido en conocimientos, que muestra el top de casas ganadoras por temporada. Esto lo puedes ver en #resultados-torneos.","Las salas de clase y de casa son para trabajar con personas de otros cursos. ","¿Te gusta lofi? Aprovecha Chamber of Lofi para estudiar escuchando esta playlist junto a otros.","La lista de los comandos se obtiene con *help","Se puede seleccionar casa en #el-sombrero.","¿Tienes dudas de materia? ¡Pregunta en #Ayuda mutua!","¿Te gustó una serie que viste recientemente? ¡Compártela en #cultura!", "¿Sientes que procrastinas mucho?¿Has probado estudiar en conjunto con la cámara prendida? ¿Te tinca usar temporizadores? (#timers)", "Lo sé, las notificaciones son molestas... ¡Puedes desactivarlas haciendo click derecho sobre el canal que quieres que no te envíe notificaciones!", "¿Quieres ver videos para entender el servidor? Aquí hay dos: https://youtu.be/9IblvXC1KFQ ; https://youtu.be/VK9456HHoAI", "¿Cómo gano puntos? Conéctate a cualquier canal de voz, y ganarás un punto por minuto conectado (los de relajo no cuentan!) :D","¿No tienes acceso a la sala de tu casa de Hogwarts? Probablemente porque aún no tienes el nivel requerido...","Las salas VIP de curso son para trabajar con un poco más de privacidad.", "Cuando llegues a lvl 20 tendrás la posibilidad de pedir un deseo... ¿Qué te gustaría pedir?"]


async def timer():
  await asyncio.sleep(5)
  print("init")
  while True:
    ahora = datetime.datetime.now()
    hora = ahora.strftime("%H")
    print(hora)
    if  hora == "16":
      canalTipp = client.get_channel(732069480955641977)#720828333138378765
      await canalTipp.send("Tipp del día: " + random.choice(tipps))
    await asyncio.sleep(3600)
def most_frequent(List): 
    counter = 0
    num = List[0] 
      
    for i in List: 
        curr_frequency = List.count(i) 
        if(curr_frequency> counter): 
            counter = curr_frequency 
            num = i 
  
    return num       

    
@client.event
async def on_message(message):
  if message.content == "*Tipps":
    await message.channel.send(random.choice(tipps))

  if message.content == "*UsuarioDelTiempo":
    print("iniciado")
    canalTimer = client.get_channel(771906602361946112)     
    counter = 0

    listaUsuarios = []
    listaUsuariosBiDim = []
    mensajes = await canalTimer.history(limit=10000).flatten()
    for message in mensajes:
        if message.author.name not in listaUsuarios and message.author.name != "Chad":
            listaUsuarios.append(message.author.name)
    
    for usuario in listaUsuarios:
      listaUsuariosBiDim.append([usuario,1])
    for msj in mensajes: 
      for persona in listaUsuariosBiDim:
        if msj.author.name == persona[0]:
          persona[1]+=1
    
    print(listaUsuariosBiDim)
    print(len(listaUsuarios))
    print(most_frequent(listaUsuarios))
    await message.channel.send(str(listaUsuariosBiDim))
Token = os.environ.get("token")
keep_alive.keep_alive()


client.loop.create_task(timer())
client.run(Token)
