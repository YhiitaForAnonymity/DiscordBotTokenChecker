import discord
from colorama import Fore, init
import ctypes
import msvcrt  # Importiere msvcrt für Tasteneingabe

# Initialisiere colorama
init()

def check_login(token):
    try:
        intents = discord.Intents.default()
        intents.members = True
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            print(f"{Fore.GREEN}[+] Token {token} working ! Account: {client.user}")
            await client.close()

        client.run(token)
        return True
    except Exception as e:
        print(f"{Fore.RED}[-] {e} not working ! Token: {token}")
        return False

def remove_processed_tokens(tokens_filename, processed_tokens):
    with open(tokens_filename, 'r') as tokens_file:
        tokens = tokens_file.readlines()

    with open(tokens_filename, 'w') as tokens_file:
        for token in tokens:
            if token.strip() not in processed_tokens:
                tokens_file.write(token)

if __name__ == "__main__":
    tokens_filename = 'token.txt'
    hits_filename = 'hits.txt'
    fails_filename = 'fails.txt'

    processed_tokens = []

    total_tokens = sum(1 for line in open(tokens_filename))
    checked_tokens = 0
    valid_tokens = 0
    invalid_tokens = 0

    ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker by @Dirsearch | Checked = {checked_tokens} | Valid = {valid_tokens}")

    with open(tokens_filename, 'r') as tokens_file, \
         open(hits_filename, 'w') as hits_file, \
         open(fails_filename, 'w') as fails_file:
        for token in tokens_file:
            token = token.strip()
            print(f"Überprüfe Token: {token}")

            checked_tokens += 1
            if check_login(token):
                hits_file.write(token + '\n')
                valid_tokens += 1
            else:
                fails_file.write(token + '\n')
                invalid_tokens += 1
            processed_tokens.append(token)

            ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker by @Dirsearch | Checked = {checked_tokens} | Valid = {valid_tokens}")

    print("Überprüfung abgeschlossen. Ergebnisse wurden in hits.txt und fails.txt geschrieben.")
    remove_processed_tokens(tokens_filename, processed_tokens)

    # Warte auf Tasteneingabe, bevor das Programm beendet wird
    print("Press any key to leave...")
    msvcrt.getch()  # Warte auf Tasteneingabe
