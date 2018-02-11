import os
from datetime import datetime
from flask import Flask, redirect, render_template, request


app = Flask(__name__)


def add_messages(username, message):
    """ Add a message to the list """
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {'timestamp': now, 'from':username, 'message':message}
    with open("data/messages.txt", "a") as chat_list:
        chat_list.writelines("{0} - {1}: {2} \n".format(message_dict['timestamp'], message_dict['from'].title(), message_dict['message']))
    
def get_all_messages():
    """Get all messages and separate them using a br"""
    with open("data/messages.txt", "r") as chat_list:
        messages = chat_list.readlines()
    return messages
    

@app.route("/", methods = ["GET", "POST"])
def index():
    """Main Page with instructions"""
    if request.method == "POST":
        with open("data/users.txt", "a") as users:
            users.writelines(request.form["username"] + "\n")
        return redirect(request.form["username"])
        
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