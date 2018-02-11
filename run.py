import os
from datetime import datetime
from flask import Flask, redirect, render_template


app = Flask(__name__)

messages = []

def add_messages(username, message):
    """ Add a message to the list """
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {'timestamp': now, 'from':username, 'message':message}
    messages.append(message_dict)
    
def get_all_messages():
    """Get all messages and separate them using a br"""
    return messages

@app.route("/")
def index():
    """Main Page with instructions"""
    return render_template('index.html')
    
@app.route("/<username>")
def user(username):
    """ Display chat messages """
    messages_string = get_all_messages()
    return render_template('username.html', username=username, messages=messages_string)
    
@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect to the user's page """
    add_messages(username, message)
    return redirect(username)



if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)