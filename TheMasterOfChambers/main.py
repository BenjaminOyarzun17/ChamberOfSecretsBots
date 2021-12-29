import discord
import json as js
import random
import asyncio
import os
import gspread
import datetime
import keep_alive
import time
import requests  # to sent GET requests
from bs4 import BeautifulSoup  # to parse HTML
from oauth2client.service_account import ServiceAccountCredentials




scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

excel = gspread.authorize(creds)


client = discord.Client()


canalPaco = client.get_channel(724700731252408360)
canalFunao = client.get_channel(736412431819079810)
canalGG = client.get_channel(724350277494374421)

hechizos = ["Sectumsempra", "Petrificus Totalus", "Imperio", "Reducto", "Avada Kedavra", "Expecto Patronum",
                "Expelliarmus", "Lumos", "Wingardium Leviosa", "Crucio","Serpensortia","Reducto"]

channelsSombrero = [client.get_channel(722218667034804364),client.get_channel(737091197151084715)]
patronus = [["Conejo", 'conejo.png'], ["Siervo", "siervo.png"], ["Pegaso", "pegaso.png"],
            ["Águila", "aguila.png"], ["Ardilla", "ardilla.png"], ["Armiño", "armiño.png"],
            ["Lobo", "lobo.png"], ["Búfalo", "bufalo.png"],["Dragón", "dragon.png"],
            ["Gato", "gato.png"], ["Serpiente", "serpiente.png"], ["Pavo Real", "pavo.png"],
            ["Fénix", "fenix.png"], ["Hipogrifo", "hipogrifo.png"],["Thestral", "thestral.png"]]
admins = ["Benha#6633"]

casas = ["Gryffindor", "Ravenclaw", "Slytherin", "Hufflepuff"]

NoXpChannels = ["Chamber_of_Relax", "Relajo 4to", "Relajo 3ro", "Relajo 2do","Relajo 1ro", "Relajo 5to","Relajo 6to", "Relajo 7mo", "Relajo 8vo", "4tos: Sala de Juegos","3ros: Sala de Juegos","2dos: Sala de Juegos","1ros: Sala de Juegos","5tos: Sala de Juegos","6tos: Sala de Juegos","7mos: Sala de Juegos","8vos: Sala de Juegos"]


xpRate = 1

@client.event
async def on_voice_state_update(member,before,after):
    
    canal = after.channel.name
    canalCheck = after.channel.name
    
    if member.voice != None:
        sheet = excel.open("masterofchambers").sheet1
        usuariosEx = sheet.col_values(5)
        if str(member.id) not in usuariosEx:
            await member.send("Veo que entraste a un canal de voz... ¡Para ganar puntos de casa de Hogwarts, debes primero pertenecer a una casa!")
        if str(member.id) in usuariosEx:
            while canalCheck == canal and member.voice.channel.name not in NoXpChannels and member.voice.self_video and not member.voice.self_deaf:
                print(f"deaf: {member.voice.self_deaf}")
                print(f"video:{member.voice.self_video}")
                
                n=0
                cell = sheet.find(str(member.id))
                info_usuario = cell.row
                xpUsuario = sheet.cell(info_usuario, 4).value
                if xpUsuario == "":
                    xpUsuario = 0
                print(str(xpUsuario))
                xpUsuario = float(xpUsuario) + 1
                sheet.update_cell(info_usuario, 4, str(xpUsuario))
                print(f"se sumo xp en {canal}")
                while n < 61:
                  canalCheck = after.channel.name
                  if canalCheck != canal:
                    print("se salio")
                    break
                  await asyncio.sleep(1)
                  n+=1
            while canalCheck == canal and member.voice.channel.name not in NoXpChannels and not member.voice.self_video and not member.voice.self_deaf:
                print(f"deaf: {member.voice.self_deaf}")
                print(f"video:{member.voice.self_video}")
                n=0
                cell = sheet.find(str(member.id))
                info_usuario = cell.row
                xpUsuario = sheet.cell(info_usuario, 4).value
                if xpUsuario == "":
                    xpUsuario = 0
                print(str(xpUsuario))
                xpUsuario = float(xpUsuario) + 0.75
                sheet.update_cell(info_usuario, 4, str(xpUsuario))
                print(f"se sumo xp en {canal}")
                while n < 61:
                  canalCheck = after.channel.name
                  if canalCheck != canal:
                    print("se salio")
                    break
                  await asyncio.sleep(1)
                  n+=1   
            while canalCheck == canal and member.voice.channel.name not in NoXpChannels and member.voice.self_video and  member.voice.self_deaf:
                print(f"deaf: {member.voice.self_deaf}")
                print(f"video:{member.voice.self_video}")
                n=0
                cell = sheet.find(str(member.id))
                info_usuario = cell.row
                xpUsuario = sheet.cell(info_usuario, 4).value
                if xpUsuario == "":
                    xpUsuario = 0
                print(str(xpUsuario))
                xpUsuario = float(xpUsuario) + 0.75
                sheet.update_cell(info_usuario, 4, str(xpUsuario))
                print(f"se sumo xp en {canal}")
                while n < 61:
                  canalCheck = after.channel.name
                  if canalCheck != canal:
                    print("se salio")
                    break
                  await asyncio.sleep(1)
                  n+=1        
            while canalCheck == canal and member.voice.channel.name not in NoXpChannels and not member.voice.self_video and  member.voice.self_deaf:
                print(f"deaf: {member.voice.self_deaf}")
                print(f"video:{member.voice.self_video}")
                n=0
                cell = sheet.find(str(member.id))
                info_usuario = cell.row
                xpUsuario = sheet.cell(info_usuario, 4).value
                if xpUsuario == "":
                    xpUsuario = 0
                print(str(xpUsuario))
                xpUsuario = float(xpUsuario) + 0.5
                sheet.update_cell(info_usuario, 4, str(xpUsuario))
                print(f"se sumo xp en {canal}")
                while n < 61:
                  canalCheck = after.channel.name
                  if canalCheck != canal:
                    print("se salio")
                    break
                  await asyncio.sleep(1)
                  n+=1        
            if member.voice.channel.name != canal:
              print("se cambió")
            
            
            if member.voice.channel.name != canal:
              print("se cambió")
              
    if member.voice == None:
        print("se desconecto")

@client.event
async def on_member_remove(member):
    canalLeft = client.get_channel(740585438254727319)
    await canalLeft.send(member.name +" abandonó el server")


@client.event
async def on_member_join(member):
    await member.send("¡Bienvenido a la Chamber Of Secrets. Para iniciarte deberías:\n-leer las reglas\n-verificar tu identidad con tu mail dsmorus en el canal 'verificador'.\n-escribir el comando de tu curso en el canal 'asignador de cursos'. En las reglas están las instrucciones para unirte a un curso. \n ¡Yo soy un Bot, por lo que no responderé tus mensajes!")
    await member.send("PD: si es que eres profesor, un administrador debe asignarte ese rol. Por ello habla con César (profesor), Benjamín Oyazún (3ro Medio), José González (4to Medio) o Sebastián Vásquez (4to Medio).")

@client.event
async def on_ready():
    print("ya estoy on line")



def takeThird(elem):
    return elem[2]


@client.event
async def on_message(message):
    ChamberOSlist = client.guilds
    ChamberOS = ChamberOSlist[0]
    COSRoles = ChamberOS.roles
    miembrosCos = ChamberOS.members
    miembroAutorLst = []
    if message.content == "*mis puntos":
        sheet = excel.open("masterofchambers").sheet1
        todos = sheet.get_all_records()
        UserPts = []
        for usuario in todos:
            if usuario["id"] == message.author.id:
                datosInsert = [usuario['Week_Points']]
                UserPts.append(datosInsert)
        await message.channel.send(f"Hasta ahora has hecho {str(UserPts[0][0])} puntos. Sigue así, {message.author.mention}")


    if message.content == "dame mi id":
        await message.channel.send(message.author.id)

     
    
    purge = "*purge"


    
    if message.content.find("*Accio")!=-1:
      if message.content.find("*Accio *Accio")!=-1:
        await message.channel.send("la recursion es mala, cortala, o llamo al sindicato de bots.")
      else: 
        SAVE_FOLDER = 'images'
        if not os.path.exists(SAVE_FOLDER):
            os.mkdir(SAVE_FOLDER)
        mensaje = message.content[7:len(message.content)]
        def download_images(mensaje):
            
            GOOGLE_IMAGE = \
                'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'
            usr_agent = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
            }
            n_images = 1
            print('Start searching.....')
            searchurl = GOOGLE_IMAGE + 'q=' + mensaje
            response = requests.get(searchurl, headers=usr_agent)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})
            count = 0
            links = []
            for res in results:
                try:
                    link = res['data-src']
                    links.append(link)
                    count += 1
                    if (count >= n_images): break
                except KeyError:
                    continue
            print(f'Downloading {len(links)} images....')
            for i, link in enumerate(links):
                response = requests.get(link)
                image_name = SAVE_FOLDER + '/descarga.jpg'
                with open(image_name, 'wb') as fh:
                    fh.write(response.content)
                    

        download_images(mensaje)
        await message.channel.send(f"¡Usaste {message.content[1:len(message.content)]}!")
        await message.channel.send(file=discord.File(SAVE_FOLDER + '/descarga.jpg'))
        await asyncio.sleep(5)
        os.remove(SAVE_FOLDER + '/descarga.jpg')



    if message.content == "*rank casas":
      canalResult = client.get_channel(744690650234093569)
      sheet = excel.open("masterofchambers").sheet1
      puntosGryffindor = 0
      puntosHufflepuff = 0
      puntosSlytherin = 0
      puntosRavenclaw = 0
      todos = sheet.get_all_records()
      puntosCasa = []
      for usuario in todos:
          if usuario["Casa"] == "Gryffindor":
              puntos = usuario['Week_Points']
              if puntos == "":
                  puntos = 0
              puntosGryffindor += puntos

          if usuario["Casa"] == "Hufflepuff":
              puntos = usuario['Week_Points']
              if puntos == "":
                  puntos = 0
              puntosHufflepuff += puntos
          if usuario["Casa"] == "Slytherin":
              puntos = usuario['Week_Points']
              if puntos == "":
                  puntos = 0
              puntosSlytherin += puntos

          if usuario["Casa"] == "Ravenclaw":
              puntos = usuario['Week_Points']
              if puntos == "":
                  puntos = 0
              puntosRavenclaw += puntos
      emoGry = client.get_emoji(
          745296119281614949)  # https://cdn.discordapp.com/emojis/745296119281614949.png?v=1
      emoHuf = client.get_emoji(
          745297278389977210)  # https://cdn.discordapp.com/emojis/745297278389977210.png?v=1
      emoSly = client.get_emoji(
          745294394785267842)  # https://cdn.discordapp.com/emojis/745294394785267842.png?v=1
      emoRav = client.get_emoji(
          745296827166752792)  # https://cdn.discordapp.com/emojis/745296827166752792.png?v=1

      puntosCasa.append(["Ravenclaw", puntosRavenclaw, emoRav])
      puntosCasa.append(["Slytherin", puntosSlytherin, emoSly])
      puntosCasa.append(["Hufflepuff", puntosHufflepuff, emoHuf])
      puntosCasa.append(["Gryffindor", puntosGryffindor, emoGry])

      puntosCasa.sort(key=takeSecond, reverse=True)

      embed = discord.Embed(title="Puntos por casa", description="El torneo inicia el 16 de cada mes")
      embed.add_field(name=f"1º {puntosCasa[0][2]} {puntosCasa[0][0]} {puntosCasa[0][2]}",
                      value=str(puntosCasa[0][1]) + " puntos", inline=False)
      embed.add_field(name=f"2º {puntosCasa[1][2]} {puntosCasa[1][0]} {puntosCasa[1][2]}",
                      value=str(puntosCasa[1][1]) + " puntos", inline=False)
      embed.add_field(name=f"3º {puntosCasa[2][2]} {puntosCasa[2][0]} {puntosCasa[2][2]}",
                      value=str(puntosCasa[2][1]) + " puntos", inline=False)
      embed.add_field(name=f"4º {puntosCasa[3][2]} {puntosCasa[3][0]} {puntosCasa[3][2]}",
                      value=str(puntosCasa[3][1]) + " puntos", inline=False)
      await message.channel.send(content=None, embed=embed)



    if message.content == "*rank Ravenclaw":
        sheet = excel.open("masterofchambers").sheet1
        todos = sheet.get_all_records()
        print(todos)
        UserPts = []
        for usuario in todos:
            if usuario["Casa"] == "Ravenclaw":
                datosInsert = [usuario["Usuario"], usuario["id"], usuario['Week_Points']]
                UserPts.append(datosInsert)
        print(UserPts)
        UserPts.sort(key = takeThird, reverse=True)
        print(UserPts)
        print(miembrosCos)

        for usuario in UserPts:
            for miembro in miembrosCos:
                if miembro.id == int(usuario[1]):
                    usuario[0] = miembro.name

        emoRav = client.get_emoji(745296827166752792)  # https://cdn.discordapp.com/emojis/745296827166752792.png?v=1
        embed = discord.Embed(title=f"{emoRav} Ranking Ravenclaw {emoRav}",description="El torneo mensual de casas terminará el 16 de cada mes")
        embed.add_field(name=f"1º {UserPts[0][0]}", value=str(UserPts[0][2]) + " puntos", inline=False)
        embed.add_field(name=f"2º {UserPts[1][0]}", value=str(UserPts[1][2]) + " puntos", inline=False)
        embed.add_field(name=f"3º {UserPts[2][0]}", value=str(UserPts[2][2]) + " puntos", inline=False)
        embed.add_field(name=f"4º {UserPts[3][0]}", value=str(UserPts[3][2]) + " puntos", inline=False)
        embed.add_field(name=f"5º {UserPts[4][0]}", value=str(UserPts[4][2]) + " puntos", inline=False)
        await message.channel.send(content=None, embed=embed)
    if message.content == "*rank Hufflepuff":
        sheet = excel.open("masterofchambers").sheet1
        todos = sheet.get_all_records()
        print(todos)
        UserPts = []
        for usuario in todos:
            if usuario["Casa"] == "Hufflepuff":
                datosInsert = [usuario["Usuario"], usuario["id"], usuario['Week_Points']]
                UserPts.append(datosInsert)
        print(UserPts)
        UserPts.sort(key=takeThird, reverse=True)
        print(UserPts)
        print(miembrosCos)

        for usuario in UserPts:
            for miembro in miembrosCos:
                if miembro.id == int(usuario[1]):
                    usuario[0] = miembro.name

        emoHuf = client.get_emoji(745297278389977210)  # https://cdn.discordapp.com/emojis/745297278389977210.png?v=1

        embed = discord.Embed(title=f"{emoHuf} Ranking Hufflepuff {emoHuf}",
                              description="El torneo mensual de casas terminará el 16 de cada mes")
        embed.add_field(name=f"1º {UserPts[0][0]}", value=str(UserPts[0][2]) + " puntos", inline=False)
        embed.add_field(name=f"2º {UserPts[1][0]}", value=str(UserPts[1][2]) + " puntos", inline=False)
        embed.add_field(name=f"3º {UserPts[2][0]}", value=str(UserPts[2][2]) + " puntos", inline=False)
        embed.add_field(name=f"4º {UserPts[3][0]}", value=str(UserPts[3][2]) + " puntos", inline=False)
        embed.add_field(name=f"5º {UserPts[4][0]}", value=str(UserPts[4][2]) + " puntos", inline=False)
        await message.channel.send(content=None, embed=embed)
    if message.content == "*rank Gryffindor":
        sheet = excel.open("masterofchambers").sheet1
        todos = sheet.get_all_records()
        print(todos)
        UserPts = []
        for usuario in todos:
            if usuario["Casa"] == "Gryffindor":
                datosInsert = [usuario["Usuario"], usuario["id"], usuario['Week_Points']]
                UserPts.append(datosInsert)
        print(UserPts)
        UserPts.sort(key=takeThird, reverse=True)
        print(UserPts)
        print(miembrosCos)

        for usuario in UserPts:
            for miembro in miembrosCos:
                if miembro.id == int(usuario[1]):
                    usuario[0] = miembro.name

        emoGry = client.get_emoji(745296119281614949)  # https://cdn.discordapp.com/emojis/745296119281614949.png?v=1

        embed = discord.Embed(title=f"{emoGry} Ranking Gryffindor {emoGry}",
                              description="El torneo mensual de casas terminará el 16 de cada mes")
        embed.add_field(name=f"1º {UserPts[0][0]}", value=str(UserPts[0][2]) + " puntos", inline=False)
        embed.add_field(name=f"2º {UserPts[1][0]}", value=str(UserPts[1][2]) + " puntos", inline=False)
        embed.add_field(name=f"3º {UserPts[2][0]}", value=str(UserPts[2][2]) + " puntos", inline=False)
        embed.add_field(name=f"4º {UserPts[3][0]}", value=str(UserPts[3][2]) + " puntos", inline=False)
        embed.add_field(name=f"5º {UserPts[4][0]}", value=str(UserPts[4][2]) + " puntos", inline=False)
        await message.channel.send(content=None, embed=embed)
    if message.content == "*rank Slytherin":
        sheet = excel.open("masterofchambers").sheet1
        todos = sheet.get_all_records()
        print(todos)
        UserPts = []
        for usuario in todos:
            if usuario["Casa"] == "Slytherin":
                datosInsert = [usuario["Usuario"], usuario["id"], usuario['Week_Points']]
                UserPts.append(datosInsert)
        print(UserPts)
        UserPts.sort(key=takeThird, reverse=True)
        print(UserPts)
        print(miembrosCos)

        for usuario in UserPts:
            for miembro in miembrosCos:
                if miembro.id == int(usuario[1]):
                    usuario[0] = miembro.name


        emoSly = client.get_emoji(745294394785267842)  # https://cdn.discordapp.com/emojis/745294394785267842.png?v=1

        embed = discord.Embed(title=f"{emoSly} Ranking Slytherin {emoSly}",
                              description="El torneo mensual de casas terminará el 16 de cada mes")
        embed.add_field(name=f"1º {UserPts[0][0]}", value=str(UserPts[0][2]) + " puntos", inline=False)
        embed.add_field(name=f"2º {UserPts[1][0]}", value=str(UserPts[1][2]) + " puntos", inline=False)
        embed.add_field(name=f"3º {UserPts[2][0]}", value=str(UserPts[2][2]) + " puntos", inline=False)
        embed.add_field(name=f"4º {UserPts[3][0]}", value=str(UserPts[3][2]) + " puntos", inline=False)
        embed.add_field(name=f"5º {UserPts[4][0]}", value=str(UserPts[4][2]) + " puntos", inline=False)
        await message.channel.send(content=None, embed=embed)

    print(f"estos son: {message.author.roles}")
    if message.channel == client.get_channel(724350277494374421):
        if message.author.id == 534589798267224065:
            await message.channel.send("GG!")

    if message.channel == client.get_channel(736970596818354226):
        rolesMiembro = message.author.roles
        if message.content == "*primeroMedio":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["4toMedio","2doMedio", "3roMedio", "5toBásico", "8voBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")

            if permiso == True:
                for rol in COSRoles:
                    if rol.name == "1roMedio":
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*segundoMedio":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","4toMedio", "3roMedio", "5toBásico", "8voBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.name == "2doMedio":
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*terceroMedio":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "4toMedio", "5toBásico", "8voBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.name == "3roMedio":
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*cuartoMedio":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "3roMedio", "5toBásico", "8voBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.name == "4toMedio":
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*quintoBasico":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "3roMedio", "4toMedio", "8voBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.id == 736702963283656715:
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*sextoBasico":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "3roMedio", "4toMedio", "8voBásico", "7moBásico","5toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.id== 736702964730691637:
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*septimoBasico":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "3roMedio", "4toMedio", "8voBásico", "5toBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.id == 736702955264409620:
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

        if message.content == "*octavoBasico":
            permiso = True
            for role in rolesMiembro:
                if role.name in ["1roMedio","2doMedio", "3roMedio", "4toMedio", "5toBásico", "7moBásico","6toBásico"]:
                    permiso = False
                    await message.channel.send("¡ya tienes un rol! Casi pasas por listo...")
            if permiso == True:
                for rol in COSRoles:
                    if rol.id == 736702935026892930:
                        await message.author.add_roles(rol)
                        await message.channel.send("¡se te asignó el rol!")
                    if rol.id == 739154345639018556:
                        await message.author.remove_roles(rol)

    if message.content.find("*purge") != -1:
        run = False
        
        rolesMiembro = message.author.roles
        for rol in rolesMiembro:
            if rol.id == 720825275654602813:
                run = True
        if run == True:
            print("lo vi")
            for role in rolesMiembro:
                if role.name == 'Admin_ big':
                    print("vi el rol")
                    try:
                        limite = int(message.content[7] + message.content[8])
                    except IndexError:
                        limite = int(message.content[7])
                    await message.channel.purge(limit=limite)
                    await message.channel.send("Se eliminaron " + str(limite) + " mensajes")



    if message.content == "*roles":
        print(COSRoles)



    if message.content == "*(backend)show channels":
        COS = message.author.guild  # cos = chamber of secrets
        print("COS")
        print(COS)
        text_channel_list = []
        voice_channel_list = []
        for guild in client.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        for guild in client.guilds:
            for channel in guild.voice_channels:
                voice_channel_list .append(channel)
        print("texto")
        print(text_channel_list)
        print("voz")
        print(voice_channel_list )
        channel = client.get_channel(722218667034804364)
        await channel.send('(función de desarrollador, nada que ver aquí)')


    if message.content == "*Lumos":
        await message.channel.send("¡Usaste Lumos!")
        await message.channel.send(file=discord.File("lumos.png"))
    if message.content == "*help":
        await message.channel.send("¿Quieres ayuda? JAJAJA. ¡Tu capricho te costará XP!")
        await asyncio.sleep(10)
        await message.channel.send("¡Sike!")
        embed = discord.Embed(title="Ayuda de comandos", description="bla bla bla")
        embed.add_field(name="*(hechizo)", value="utilizas un hechizo. ¿Cuáles?. No lo se... ¿Te sabes alguno?")
        embed.add_field(name="*iniciar test de casas", value="el sombrero te asignará una casa. Solo funciona una vez.")
        embed.add_field(name="*rank casas", value="Permite ver el ranking de casas ¿Quién ganará?")
        embed.add_field(name="*rank (Casa)", value="Muestra el rank interno de cada casa.")
        embed.add_field(name="*mis puntos", value="Muestra los puntos que hechos en la temporada. ")
        embed.add_field(name="-play (canción)", value="Groovy toca una canción.")
        embed.add_field(name="!play (canción)", value="MEE6 toca una canción.")
        embed.add_field(name="-p (canción)", value="Groovy toca una canción.")
        embed.add_field(name="R!play (canción)", value="Rythm toca una canción.")
        embed.add_field(name=".play (canción)", value="Hydra toca una canción.")
        embed.add_field(name="ar!top", value="Muestra el ranking del server. ¿Aún eres Ameba?")
        embed.add_field(name="ar!m stats", value="Muestra tus estadísticas.")

        await message.channel.send(content=None, embed=embed)

    if message.channel ==canalGG:
        if message.content.find("Felicidades")!=-1:
            await message.channel.send("GG!")


    for hechizo in hechizos:
        if message.content == "*" + hechizo:
            await message.channel.send("usaste " + hechizo)
    if message.content == "*Reducto":
        await message.channel.send("Usaste reducto.")
        await message.channel.send(file=discord.File("reducto.gif"))
    if message.content == "*Crucio":
        await message.channel.send("Usaste crucio.")
        await message.channel.send(file=discord.File("crucio.gif"))
    if message.content == "*Morsmordre":
        await message.channel.send("Así que... eres un seguidor... Nunca esperé eso de ti..." + message.author.mention)
        await message.channel.send(file=discord.File("morsmodre.gif"))
    if message.content == "*quiero ser seguidor":
        await message.channel.send("¿Seguro que quieres seguir al que no se debe nombrar?")
    if message.content == "*Avada Kedavra":
        kedabras = ["Eres una persona muy mala, y un gatito murió en alguna parte por tu culpa",
                    "De todos los hechizos que conoces, usaste este... No abuses de tu poder, puede que... ¿te coste XP?",
                    "Tu crueldad es insuperable",
                    "Acabas de superar al doctor malito"]
        kedabra = random.choice(kedabras)

        await message.channel.send(kedabra)
    if message.content == "*Expecto Patronum":
        usuarios = []
        objetosJson = []
        usuarios.clear()
        objetosJson.clear()
        with open("statsUsuarios.txt", "r+") as file:
            for line in file:
                linea = js.loads(line)
                objetosJson.append(linea)
            for user in objetosJson:
                usuarios.append(user["usuario"])

        pick = random.choice(patronus)
        sheet = excel.open("masterofchambers").sheet1
        usuariosEx = sheet.col_values(1)

        usuario = str(message.author)
        ubicacionJson = 0
        if str(message.author) in usuariosEx:
            cell = sheet.find(str(message.author))
            fila = cell.row
            patronusUser = sheet.cell(fila, 3).value
            if str(patronusUser) != "":
                await message.channel.send("Usaste tu " + str(patronusUser))
                for par in patronus:
                    if par[0] == patronusUser:
                        imagenPatronus = par[1]
                await message.channel.send(file=discord.File(imagenPatronus))
            if str(patronusUser) == "":
                await message.channel.send(
                    "¡Acabas de descubrir a tu Patronum!...Tu Patronum es...¡ " + pick[0] + "!. Usaste tu " + pick[0])
                await asyncio.sleep(2)
                await message.channel.send(file=discord.File(pick[1]))
                newPatronus = pick[0]
                sheet.update_cell(fila, 3, newPatronus)
        if str(message.author) not in usuariosEx:
            await message.channel.send(
                "Antes de conocer tu Patronus debes estar en una casa. Usa el comando (*iniciar test de casas) para entrar en una")

    if message.content == "*Wingardium Leviosa":
        await message.channel.send("se dice leviosaaa")



    if message.channel == client.get_channel(722218667034804364) or message.channel == client.get_channel(737091197151084715):
        if message.content == "*iniciar test de casas":
            sheet = excel.open("masterofchambers").sheet1
            usuariosEx = sheet.col_values(1)
            if str(message.author) in usuariosEx:
                await message.channel.send(
                    "Lo sentimos, ya tienes una casa. Pero si quieres obtener acceso a las demás casas, ten esperanza.")

            if str(message.author) not in usuariosEx:
                casa = random.choice(casas)
                if casa == "Gryffindor":
                     for rol in COSRoles:
                         if rol.id == 737051589432311860:
                            await message.author.add_roles(rol)
                     await message.channel.send(
                        "Acaba de iniciar la ceremonia. El sombrero está decidiendo... ¡Parece que ha hecho una decisión!... Ahora perteneces a... " + "¡**" + casa + "**! claramente eres una persona con coraje y caballerosa. Es demasiado claro, nunca te rindes y tu osadía es incomparable.")


                if casa == "Slytherin":
                     for rol in COSRoles:
                         if rol.id == 737052072356085795:
                            await message.author.add_roles(rol)
                     await message.channel.send(
                        "Acaba de iniciar la ceremonia. El sombrero está decidiendo... ¡Parece que ha hecho una decisión!... Ahora perteneces a... " + "¡**" + casa + "**!. Eres una autoridad innata, tu astucia es incomparable y tu ambición permitirá que logres cosas... ¡increíbles!")
                if casa == "Ravenclaw":
                     for rol in COSRoles:
                         if rol.id == 737051768822956103:
                            await message.author.add_roles(rol)
                     await message.channel.send(
                        "Acaba de iniciar la ceremonia. El sombrero está decidiendo... ¡Parece que ha hecho una decisión!... Ahora perteneces a... " + "¡**" + casa + "**!. Tu claro ingenio, sabiduría e intelecto te llevarán a lugares que no puedes imaginar...")

                if casa == "Hufflepuff":
                     for rol in COSRoles:
                         if rol.id == 737051849726885978:
                            await message.author.add_roles(rol)
                     await message.channel.send(
                        "Acaba de iniciar la ceremonia. El sombrero está decidiendo... ¡Parece que ha hecho una decisión!... Ahora perteneces a... " + "¡**" + casa + "**! sin duda alguna trabajas duro, tienes paciencia, eres fiel a tus amistades y tu sinceridad es tu mayor cualidad")
                insertRow = [str(message.author), casa, "", 0, str(message.author.id)]
                sheet.append_row(insertRow)

def takeSecond(elem):
    return elem[1]






"""
async def mostrarHora():
    
    
    await asyncio.sleep(5)
    COSl = []
    for guild in client.guilds:
        COSl.append(guild)
    COS = COSl[0]
    #otra opcion para obtener la COS: client.get_guild(720821875587940392)
    while True:
        now = datetime.datetime.now()
        global hora
        hora = now.strftime("%H")
        print(hora)
        eventos = ["troll"]#["troll", "quidditch", "campeones de casas"]
        if hora == "21": #18
            print("inició un evento")
            evento = random.choice(eventos)

            if evento == "troll":
                xpRate = 2
                print("el nuevo xprate es"+str(xpRate))
                botspam = [client.get_channel(722218667034804364)]
                Casas = [client.get_channel(745636717666500737),client.get_channel(745643772934881421),
                         client.get_channel(745641760864075838),client.get_channel(745639689322627234)]
                for casa in Casas: #recordar cambiar esto a Casas
                    await casa.send("¡Acaba de aparecer un troll! ¡Usen sus varitas en conjunto para espantarlo! ¡Ganarán 2 puntos por minuto por 1 hora! ¡Aprovechen!")
                
                await asyncio.sleep(3600)
                xpRate = 1
                for casa in botspam: #recordar cambiar esto a Casas
                    await casa.send("¡El troll se ha ido! La ganancia de puntos ha vuelto a la normalidad...")
                print("Ha llegado un troll")
            if evento == "quidditch":
                print("Ha iniciado el torneo de quidditch")

            if evento == "campeones de casas":
                print("Ha iniciado el torneo de campeones")
                sheet = excel.open("masterofchambers").sheet1
                todos = sheet.get_all_records()
                MiembrosGryffindor = []
                MiembrosSlytherin = []
                MiembrosRavenclaw = []
                MiembrosHufflepuff = []
                for usuario in todos:
                    if usuario["Casa"] == "Gryffindor":
                        MiembrosGryffindor.append([usuario["Usuario"], usuario["id"],usuario["Week_Points"]])
                    if usuario["Casa"] == "Hufflepuff":
                        MiembrosHufflepuff.append([usuario["Usuario"], usuario["id"],usuario["Week_Points"]])
                    if usuario["Casa"] == "Ravenclaw":
                        MiembrosRavenclaw.append([usuario["Usuario"], usuario["id"],usuario["Week_Points"]])
                    if usuario["Casa"] == "Slytherin":
                        MiembrosSlytherin.append([usuario["Usuario"], usuario["id"],usuario["Week_Points"]])


                print(MiembrosRavenclaw)
                print(MiembrosGryffindor)
                print(MiembrosSlytherin)
                elegidosGryffindor = sorted(MiembrosGryffindor, key=lambda x:x[2])# MiembrosGryffindor.sort(key=lambda x:(x[2], -x[0]), reverse=True)
                print(elegidosGryffindor)
                elegidoGryffindor = elegidosGryffindor[-1]
                elegidosRavenclaw = sorted(MiembrosRavenclaw, key=lambda x:x[2])# MiembrosRavenclaw.sort(key=lambda x:(x[2], -x[0]), reverse=True)
                elegidoRavenclaw = elegidosRavenclaw[-1]
                elegidosHufflepuff = sorted(MiembrosHufflepuff, key=lambda x:x[2])#MiembrosHufflepuff.sort(key=lambda x:(x[2], -x[0]), reverse=True)
                elegidoHufflepuff = elegidosHufflepuff[-1]
                elegidosSlytherin = sorted(MiembrosSlytherin, key=lambda x:x[2])# MiembrosSlytherin.sort(key=lambda x:(x[2], -x[0]), reverse=True)
                elegidoSlytherin = elegidosSlytherin[-1]
                botspam = client.get_channel(722218667034804364)

                anuncios = client.get_channel(720828333138378765)
                chat_gryffindor = client.get_channel(745636717666500737)
                chat_slytherin = client.get_channel(745643772934881421)
                chat_ravenclaw = client.get_channel(745641760864075838)
                chat_hufflepuff = client.get_channel(745639689322627234)
                embed = discord.Embed(title="Representantes de cada casa")
                embed.add_field(name=f"Gryffindor", value=str(elegidoGryffindor[0]), inline=False)
                embed.add_field(name=f"Ravenclaw", value=str(elegidoRavenclaw[0]), inline=False)
                embed.add_field(name=f"Hufflepuff", value=str(elegidoHufflepuff[0]), inline=False)
                embed.add_field(name=f"Slytherin", value=str(elegidoSlytherin[0]), inline=False)

                await botspam.send(content=None, embed=embed)
                await botspam.send(f"El elegido de Gryffindor es {elegidoGryffindor[0]}")
                await botspam.send(f"Los representantes de cada casa son")
        time.sleep(3600)  # cada 20 minutos

client.loop.create_task(mostrarHora())
"""



Token = os.environ.get("token")
keep_alive.keep_alive()
client.run(Token)