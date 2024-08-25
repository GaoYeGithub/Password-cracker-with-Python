import hashlib
from urllib.request import urlopen

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile


def hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()


def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password,
                  "\n please change this, it was really easy to guess it (:")
            exit()


url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'

print("Enter your actual passoword and let's guess how easy it is to guess it!\n ex: trying entering 'henry' as a password without the '' ")

while True:
    actual_password = input()
    actual_password_hash = hash(actual_password)
    
    wordlist = readwordlist(url).decode('UTF-8')
    guesspasswordlist = wordlist.split('\n')
    more = input("do you want to add more passwords to the wordlist? (y/n)")
    
bruteforce(guesspasswordlist, actual_password_hash)
    
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: \n\n ps: You can always import a new wordlist and check whether ur password still passes this bruteforce attack")

