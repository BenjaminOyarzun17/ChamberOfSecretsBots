# Project description
This repository gathers three discord bots created for the discord server "La camara de los secretos", which is the community server of the chilean school "Deutsche Schule Sankt Thomas Morus". 
<br/>
The aim of this markdown is then to show the commands that these bots support, in case some fellow classmate needs the code for some reason. 
<br/>

# KnowledgeController
This first bot was created in order to make the server more user-friendly. That is to say, it is a support bot that has many help commands. 
<br/>
## `*Tipps`
This command displays a random help message, which is chosen from the tipps list. Some possible messages are:
- En las salas que dice relajo no se pueden ganar puntos ni xp. 
- Si encuentras un easteregg nuevo puedes ganar xp y puntos extra para tu casa.
- Esto puede sonar raro, pero tenemos tres sistemas de rankings. El primero es el de nivel personal, que mide tu participación en general (mensajes, horas conectado en channels de voz, etc...). Puedes ver tu experiencia en #chat-top. \nEl segundo mide tu actividad en canales de voz mensualmente, en donde los puntos que ganas se juntan con los de tu casa de Hogwarts para el torneo de casas. Esto lo puedes ver en #torneo-de- casas. \nFinalmente está el ranking de casas medido en conocimientos, que muestra el top de casas ganadoras por temporada. Esto lo puedes ver en #resultados-torneos.

## `*UsuarioDelTiempo`
This is a hidde function, which was created for the 2020 closure event. Here, a prize would be given to the user that used the timer bot the most. This message sends a dictionary-like data structure, which contains the amount of times a given user used the timer bot. 

# TimeController
This bot works as a timer. After a timer ends, a user gets a mention, which tries to catch the users attention. 
## `?set timer (title) <minutes>`
This command sets a timer that lasts a given amount of minutes. The title intends to give a description to the timer. 
# MasterOfChambers (aka. Lil'Master of Chambers)
This is a moderation and helper bot. Here are some of it's main functions:
1. It handles the user authentication process, which runs whenever a user joins the server. There is a reserved channel for email registration, which only accepts emails that belong to the community (@dsmorus.cl).2. It assigns the "verified" after the registration email was succesfully sent. 
3. It sends a warning message to the admins in case a blacklisted word was sent. 
4. It performs a special action in case an easteregg was discovered in the "eastereggs" channel. 
Important notice: This bot is mainly a administrative bot. Therefore, it doesn't provide many noteworthy commands that should be described in this guide. If you're still curious about it's capabilities, you should directly read the source code. 
# TheMasterOfChambers
This is arguably the most important bot. The following functionalities are provided by this fellow:
1. It stores the amount of time a user spent on a given voice channel. This count is then used for the ranking that belongs to the "houses tournament". 
	* There is a special functionallity enabled, which regulates the amount of xp given in relationship of the user's status. I.e, more xp will be given if the user has it's camera turned on. 
2. It supports many commands that are related to the "houses tournament"
3. Many other functions that now will be listed below. 

## `*misPuntos`
Displays the amount of xp points that the user has won during the last season. 
## `*Accio <item>`
Given any item, it perfoms a google image search, and sends that google image, just as if you had used the "accio" spell. 
## `*rank casas`
Shows the house's ranking. It returns an embed, which by default sorts the results. 
## `*rank <house>`
The only possible houses are [Ravenclow, Griffindor, Slytherin, Hufflepuff]. It displays the inner rank from a specific house. Important notice: this ranking is public. Thus, anyone can acces it, regardless the house the user belongs to. 
## `*<course>`
This command assigns a course role. The possible courses are ["4toMedio","2doMedio", "3roMedio", "5toBásico", "8voBásico", "7moBásico","6toBásico"] 
## `*<spell>`
It performs a Harry Potter spell. The author encourages the user to test a few of them to see what happens. 
## `*help`
Sends an embed that resumes all the commands that are publicaly available (this also considers the other three bots).
## `iniciar test de casas`
If the user does not belong to any hogwarts house, it randomly assigns a house to the user. 
# Final words
This project was implemented during 2020's quarantine. It's aim was to reduce the social distance created by covid by creating a common platform where the students had a chance to gather and enjoy themselves. The server is still active, but nowadays it is not anymore what it used to be. 
Therefore, fellow classmate, if you are reading this...
Fork this project, and try to customize it for your own needs...
Maybe, you will be able to revive this wonderful server, which once gave us some unforgettable times. 

-MOB17; the admin. 


