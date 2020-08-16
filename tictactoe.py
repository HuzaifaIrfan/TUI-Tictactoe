from os import system


print("\nTic Tac Toe ")
print("Made By Huzaifa Irfan ")
print("\nWelcome ")

player1=input("Name of Player1\n")
player2=input("Name of Player2\n")


input("Press Enter to Start")


running = True

game=[0,0,0,0,0,0,0,0,0]

display=[{"id":0,"char":"-"},{"id":1,"char":"X"},{"id":2,"char":"O"}]

players=[{"id":1,"name":player1,"score":0},{"id":2,"name":player2,"score":0}]



xnow=True


def clearscreen():
	system("clear")


def getchar(gotid):
	for obj in display:
		if obj["id"]==gotid:
			return obj["char"]

def asknum(whatval):
	anum=None
	while(anum==None):
		try:
			anum=int(input(whatval))
		except:
			print("Number required (from 1-9) ")
			continue

		if (anum <1 or anum >9):
			print("Write a Number (from 1-9) ")
			anum=None


	return anum



def exitter(val):
		input(val)





def playagain():
	global game
	game=[0,0,0,0,0,0,0,0,0]
	play=input("Do you want to play again y/n ")
	if play=="n":
		running=False




def winner(idnow):
	for player in players:
		if player["id"]==idnow:
			clearscreen()
			print(player["name"],"Wins")
			player["score"]=player["score"]+1
			playagain()



winpattern=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]


def checkwinner(idnow):
	for apattern in winpattern:
		if (game[apattern[0]]==idnow and game[apattern[1]]==idnow and game[apattern[2]]==idnow):
			winner(idnow)

def checker():
	for player in players:
		idnow = player["id"]
		checkwinner(idnow)


def checktie():
	clearscreen()
	filled=0
	for pos in game:
		if pos != 0:
			filled=filled+1

	if filled==9:
		print("Game Tied ")
		playagain()


while(running):
	
	clearscreen()

	print("\nTic Tac Toe ")
	print("Made By Huzaifa Irfan ")

	for player in players:
		print(player["name"]," : ",player["score"])

	print("\n")
	idnow=0
	if xnow == True:
		print(players[0]["name"]+"'s Turn\n")
		idnow=1
	else:
		print(players[1]["name"]+"'s Turn\n")
		idnow=2

	print(getchar(game[0])," ",getchar(game[1])," ",getchar(game[2]))
	print(getchar(game[3])," ",getchar(game[4])," ",getchar(game[5]))
	print(getchar(game[6])," ",getchar(game[7])," ",getchar(game[8]))

	position=asknum("\nEnter location (1-9) to click ")

	if game[position-1]==0:
		#exitter("continue game")
		game[position-1]=idnow
		checker()
		xnow = not xnow
	else:
		exitter("please select another location ")

	checktie()

	clearscreen()

print("Bye Bye ")

print("See You Soon ")
