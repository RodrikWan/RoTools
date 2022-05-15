# ═║╔╗╚╝╠╣╩╬
#Colorama
from colorama import *
#Others
import os, requests, random, string, base64
#Credits

def Credits():
    os.system('title RoTools 0.1 - Credits')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Made by: RodrikWan                                      {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} Version: 0.1.0                                          {Fore.CYAN}║")
    print(F"{Fore.CYAN}║                                                         ║")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Changelog:                                              {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Main Menu                                       {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Credits                                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Menu                                    {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Nitro Generator                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Token Generator                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Token Info                              {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Token from Email/Password               {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Webhook Spammer                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Webhook Deleter                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Half token from user ID                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord change Hypesquad House                  {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Disable Token                           {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Discord Menu 2 (new page)                       {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    input(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Press [Enter] to return to Main Menu")
    MainMenu()

#Discord Menu

def DiscordMenu():
    os.system('title RoTools 0.1 - Discord Menu')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(f"{Fore.CYAN}║{Fore.WHITE} Discord Menu                                            {Fore.CYAN}║")
    print(f"{Fore.CYAN}║                                                         ║")#-------------------|
    print(f"{Fore.CYAN}║{Fore.WHITE} 1 | Discord Nitro Generator                             {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 2 | Discord Token Generator                             {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 3 | Discord Token Info                                  {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 4 | Discord Token from Email/Password                   {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 5 | Discord Webhook Spammer                             {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 6 | Discord Webhook Deleter                             {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 7 | Discord Half token from user ID                     {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 8 | Discord change Hypesquad House                      {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 9 | Next page                                           {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 0 | Main Menu                                           {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    DiscordMenuChoice = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
    
    if DiscordMenuChoice == 1:
        NitroGenerator()
    elif DiscordMenuChoice == 2:
        TokenGenerator()
    elif DiscordMenuChoice == 3:
        TokenInfo()
    elif DiscordMenuChoice == 4:
        TokenFromEmailPass()
    elif DiscordMenuChoice == 5:
        WebhookSpammer()
    elif DiscordMenuChoice == 6:
        WebhookDeleter()
    elif DiscordMenuChoice == 7:
        HalfToken()
    elif DiscordMenuChoice == 8:
        ChangeHypesquadHouse()
    elif DiscordMenuChoice == 9:
        DiscordMenu2()
    elif DiscordMenuChoice == 0:
        MainMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu2

def DiscordMenu2():
    os.system('title RoTools 0.1 - Discord Menu 2')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(f"{Fore.CYAN}║{Fore.WHITE} Discord Menu 2                                          {Fore.CYAN}║")
    print(f"{Fore.CYAN}║                                                         ║")#-------------------|
    print(f"{Fore.CYAN}║{Fore.WHITE} 1 | Discord Token Disabler                              {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 2 | Discord Token Unverifier                            {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 8 | Previous page                                       {Fore.CYAN}║")
    print(f"{Fore.CYAN}║{Fore.WHITE} 0 | Main Menu                                           {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    DiscordMenuChoice = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
    
    if DiscordMenuChoice == 1:
        DisableToken()
    elif DiscordMenuChoice == 2:
        TokenUnverifier()
    elif DiscordMenuChoice == 8:
        DiscordMenu()
    elif DiscordMenuChoice == 9:
        DiscordMenu2()
    elif DiscordMenuChoice == 0:
        MainMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()


#Discord Menu > Nitro Generator

def NitroGenerator():
    os.system('title RoTools 0.1 - Discord Nitro Generator')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Nitro Generator                                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    try:
        NitroGeneratorAmount = int(input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Amount: '))
        print()
        value = 1
        while value <= NitroGeneratorAmount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Generated {NitroGeneratorAmount} codes")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > Token Generator

def TokenGenerator():
    os.system('title RoTools 0.1 - Discord Token Generator')
    os.system('cls')
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Token Generator                                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    try:
        TokenGeneratorAmount = int(input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Amount: '))
        print()
        value = 1
        while value <= TokenGeneratorAmount:
            code = "Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Generated {TokenGeneratorAmount} tokens")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Token Info

def TokenInfo():
    os.system('title RoTools 0.1 - Discord Token Info')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Token Info                                      {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    TokenInfoToken = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Token: ')

    headers = {'Authorization': TokenInfoToken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        verified = r.json()['verified']
        
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}User: {userName}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}ID: {userID}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}Phone: {phone}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}Email: {email}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}MFA: {mfa}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}Verified: {verified}")
        print(f"{Fore.CYAN}[INFO] {Fore.WHITE}Token: {TokenInfoToken}")
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Info generated")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid Token")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Token from Email/Password

def TokenFromEmailPass():
    os.system('title RoTools 0.1 - Discord Token from Email/Password')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Token from Email/Password                       {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    TokenFromEmail = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Email: ')
    TokenFromPassword = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Password: ')

    data={'email': TokenFromEmail, 'password': TokenFromPassword, 'undelete': "false"}
    headers={'content-type': "application/json", 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    r = requests.post('https://discord.com/api/v8/auth/login', json=data, headers=headers)
    if r.status_code == 200:
        token = r.json()['token']
        print(f'\n{Fore.WHITE}TOKEN: {token}')
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Token generated")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
        os.system('cls; clear')
    elif "PASSWORD_DOES_NOT_MATCH" in r.text:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid password")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    elif "captcha-required" in r.text:
        print(f"\n{Fore.YELLOW}[WARN] {Fore.WHITE}Returned captcha")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid email or password")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > WebHook Spammer

def WebhookSpammer():
    os.system('title RoTools 0.1 - Discord Webhook Spammer')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Webhook Spammer                                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    try:
        WebhookSpammerWebhook = input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Webhook: ")
        WebhookSpammerMessage = input(f"{Fore.CYAN}[INPUT] {Fore.WHITE}Message: ")
        WebhookSpammerAmount = int(input(f"{Fore.CYAN}[INPUT] {Fore.WHITE}Amount: "))
        print()
        for i in range(WebhookSpammerAmount):
            _data = requests.post(WebhookSpammerWebhook, json={'content': WebhookSpammerMessage}, headers={'Content-Type': 'application/json'})
            if _data.status_code < 400:
                print(f'{Fore.GREEN}[SUCCESS] {Fore.WHITE}Sent a message')
        print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Sent {WebhookSpammerAmount} messages')
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Couldn't spam Webhook")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > Webhook Deleter

def WebhookDeleter():
    os.system('title RoTools 0.1 - Discord Webhook Deleter')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Webhook Deleter                                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    try:
        WebhookDeleterWebhook = input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Webhook: ")
        requests.delete(WebhookDeleterWebhook.rstrip())
        print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Webhook deleted')
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Couldn't delete Webhook")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > HalfToken

def HalfToken():
    os.system('title RoTools 0.1 - Discord Half Token from user ID')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Half token from user ID                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    userid = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}UserID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    HalfTokenGen = bas64_bytes.decode('utf-8')
    print(f'\n{Fore.WHITE}Half Token: {HalfTokenGen}')
    print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Half token generated')
    input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
    DiscordMenu()

#Discord Menu > Change Hypesquad House

def ChangeHypesquadHouse():
    os.system('title RoTools 0.1 - Discord change Hypesquad House')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord change Hypesquad House                          {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}                                                         {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 1 | Bravery                                             {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 2 | Brilliance                                          {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 3 | Balance                                             {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    try:
        ChangeHypesquadHouseHouse = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
        ChangeHypesquadHouseToken = input(f'{Fore.CYAN}[INPUT] {Fore.WHITE}Token: ')
        headers = {'Authorization': ChangeHypesquadHouseToken, 'Content-Type': 'application/json'}  
        r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
        if r.status_code == 200:
            headers = {
                'Authorization': ChangeHypesquadHouseToken,
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
            }
        if ChangeHypesquadHouseHouse == "1":
            payload = {'house_id': 1}
        elif ChangeHypesquadHouseHouse == "2":
            payload = {'house_id': 2}
        elif ChangeHypesquadHouseHouse == "3":
            payload = {'house_id': 3}
        r = requests.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
        if r.status_code == 204:
            print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}House changed')
            input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
            DiscordMenu()
    except:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid token")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu 2 > Disable Token

def DisableToken():
    os.system('title RoTools 0.1 - Discord Token Disabler')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Token Disabler                                  {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    disabletokentoken = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Token: ')

    headers = {'Authorization': disabletokentoken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.patch('https://discordapp.com/api/v8/users/@me', headers={'Authorization': disabletokentoken}, json={'date_of_birth': '2015-7-16'})
        if r.status_code == 400:
            print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Token disabled')
            input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
            DiscordMenu2()
        else:
            print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid token")
            input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
            DiscordMenu2()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid token")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
        DiscordMenu2()

#Discord Menu 2 > Token Unverifier

def TokenUnverifier():
    os.system('title RoTools 0.1 - Discord Token Unverifier')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Discord Token Unverifier                                {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    tokenunverifiertoken = input(f'\n{Fore.CYAN}[INPUT] {Fore.WHITE}Token: ')

    headers = {'Authorization': tokenunverifiertoken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        r = requests.post('https://discordapp.com/api/v8/users/@me/relationships', headers={'Authorization': tokenunverifiertoken, 'User-Agent': 'discordbot'}, json={'username': 'LMAO', 'discriminator': 6572})
        if r.status_code == 204:
            print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Token unverified')
            input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
            DiscordMenu2()
        else:
            print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Token unverifier failed")
            input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
            DiscordMenu2()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid token")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu 2")
        DiscordMenu2()

#Windows Menu

def WindowsMenu():
    os.system('title RoTools 0.1 - Windows Menu')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Windows Menu                                            {Fore.CYAN}║")
    print(F"{Fore.CYAN}║                                                         ║")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} 1 | Windows Power Menu                                  {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 0 | Main Menu                                           {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    WindowsMenuChoice = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
    
    if WindowsMenuChoice == 1:
        WindowsPower()
    elif WindowsMenuChoice == 0:
        MainMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Windows Menu')
        WindowsMenu()

#Windows Menu > Windows Power Menu

def WindowsPower():
    os.system('title RoTools 0.1 - Windows Power Menu')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Windows Power Menu                                      {Fore.CYAN}║")
    print(F"{Fore.CYAN}║                                                         ║")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} 1 | Log out                                             {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 2 | Hibernate                                           {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 3 | Shutdown                                            {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 4 | Restart                                             {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 0 | Windows Menu                                        {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    WindowsPowerChoice = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
    
    if WindowsPowerChoice == 1:
        os.system('shutdown /l')
    elif WindowsPowerChoice == 2:
        os.system('shutdown /h')
    elif WindowsPowerChoice == 3:
        os.system("shutdown /s")
    elif WindowsPowerChoice == 4:
        os.system("shutdown /r")
    elif WindowsPowerChoice == 0:
        WindowsMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Windows Power Menu')
        WindowsPower()

#Main Menu

def MainMenu():
    os.system('title RoTools 0.1 - Main Menu')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Main Menu                                               {Fore.CYAN}║")
    print(F"{Fore.CYAN}║                                                         ║")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} 1 | Credits                                             {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 2 | Windows Menu                                        {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 3 | Discord Menu                                        {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 0 | Exit                                                {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    MainMenuChoice = int(input(f"\n{Fore.CYAN}[INPUT] {Fore.WHITE}Option: "))
    
    if MainMenuChoice == 1:
        Credits()
    elif MainMenuChoice == 2:
        WindowsMenu()
    elif MainMenuChoice == 3:
        DiscordMenu()
    elif MainMenuChoice == 0:
        os.system('exit')
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Main Menu')
        MainMenu()

MainMenu()