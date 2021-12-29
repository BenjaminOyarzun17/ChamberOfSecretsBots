import keep_alive
import discord
import os
import datetime
import asyncio
import random
import smtplib
from email.message import EmailMessage
import imaplib
import email
import time
from email.header import decode_header




client = discord.Client()



channelsEaster = [client.get_channel(732069480955641977)]

insultos = ["mierda", "puta", "ctm", "conche tu madre", "concha tu madre" , "pico", "puto", "marica","maricon", "maraco", "wea", "weas", "culiao", "ql", "fuck", "shit", "fuck you","asshole", "ass hole", "pussy", "mierda"]

EMAIL_ADDRESS = "masterofchambers22@gmail.com"#os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get("clave") #os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Verificación Chamber Of Secrets'
msg['From']= EMAIL_ADDRESS
msg['To']= ""
contactos = []
#msg['To'] = EMAIL_ADDRESS   ', '.join(contacts)

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1>¡Bienvenido a Chamber of Secrets!</h1>

        <p>Este es un mail de verificación, no es spam. <b>Si es que no crees que debiste haber recibido este mail, envía un mail a boyarzun@dsmorus.cl, jogonzalez@dsmorus.cl o sebamono1@gmail.com. </b>
        <br></br>
        <p> Este es un servidor de trabajo, donde nos juntamos a trabajar todos los días. ¡Su propósito es ayudarnos a organizar mejor nuestro tiempo y estudiar todos juntos!
        <br></br>
        <p> En el servidor podrás:
        <ul> <!--A es para ordenar con ltras, 1 es para numeros, a para minusculas -->
            <li>Avanzar junto a otros en lo que sea que te cueste hacer por lata.</li>
            <li>Ser parte de una de las casas de Howard y trabajar junto a tus compañeros por ver cuál es la mejor.</li>
            <li>Subir de nivel estudiando y ver tu esfuerzo junto a tus amigos.</li>
            <li>Hacer trabajos grupales y... ¡ganar algo acambio!</li>
            <li>Conocer a personas de otros cursos, y cooperar con ellas</li>
            <li>¡Mucho, pero mucho más!</li>
        </ul>
        <p>Si no lo sabías, tenemos un video explicativo para aprender a usar discord:
        <a href="https://youtu.be/VK9456HHoAI" target = "_blank">Cliquea aquí para ver el video</a>
        <br></br>
        <h2>¿Cómo verifico mi mail?</h2>
        <p> Es muy importante que verifiques tu identidad, para proteger a nuestros usuarios. <b>Simplemente responde este mail, contestanto: si, soy yo.</b>
        <br></br>
        <p> PD: Yo soy un bot, por lo que no responderé a tus mensajes. <b>Es muy importante que pongas el mensaje "si, soy yo." exactamente como aparece. NO DEBES INCLUIR NADA MÁS.</b> 
    </body>
</html>
""", subtype='html')

async def scrapEmail(mail):
    #print(mail)
    username = "masterofchambers22@gmail.com"
    password = os.environ.get("claveMail")
    VerifyFound = False
    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    # authenticate
    imap.login(username, password)
    minutos = 0

    while VerifyFound == False or minutos < 15:
        print("iniciando otra ronda")
        status, messages = imap.select("INBOX")
        # number of top emails to fetch
        N = 3
        # total number of emails
        messages = int(messages[0])

        # create an IMAP4 class with SSL
        for i in range(messages, messages-N, -1):
            # fetch the email message by ID
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode()
                    # email sender
                    from_ = msg.get("From")

                    if from_.find(mail)!=-1:
                    # if the email message is multipart
                        print("Subject:", subject)
                        print("From:", from_)
                        if msg.is_multipart():
                            # iterate over email parts
                            for part in msg.walk():
                                # extract content type of email
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))
                                try:
                                    # get the email body
                                    body = part.get_payload(decode=True).decode()
                                    if body.lower().find("si, soy yo.") != -1:
                                        print(body)
                                        minutos = 16
                                        return "valido"

                                    else:
                                        return "inválido"
                                except:
                                    pass

                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    # print text/plain emails and skip attachments
                                    print(body)
                            VerifyFound = True
        await asyncio.sleep(60)

        #time.sleep(20)
    imap.close()
    imap.logout()


def seleccionarSaludo(nombre):
    saludos = ["Bienvenido a la Chamber of Secrets... Puedo sentir un potencial enorme en tí... ¡No lo malgastes y lee las reglas!",
               "Llegará un día en el que las personas dejarán de tener motivación, y la procrastinación y el hacer nada se volverá la norma entre nosotros, pero mientras estemos acá no llegará ese día! Llegará un día en el que la flojera se sobrepondrá a las ganas de aprender, pero mientras estemos acá no llegará ese día! Este día hay que estudiar! Bienvenido, "+nombre+", a La Cámara de los Secretos.",
               "Miren todos! Llegó una nueva @Ameba a este universo!! Y se hace llamar  "+nombre+"! ¿Saben qué significa esto? Toda una nueva rama evolutiva de posibilidades y potencial en su máximo estado! Si consigues hacerte paso por el engorroso camino de la procrastinación, podrás llegar a evolucionar a lo que tú quieras!",
               "¿Todavía tienes guías no hechas o pdfs sin leer, "+nombre+"? Entonces estás en el lugar correcto! Con este nuevo producto, La Cámara de los Secretos, podrás dejar de procrastinar! Solo por hoy!!! Si lees las normas en #reglas_de_uso y podrás entrar al servidor **totalmente gratis**. Además, si escribes el comando de tu curso en #asignador-de-cursos en menos de 15 minutos, podrás ganar 0.5 puntos de experiencia!!. Disfruta del servidor!",
               "Bienvenido a la Cámara de los Secretos,  "+nombre+"! Escribe tu curso en #asignador-de-cursos, consigue una casa en #el-sombrero y empieza a trabajar para subir de nivel y desbloquear contenido exclusivo!",
               "¿Nunca te has preguntado cómo empezaron los más grandes de la historia,  "+nombre+"? Seguramente parecido a ti! Llenos de responsabilidades y ganas de aprender. Lee las normas en #reglas_de_uso y empieza a trabajar para conseguir todos tus objetivos!",
               "¿No te ha pasado,  "+nombre+", que no tienes ganas de hacer algo, pero ves a alguien hacerlo y de repente te dan ganas? Bueno, de eso se trata esto! Lee las normas en #reglas_de_uso y trabaja con nosotros!",
               "Cuando empezaste a andar en bicicleta, todo parecía muy difícil, ¿no,  "+nombre+"?. Pero con práctica puedes llegar a usarla como una herramienta de transporte. Lo mismo ocurre con el manejo del tiempo. Al principio te puede costar, pero luego de unos días te puede dar muchos beneficios!  Espera, ¿no sabes andar en bicicleta?",
               "Por fin llegaste,  "+nombre+"! Todos denle la bienvenida ! ¿Trajiste la pizza?... Ah… No la trajiste... Bueno, te dejaremos entrar pero solo si lees las reglas en #reglas_de_uso. Disfruta del server!",
               "Y así comienza la aventura del héroe... Con un simple mensaje de bienvenida. Llegarás sin duda a lograr cosas inimaginables,  "+nombre+", pero todos los héroes tienen sus inicios... Entonces ¿Por qué no partir leyendo las reglas en #reglas_de_uso?",
               "Érase una vez una @Ameba. Quizás no era el ser vivo más complejo o el más especial, pero la ameba se transformó en todos los animales que conocemos hoy en día. Así que querido "+nombre+", sí, eres una ameba, no te frustres, pues con el tiempo evolucionarás a niveles más y más extraordinarios."]
    mensaje = random.choice(saludos)
    return mensaje

@client.event
async def on_member_join(member):
    print(member.name)
    print(type(member.mention))
    channelWelcome = client.get_channel(720821875587940395)
    await asyncio.sleep(2)
    await channelWelcome.send("bienvenid@ "+member.mention)
    try:
        await channelWelcome.send(seleccionarSaludo(member.name))
    except Exception as e:
        canalError = client.get_channel(722218667034804364)
        await canalError.send(e)


@client.event
async def on_member_update(before, after):
    canalConfirm = client.get_channel(722218667034804364)
    RolesDespues = after.roles
    RolesAntes = before.roles
     
    rolNuevo = [elemento for elemento in RolesDespues if elemento not in RolesAntes]

    ChamberOSlist = client.guilds
    ChamberOS = ChamberOSlist[0]
    COSRoles = ChamberOS.roles
    channelGG = client.get_channel(724350277494374421)
    if rolNuevo[0].id in [724370758054182994, 724370757668438016,724370757081104385,724370754065530901,724370753486848170,724370752568164374,724370751662063648,725098236125380690,725098238067343490,725098234695122964,724370751112740957,724370750274011157,724370747367358696,724300236436013289,724295661104922715,724293405567615098,725096836435673198,725096835865378896,725096833868628010,759807196828663848,759807195029438554,759807193725272156,759807193032687616,759807191459823656,759807190818095105,759807189379973160,759807188368621628,759807187500662824,759807185714151466,759807185709432912,759807183624994866,759807181763248168,759807179589943297,759807182346387456,759807178663002142,759807176650260502,759807175144505405,759807173437554738,759807171541729340]:
      await channelGG.send(f"GG! {after.mention}")
    
    for rol in RolesDespues:
        if rol.id == 724370751112740957: #lvl 10
            for role in RolesDespues:
                if role.id == 737051849726885978: #hufle
                    huffleVIP = [rolu for rolu in COSRoles if rolu.id == 729371025841848410]
                    await after.add_roles(huffleVIP[0])
                if role.id == 737052072356085795:#sly
                    slytherinVIP = [rolu for rolu in COSRoles if rolu.id == 729371132800794735]
                    await after.add_roles(slytherinVIP[0])
                if role.id == 737051589432311860: #gryff
                    gryffindorVIP = [rolu for rolu in COSRoles if rolu.id == 729370944769884261]
                    await after.add_roles(gryffindorVIP[0])
                if role.id == 737051768822956103: #rav
                    ravenVIP = [rolu for rolu in COSRoles if rolu.id == 729371078006145176]
                    await after.add_roles(ravenVIP[0])
        if rol.id == 724370752568164374: #lvl15, relativista temporal
            for role in RolesDespues:
                if role.id == 722214788242997250: #4tomedio
                    VIP = [rolu for rolu in COSRoles if rolu.id == 727277116676243588]
                    await after.add_roles(VIP[0])
                    await channelGG.send(f"Ahora eres admin de curso {after.mention}")
                if role.id == 722214504271970407: #3romedio
                    VIP = [rolu for rolu in COSRoles if rolu.id == 723921067940511784]
                    await after.add_roles(VIP[0])
                    await channelGG.send(f"Ahora eres admin de curso {after.mention}")
                if role.id == 722838229040103445: #2domedio
                    VIP = [rolu for rolu in COSRoles if rolu.id == 728059540020396152]
                    await after.add_roles(VIP[0])
                    await channelGG.send(f"Ahora eres admin de curso {after.mention}")
                if role.id == 727277635528556634: #1ro#medio
                    VIP = [rolu for rolu in COSRoles if rolu.id == 728059656408268809]
                    await after.add_roles(VIP[0])
                    await channelGG.send(f"Ahora eres admin de curso {after.mention}")

@client.event
async def on_ready():
    print("bot 2 on line")

@client.event
async def on_message(message):

    canalPaco = client.get_channel(724700731252408360)
    canalFunao = client.get_channel(736412431819079810)
    ChamberOSlist = client.guilds
    ChamberOS = ChamberOSlist[0]
    COSRoles = ChamberOS.roles
    miembrosCos = ChamberOS.members
    
    miembroAutorLst = []
    if message.content.find("*give")!=-1 :
      await message.channel.send("puntos asignados!")
    if message.channel.id == 722218667034804364 or message.channel.id == 746859644491792514:
      if message.content.find("@dsmorus.cl") != -1 and message.author.id != 728079038664540250:
          msg.replace_header('To', message.content)
          with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
              smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
              smtp.send_message(msg)
          await message.channel.send(f"¡masterofchambers22@gmail.com acaba de mandar el mail de verificación a {message.content}!")
          print("buscando:" + message.content)
          verificado = await scrapEmail(str(message.content))

          if verificado == "valido":
              ChamberOSlist = client.guilds
              ChamberOS = ChamberOSlist[0]
              COSRoles = ChamberOS.roles
              for rol in COSRoles:
                  if rol.id == 739154345639018556:
                      await message.author.add_roles(rol)
              await message.channel.send(f"Mail recibido, se te acaba de añadir el rol, {message.author.mention}")
          if verificado == "invalido":
              await message.channel.send(f"recibí un mail de {message.author.mention}, pero tenía el contenido pedido.")



    if message.content == "*mandame el mail che":
        msg.replace_header('To',EMAIL_ADDRESS )
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        await message.channel.send("mail enviado")

    

    for member in miembrosCos:
        if message.author == member:
            miembroAutorLst.clear()
            miembroAutorLst.append(member)
    miembroAutor = miembroAutorLst[0]
    rolesMiembro = miembroAutor.roles
    purge = "*purge"
    if message.channel == client.get_channel(724350277494374421):
        if message.author.id == 534589798267224065:
            await message.channel.send("GG!")

    if message.content == "*probando":
        await message.channel.send("lo veo")

    for insulto in insultos:
        contenido = str(message.content).lower()
        espacioContenido = (" " + contenido).lower()
        if espacioContenido.find(insulto) != -1:
            await message.delete()
            embed = discord.Embed(title="WARNING", description="alguien usó una palabra blacklisted")
            embed.add_field(name="Usuario", value=message.author)
            embed.add_field(name="Palabra", value=message.content)
            embed.add_field(name="Insulto", value=insulto)
            await canalPaco.send(content=None, embed=embed)
            await canalFunao.send(content=None, embed=embed)
            await message.channel.send("Cuida tu vocabulario!")

        if contenido.find(" " + insulto + " ") != -1:
            await message.delete()
            embed = discord.Embed(title="WARNING", description="alguien usó una palabra blacklisted")
            embed.add_field(name="Usuario", value=message.author)
            embed.add_field(name="Palabra", value=message.content)
            embed.add_field(name="Insulto", value=insulto)
            await canalPaco.send(content=None, embed=embed)
            await canalFunao.send(content=None, embed=embed)
            await message.channel.send("te caché!")

    if message.content == "*COS":
        COS = client.get_guild(720821875587940392)
        await message.channel.send(str(COS))

    if message.channel.id == 724350277494374421:
        if message.content.find("Felicidades")!=-1:
            await message.channel.send("GG!")

    if str(message.channel) == "eastereggs":
        if message.content == "*Homero":
            await message.channel.send("@everyone ¡Soy Homero Chino!")

        if message.content == "*Shootit":
            await message.channel.send("@everyone Shooting Stars")

        if message.content == "*Eu Macaco":
            await message.channel.send("@everyone Ha aparecido un simio salvaje")

        if message.content == "*Troll Me":
            await message.channel.send(file=discord.File("trollface.png"))

        if message.content == "*UwU":
            await message.channel.send("@everyone UwU")



async def mostrarHora():
    await asyncio.sleep(20)
    COSl = []
    for guild in client.guilds:
        COSl.append(guild)
    COS = COSl[0]
    channelReady = client.get_channel(725531375477719060)
    while True:
        await asyncio.sleep(20)
        now = datetime.datetime.now()
        global hora
        hora = now.strftime("%H:%M")
        print(hora)
        hoursAntiAfk = ["03:00","04:00","05:00", "06:00","07:00", "09:00", "11:00", "12:00",
                        "14:00", "20:00", "22:00", "23:00", "24:00", "01:00", "02:00"]

        horas = ["18:45","15:50"]
        # 4 horas de adelanto
        if hora in hoursAntiAfk:
            print("el mensaje se mandó")

            miembrosVoiceSF = []
            miembrosVoice = []
            miembrosVoiceSF.clear()
            miembrosVoice.clear()
            for voiceChannel in COS.voice_channels:
                miembrosVoiceSF.append(voiceChannel.members)

            for miembro in miembrosVoiceSF:
                if miembro != []:
                    miembrosVoice.append(miembro[0])
            try:
              for miembro in miembrosVoice:
                    if int(miembro.id) not in [235088799074484224,159985870458322944,547905866255433758, 234395307759108106]:
                        await miembro.move_to(client.get_channel(724425478034817065))
            
            except Exception as e:
                await channelReady.send(e)

            await asyncio.sleep(60)

        if hora in horas:
            print("el mensaje se mandó")
            await channelReady.send('se movió a los usuarios a las '+hora)
            miembrosVoiceSF = []
            miembrosVoice = []
            miembrosVoiceSF.clear()
            miembrosVoice.clear()
            for voiceChannel in COS.voice_channels:
                miembrosVoiceSF.append(voiceChannel.members)

            for miembro in miembrosVoiceSF:
                if miembro != []:
                    miembrosVoice.append(miembro[0])
            try:
                for miembro in miembrosVoice:
                    if int(miembro.id) not in [235088799074484224,159985870458322944,547905866255433758,234395307759108106]:
                        await miembro.move_to(client.get_channel(724425478034817065))
            except Exception as e:
                await channelReady.send(e)

            await asyncio.sleep(60)


keep_alive.keep_alive()
client.loop.create_task(mostrarHora())
client.run(os.environ.get("Token"))
