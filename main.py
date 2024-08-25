from flask import Flask, render_template, request
import hashlib
from urllib.request import urlopen
import random
import string

app = Flask(__name__)

def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        return f"Error reading wordlist: {e}"
    return wordlistfile

def hash(password):
    result = hashlib.sha1(password.encode())
    return result.hexdigest()

def generate_password_suggestion():
    """Generate a strong password suggestion."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(16))

def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            suggestions = [generate_password_suggestion() for _ in range(3)]
            return f"Password cracked: {guess_password}", suggestions
    return "Password not found in wordlist", []

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    suggestions = []
    if request.method == 'POST':
        actual_password = request.form['password']
        actual_password_hash = hash(actual_password)

        url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
        wordlist = readwordlist(url).decode('UTF-8')
        guesspasswordlist = wordlist.split('\n')

        result, suggestions = bruteforce(guesspasswordlist, actual_password_hash)

    return render_template('index.html', result=result, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)