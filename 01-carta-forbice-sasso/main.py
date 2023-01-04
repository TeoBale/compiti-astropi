from random import randrange 
# dalla libreria importa la funzione che ci serve

print("Carta forbice sasso") # Stampiamo il titolo
print("Inserisci il numero corrispondente alla tua scelta !") # Spieghiamo come si gioca

# Stampiamo a schermo le opzioni
print("[1] -> Carta")
print("[2] -> Forbice")
print("[3] -> Sasso")

# Dizionario contenente tutte le opzioni
dictionary = {
'1-1': None,
'2-2': None,
'3-3': None,

'1-2': 'B',
'1-3': 'A',

'2-3': 'B',
'2-1': 'A',

'3-1': 'B',
'3-2': 'A',
}

# Questa funzione prende due argomenti e restituisce il vincitore
def check(a, b): 
	winner = dictionary[f"{a}-{b}"]
	return winner

# Definiamo il punteggio
wins = (0, 0) 

# Loop con 3 interazioni	
for  interaction  in  range(3):
	print(f"Siamo al {interaction+1} round !")
	
	user_option = input('Inserisci un numero da 1 a 3')
	bot_option = randrange(1, 4)

	round_winner = check(user_option, bot_option)
	if not round_winner:
		print("Parità !")
	elif round_winner == 'A':
		print('Hai vinto il round !')

		# Modifichiamo il punteggio
		wins = (wins[0] + 1, wins[1])
		
	elif round_winner == 'B':
		print('Hai perso il round T.T')
		
		# Modifichiamo il punteggio
		wins = (wins[0], wins[1] + 1)


if  wins[0] == wins[1]:
	print('Wow, siete pari !')
elif  wins[0] > wins[1]:
	print('Bravo, hai vinto !')
else:
	print('Mi dispiace... hai perso.. Sono troppo forte :P')
