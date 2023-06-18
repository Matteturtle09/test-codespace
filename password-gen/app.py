'''Libreria per generare valori casuali'''
import random

# in questa variabile sono contenute tutte le lettere
CHARACTERS = 'qwertyuiopasdfghjklzxcvbnm'

# in questa variabile sono contenute tutte le cifre
NUMBERS = '1234567890'

# l'utente seleziona la lunghezza della password
PASSWORD_LENGTH = int(input('Lunghezza Password: '))

# variabile password vuota
PASSWORD = []

for i in range(PASSWORD_LENGTH):   
    PASSWORD.append(random.choice(CHARACTERS + NUMBERS)) # aggiungiamo un carattere o un numero alla password

print(''.join(map(str, PASSWORD))) # stampiamo il risultato sotto forma di stringa