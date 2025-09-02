#import discord

#TOKEN = "" insert token here

#client = discord.Client()

#client.run(TOKEN) 

#Difficulty 1-5 is able to be beat if you move first, (1 1), (2,2), (1,3), (1,2)
#from random import seed
from posixpath import split
from random import randint
from discord.ui import Button, View
from bs4 import BeautifulSoup
import requests
from copy import deepcopy
from json.encoder import INFINITY
import math
import copy
from random import random
import discord
import asyncio
import wonderwords
from discord.ext import commands
#intents = discord.Intents.all()
#bot = discord.Bot(intents=intents)
#from discord.ext import commands #fore discrodions

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix='*', intents=intents, case_insensitive = True)

@client.event
async def on_ready():
    print('We have successfully loggged in as {0.user}'.format(client))
    await client.get_guild(1009659198688219166).get_channel(1009801995152007299).send("Perosn joined the chat")
word = "Hello This is a test"
bot_move  = False
board =  [['X', 'X','X'],
          ['y', 'y','y'],
          ['X', 'X','X']] 
bot_depth = 0
p1sign = '🇽'  
p2sign = '🅾️'
spots_remaining =9  
player1 = ''
player2 = str()
playersturn = ''
already_used = []
all_letters = []
sentence = []
letters_wrong = 0 
setword = False
hangman = False
body = [' \n :) \n \n ',
'\n(\n', F
'\n()\n',
'\n()-\n',
'man \n  \ \n()-\n', 
'man \n  \ \n()-\n  /',
'man \n  \ \n()-|\n  /',
'man \n  \ \n()-||\n  /',
'man \n  \ \n()-|||\n  /',
'man \n  \     / \n()-|||\n  /',
'man\n  \     / \n()-|||\n  /     \x5c',]

#   \   /
# ()----
#   /   \


#   ____________
#  |            |
#  |            O
#  |           /|\
#  |            |
#  |           / \
# _|_
#|   |______
#|          |
#|__________|
#|                  |\n
body2 = [
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |\n   |\n   |\n   |\n \_|\_ \n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |\n   |\n   |\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /\n   |\n   |\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\n   |\n   |\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\x5c\n   |\n   |\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\x5c\n   |             |\n   |\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\x5c\n   |             |\n   |           / \n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
    ':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\x5c\n   |             |\n   |           / \x5c\n \_|\_\n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|',
]
    
    #':) \n     \__\__\__\__\__\__\n   |             |\n   |            O\n   |           /|\x5c\n   |             |\n   |           / \x5c\n \_|\_ \n|     |\__\__\__\__\__\_\n|\__\__\__\__\__\__\__\__|'    ####__\|__\ \n|   |__\__\__ \n|          |\n|__\__\__\__\__|\n'

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

@client.command()
async def nsfw(ctx):
    await ctx.send("https://matias.ma/nsfw/")
@client.command()
async def new_game(ctx):
    global player1,player2,board,spots_remaining,p1sign,p2sign
    p1sign = '🇽'  
    p2sign = '🅾️'
    spots_remaining = 9
    board =[
          ['   ', '   ','   '],
          ['   ', '   ','   '],
          ['   ', '   ','   ']] 
    player1 = str()
    player2 = str()
    await ctx.send("New game started, looking for players")
    #await print_board(ctx)
async def check_win(game):
    for x in range(3):
        character = game[x][0]
        winning = True
        if character == "   ":
            winning = False
        for y in range(3):
            if character != game[x][y]:
                winning = False
        if winning == True:
            return(True)

    for x in range(3):
        character = game[0][x]
        winning = True
        if character == "   ":
            winning = False
        for y in range(3):
            if character != game[y][x]:
                winning = False
        if winning == True:
            return(True)
    if game[0][0] == game [1][1] and game[0][0]== game[2][2] and game[0][0] != "   ":
        #print("DIAGNOAL 1")
        return(True)
    if game[2][0] == game [1][1] and game[2][0]== game[0][2] and game[2][0] != "   ":
        #print("DIAGNOAL 2")
        return(True)

async def min_max(depth,game,player,ctx,starting_depth):
   # print("called")
    #player = letter eg 'X'
    best_move = 0 
    best_score  =  0
    if player == "X":
        next_player = 'O'
        best_score = INFINITY
    else:
        next_player = 'X'
        best_score = -INFINITY
    if await check_win(game)== True:
        #print("FOUND WIN ")
        
        if next_player =="O": #The player that moved before this turn is the current next player 
            return(10)
        else:
            return(-10)

    if depth > 0 :
        
        for i in range(9):
            #print(str(math.floor(i/3))+str(i%3))
            #await ctx.send("new depth" + str(depth))
            if not game[0].__contains__('   ') and not game[1].__contains__('   ')  and not game[2].__contains__('   ') :
                #print("Full board ")
                return(0)
            if game[math.floor(i/3)][i%3] == '   ':
                new_board = copy.deepcopy(game)
                new_board[math.floor(i/3)][i%3] = player
                
               
                if depth != starting_depth:
                    if player == "O":
                        best_score = (max(await  min_max(depth-1,new_board,next_player,ctx,starting_depth),best_score))
                    else:
                        best_score = (min(await  min_max(depth-1,new_board,next_player,ctx,starting_depth),best_score))
                else:
                    if player == "O":
                        score = await min_max(depth-1,new_board,next_player,ctx,starting_depth)
                        
                        if  score >best_score:

                            best_move = i 
                            best_score = score
                    else:
                        score = await min_max(depth-1,new_board,next_player,ctx,starting_depth)
                        
                        if  score <best_score:
                            best_move = i 
                            best_score = score
        if depth != starting_depth:
            return(best_score)
        else:
            print(best_score)
            return(best_move)
    else:
        return(0)

@client.command()
async def add_bot(ctx , difficulty: int ):
    global bot_depth,playersturn,player1,player2
    if player1 == '':
        player1 = "Bot"
        await ctx.send("Botman Joined as player1")
        bot_depth = difficulty
    elif player2 == '':
        player2 = "Bot"
        await ctx.send("Botman Joined as player2")
        playersturn = player1
        bot_depth = difficulty
        playersturn = player1
        #await ctx.send( ctx.author.mention + " Joined as player2")
        await ctx.send("Game is now full")
        if player1 !="Bot":
            await ctx.send("<@"+str(player1)+ "> It is now your turn")
    else:
        await ctx.send("Game is full")


@client.command()
async def join_game(ctx, sign):
    global player1,player2,playersturn,p1sign,p2sign
    if player1 == '':
        player1 =  ctx.author.id
        if sign != "":
            p1sign = sign
        message = await ctx.send( ctx.author.mention + " Joined as player1")
        await message.add_reaction(p1sign)
        
    elif player2 == '':
        if player1 != ctx.author.id:
            player2 =  ctx.author.id
            if sign != "":
                p2sign = sign
            playersturn = player1
            message = await ctx.send( ctx.author.mention + " Joined as player2")
            await message.add_reaction(p2sign)
            await ctx.send("Game is now full")
            if player1 !="Bot":
                await ctx.send("<@"+str(player1)+ "> It is now your turn")
            else:
                move = await  min_max(bot_depth,board,'X',ctx,bot_depth)
                if playersturn == player1:
                    board[math.floor(move/3)][move%3] = "X"
                else:
                     board[math.floor(move/3)][move%3] = "O"
                playersturn = player2
                await print_board(ctx, "X", "O")
                await ctx.send("<@"+str(playersturn)+ "> It is now your turn")
        else:
            await ctx.send("Sorry you can not play agaisnt yourself")
    else:
        await ctx.send("Game is full")

#@client.command()
#async def num(ctx):
    #if ctx.author.id == player1:


async def print_board(ctx, player_character, opposing):
    global player1, player2, playersturn 
    print_board = str()
    for x in range(3):
        out = ''
        for y in range(3):
            out += '|'
            out += board[x][y]
            #if y != 2:
        out += "|"
        print_board += out 
        
   
        print_board += '\n'
    print_board= print_board.replace("O", p2sign)
    print_board = print_board.replace("X", p1sign)
    print_board =print_board.replace("   ", "⬛")
    
    await ctx.send(print_board)
    


   
    for x in range(3):
        character = board[x][0]
        winning = True
        if character == "   ":
            winning = False
       
        for y in range(3):
            if character != board[x][y]:
                winning = False
        if winning == True:
            if bot_move == False:
                await ctx.send(ctx.author.mention + "Won")
            else:
                message  = await ctx.send("@Person" + "Won")
                await message.add_reaction('🇱')
                await message.add_reaction('🇧')
                await message.add_reaction('🇴')
                await message.add_reaction('🇿' )
                await message.add_reaction('😴')
                await message.add_reaction('💪🏻')
                await message.add_reaction('👏🏻')

            player1 = ''
            player2 = ''
            playersturn = ''
    

    for x in range(3):
        character = board[0][x]
        winning = True
        if character == "   ":
            winning = False
        for y in range(3):
            if character != board[y][x]:
                winning = False
        if winning == True:
            if bot_move == False:
                await ctx.send(ctx.author.mention + "Won")
            else:
                message  = await ctx.send("@Person" + "Won")
                await message.add_reaction('🇱')
                await message.add_reaction('🇧')
                await message.add_reaction('🇴')
                await message.add_reaction('🇿' )
                await message.add_reaction('😴')
                await message.add_reaction('💪🏻')
                await message.add_reaction('👏🏻')
            player1 = ''
            player2 = ''
            playersturn = ''
    if board[0][0] == board [1][1] and board[0][0]== board[2][2] and board[0][0] != "   ":
        if bot_move == False:
            await ctx.send(ctx.author.mention + "Won")
        else:
            message  = await ctx.send("@Person" + "Won")
            await message.add_reaction('🇱')
            await message.add_reaction('🇧')
            await message.add_reaction('🇴')
            await message.add_reaction('🇿' )
            await message.add_reaction('😴')
            await message.add_reaction('💪🏻')
            await message.add_reaction('👏🏻')
        player1 = ''
        player2 = ''
        playersturn = ''
    if board[2][0] == board [1][1] and board[2][0]== board[0][2] and board[2][0] != "   ":
        if bot_move == False:
            await ctx.send(ctx.author.mention + "Won")
        else:
            message  = await ctx.send("@Person" + "Won")
            await message.add_reaction('🇱')
            await message.add_reaction('🇧')
            await message.add_reaction('🇴')
            await message.add_reaction('🇿' )
            await message.add_reaction('😴')
            await message.add_reaction('💪🏻')
            await message.add_reaction('👏🏻')
        player1 = ''
        player2 = ''
        playersturn = ''
        


@client.command()
async def play(ctx, ypos: int, xpos: int):
    global playersturn,spots_remaining,bot_move
    bot_move  = False
    if ctx.author.id == playersturn:
        #await ctx.send(position )
        if playersturn == player1:
            if board[xpos-1][ypos-1] == '   ':
                board[xpos-1][ypos-1] = "X"
                spots_remaining -=1  
                #await ctx.send('X')
                playersturn = player2
                await print_board(ctx, "X", "O")
                if playersturn != "Bot":
                    await ctx.send("<@"+str(playersturn)+ "> It is now your turn")
                else:
                    await ctx.send("@"+'Person'+ " It is now your turn")
                    move = await  min_max(bot_depth,board,'O',ctx,bot_depth)
                    bot_move  = True
                    #if playersturn == player1:
                    board[math.floor(move/3)][move%3] = "O"
                    spots_remaining -=1  
                   # else:
                        #board[math.floor(move/3)][move%3] = "O"
                    playersturn = player1
                    await print_board(ctx, "O", "X")
                    if player1 != '':
                        await ctx.send("<@"+str(playersturn)+ "> It is now your turn")
            else:
                await ctx.send("NAh they trynna cheat")
        else:
            if board[xpos-1][ypos-1] == '   ':
                board[xpos-1][ypos-1] = "O"
                spots_remaining -=1  
                #await ctx.send('O')
                playersturn = player1
                await print_board(ctx, "O", "X")
                if playersturn != "Bot":
                    await ctx.send("<@"+str(playersturn)+ "> It is now your turn")
                else:
                    await ctx.send("@"+'Person'+ " It is now your turn")
                    move = await  min_max(bot_depth,board,'X',ctx,bot_depth)
                    bot_move  = True
                    #if playersturn == player1:
                    board[math.floor(move/3)][move%3] = "X"
                    spots_remaining -=1  
                   # else:
                       # board[math.floor(move/3)][move%3] = "O"
                    playersturn = player2
                    await print_board(ctx, "X", "O")
                    if player2 != '':
                        await ctx.send("<@"+str(playersturn)+ "> It is now your turn")
                #await ctx.send(player2.mention +" It is now your turn")
            else:
                await ctx.send("NAh they trynna cheat")

    #try:
      ##  msg = await client.wait_for("message", timeout=30) # 30 seconds to reply
        #await ctx.send(msg)
    #except asyncio.TimeoutError:
       # await ctx.send("Sorry, you didn't reply in time!")
async def print_hang(ctx):
    #await ctx.send("printing hangman")
    global setword,letters_wrong
    letters_wrong = 0 
    if setword == True:
        letters_wrong = 7
        setword = False
    global hangman
    hang_board = []
    for i in sentence:
        hang_board.append(i)
        hang_board.append(' ')
    board =''
    for i in hang_board:
        board += i
    await ctx.send(board)
    #for i in body2:
        #await ctx.send(i)
    if letters_wrong <= len(body2)-1:
        await ctx.send("test")
        await ctx.send(body2[letters_wrong])
        await ctx.send('Letters tried ' +' '.join([str(elem) for elem in already_used]))
    if not sentence.__contains__("-"):
        await ctx.send("Congrats you win!")
        hangman = False
    if letters_wrong == len(body2)-1:
        await ctx.send("Naw ur rlly just that bad \n The right answer is...")
        for i in range(len(sentence)):
            sentence[i] = all_letters[i]
        
        board =''
        for i in sentence:
            board += i
        await ctx.send(board)
        hangman = False
    


@client.command()
async def letter(ctx, letter: str):
    global letters_wrong
    if hangman == True:
        if letter != " " :
            if not already_used.__contains__(letter):
                already_used.append(letter)
                if all_letters.__contains__(letter):
                    for i in range(len(sentence)):
                        if all_letters[i] == letter:
                            sentence[i] = letter
                else:
                    letters_wrong += 1
        await print_hang(ctx)
    else:
        await ctx.send("Game currently not running")
   

   
@client.command()
async def sentence(ctx, letter: str):
    print("what")
    global sentence, all_letters,letters_wrong
    if hangman:
        if letter.casefold() == word.casefold():
            print("true")
            print(all_letters)
            for i in range(len(sentence)):
                sentence[i] = all_letters[i]
        else:
            print(word)
            print(letter)
            letters_wrong +=1
       
        await print_hang(ctx)
    else:

        await ctx.send("Game currently not running")

@client.command()
async def hangman(ctx):
    global already_used,all_letters,sentence,letters_wrong,hangman,word,setword
    letters_wrong = 0 
    already_used = []
    from wonderwords import RandomSentence
    s = RandomSentence()
    word = s.sentence().casefold()
    word = word[:-1]
    if setword == True:
        word = "anthony"
    
    print(word)
   # word = "hello this is a test"
    all_letters = [*word]  #word.split()
    sentence = [*word]#word.split()
    for i in range(len(sentence)):
        if sentence[i] != ' ':
            sentence[i] = '-'
        else: 
            sentence[i] = '    '
    hangman = True
    await print_hang(ctx)
  


@client.command()
async def guess(ctx,name:str):
    if name == "tannishtha":
        await ctx.send("true")
    else:
        await ctx.send("false")


@client.command()
async def quiet(ctx):
    message = await ctx.send("Shush!")
    await message.add_reaction('🤫')
    message = await ctx.send("Shush!")
    await message.add_reaction('🤫')
    message = await ctx.send("You Can \n Shush!!! urself")
    await message.add_reaction('🤫')
    message = await ctx.send("You Can \n Shush!!! urself")
    await message.add_reaction('🤫')
@client.command()
async def who(ctx):
    if round(randint(0,3)) == 1:
        await ctx.send("Ever...")
        await ctx.send("Aksed!")
    else:
        await ctx.send("Cares")


@client.command()
async def local_weather(ctx):
    url = 'https://weather.com/weather/today/l/38.72,-121.34?par=google'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    temp = soup.find("span", class_="CurrentConditions--tempValue--3a50n")
    #high = soup.find('a', class_="Column--innerWrapper--1vUk1  Button--default--3zkvy")
    high = soup.find_all("div", class_="Column--temp--5hqI_") #[1]
    days = soup.find_all('span',class_="Ellipsis--ellipsis--1sNTm")
    await ctx.send("Current tempature of Antelope "+str(temp.text))

    for i in range(5):
        await ctx.send(f"{days[13+i].text} 's high is {high[9+i].text}")


class DayButton(Button):
    days = {
        'Mon' : "Monday",
        'Tue' : "Tuesday",
        'Wed' : "Wednesday",
        'Thu' : "Thursday",
        'Fri' : "Friday",
        'Sat' : "Saturday",
        'Sun' : "Sunday",
    }
    myweather = []
    current_temp = 0 
    myindex = 0
    mylocation = ''
    print = ''
    def __init__(self,i,weatherData,index,location,current_temp):
        super().__init__(label = i[0], style = discord.ButtonStyle.green)
        self.myweather = weatherData
        self.myindex  = index 
        self.mylocation = location
        self.current_temp = current_temp
    

    async def callback(self,interaction):
        
       
        self.print = ' '
        if self.myindex !=0:
            self.day = self.days[self.myweather[self.myindex][0]]
        else:
            self.day = "Today"
        self.print += ("Weather Forecast on " + self.day +" for: " + self.mylocation )
        self.print+= "\n"
        self.print += "The high will be: " +self.myweather[self.myindex][1]
        if self.myindex == 0:
            self.print += '\n'
            self.print += "The current tempature is " + self.current_temp
        await interaction.response.send_message(self.print)


@client.command()
async def weather(ctx, location):
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0" # can be found with https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    }

    params = {
    "q": "weather in " + location, #Questoin
    "gl": "us",
    "hl": "en",
    "num": "100"
    }


    url = 'https://www.google.com/search?q='

    response = requests.get(url, headers=headers, params=params)

    weather = [] #[day high]
    today = [] #currnet temp, high
    soup = BeautifulSoup(response.text,'lxml')

    
    spell_check = soup.find('a',id="fprsl")

    if spell_check != None:
        location = spell_check.text.strip('weather for ')

    temp = soup.find('span', id="wob_tm").text
    d  = soup.find('div', class_="wob_df wob_ds")  #wob_df
    day = d.find('div', class_="Z1VzSb").text
    high = d.find('span',class_="wob_t").text
    
    today.append(temp)
    today.append(high)
   
    days  = soup.find_all('div', class_="wob_df")
   
    for d in days:
        day = d.find('div', class_="Z1VzSb").text
        high = d.find('span',class_="wob_t").text
        weather.append([day,high])

    #print = ' '
    
    async def forecast(interaction):
        

        
        print = ' '
        temp = soup.find('span', id="wob_tm").text
        print += ("Weather Forecast For: " + location)
        print+= '\n'
        print += ("The current temapture is " + today[0])#+temp)
        print+= '\n'

        d  = soup.find('div', class_="wob_df wob_ds")  #wob_df
        day = d.find('div', class_="Z1VzSb").text
        high = d.find('span',class_="wob_t").text
        print += ("The high for today is " + today[1]) #+str(high) )
        print+= '\n'
    
        days  = soup.find_all('div', class_="wob_df") 
        for d in weather:
            #day = d.find('div', class_="Z1VzSb").text
            #high = d.find('span',class_="wob_t").text
            print +=("The high for " +d[0] + ' is ' +d[1] )
            print+= '\n'
        await interaction.response.send_message(print)
    
    
        # look for interaction.smth to get button name https://discordpy.readthedocs.io/en/latest/interactions/api.html
        #for i in weather:
         #   if i [0] == button.name():
          #      index = i

        

    button = Button(label = "forecast", style = discord.ButtonStyle.green)
    
    button.callback = forecast
    view = View()
    view.add_item(button)
    
    for index, i in enumerate(weather):
        if index != 0:
            b = DayButton(i,weather,index,location,today[0])
        else:
            b = DayButton(['Today'],weather,index,location,today[0])
        #b.callback = print_day()
        view.add_item(b)

    await ctx.send(view = view )


@client.command()
async def day(ctx,):
    print = ''
    url = 'https://nationaldaycalendar.com/what-day-is-it/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')


    date = soup.find('div', class_="title-info").text
    year = date.split()[5]
    print += date
    
    
    info = soup.find('div', class_="info")
    moreinfo = info.find_all('span', class_="box-info-result")
   
    daynumb = moreinfo[0].text
    weeknumb = moreinfo[1].text
    percent = moreinfo[2].text
    percent = percent.split()[0]

    
    print += 'It is day number ' +daynumb +'\n'
    print += 'It is week number ' +weeknumb +'\n'
    print += 'We are ' +percent +" of the way through " +year +'\n'
    
   
    print += "Today is: " +'\n'
    national_days = soup.find_all("span",class_="evcal_desc2 evcal_event_title")
    for i in national_days:
        print += i.text
        print += '\n'
    await ctx.send(print)

@client.command()
async def calc(ctx, equation):
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0" # can be found with https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    }

    params = {
    "q": "what is  " + equation, #Questoin
    "gl": "us",
    "hl": "en",
    "num": "100"
    }


    url = 'https://www.google.com/search?q='

    response = requests.get(url, headers=headers, params=params)

    soup = BeautifulSoup(response.text, "lxml")
    answer = soup.find('span', class_="qv3Wpe")
    #print(answer)
    await ctx.send(answer.text)

@client.command()
async def time(ctx, place):
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0" # can be found with https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    }

    params = {
    "q": "time in the  " + place, #Questoin
    "gl": "us",
    "hl": "en",
    "num": "100"
    }


    url = 'https://www.google.com/search?q='
    response = requests.get(url, headers=headers, params=params)
    soup = BeautifulSoup(response.text,'lxml')
    time = soup.find('div', class_="gsrt vk_bk FzvWSb YwPhnf")
    await ctx.send("It is " +time.text +' in '  +place)


@client.command()
async def button(ctx ,  description =  "blah blah blahj" ):
    button = Button(label="Ciclk me", style= discord.ButtonStyle.green, emoji= "👌")
    button2 = Button(label="Ciclk me", style= discord.ButtonStyle.danger, emoji= "😘")
    button3 = Button(label="Ciclk me", url = 'https://www.youtube.com/watch?v=fcZXfoB2f70',style= discord.ButtonStyle.green, emoji= "😉")
    
    async def button_callback(interaction):
        await interaction.response.send_message("https://matias.ma/nsfw/") 
    
    async def button_callback1(interaction):
        await interaction.response.send_message("Tanishtha is a loser") 
    
    button.callback = button_callback1

    view = View()#button,button2,button3)
    view.add_item(button)
    view.add_item(button2)
    view.add_item(button3)
    #view.remove_item(button)
    await ctx.send("test", view=view)

#@bot.slash_command()
#async def hi(ctx, name: str = None):
#    name = name or ctx.author.name
 #   await ctx.respond(f"Hello {name}!")

@client.command()
async def correct(ctx, sentence):
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0" # can be found with https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    }

    params = {
    "q": "how to spell  " , #Questoin
    "gl": "us",
    "hl": "en",
    "num": "100"
    }


    url = 'https://www.google.com/search?q='
    for i in sentence.split():
        params["q"] = "how to spell  " +i
       # print(params['q'])
        response = requests.get(url, headers=headers, params=params)
        soup = BeautifulSoup(response.text, "lxml")
        spelled_right = soup.find('a',id="fprsl" )
        #print(spelled_right)
        #print(i)
        if spelled_right !=None:
            spelled_right =spelled_right.text.replace('how to spell ','',1)
            await ctx.send("You spelt " + i + " wrong, did you mean " +spelled_right)

@client.command()
async def air(ctx, place):
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0" # can be found with https://www.whatismybrowser.com/detect/what-is-my-user-agent/
    }

    params = {
    "q": "Air quality in  " +place, #Questoin
    "gl": "us",
    "hl": "en",
    "num": "100"
    }
    url = 'https://www.google.com/search?q='
    response = requests.get(url, headers=headers, params=params)
    

    soup = BeautifulSoup(response.text, "lxml")
    air = soup.find('span' ,class_="wYbWKb")
    await ctx.send("The air quality in " +place +' is ' +air.text)


TOKEN = '' your token here
client.run(TOKEN) 
#weather('antelope')

