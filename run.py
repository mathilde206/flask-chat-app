import os

from flask import Flask, redirect

app = Flask(__name__)

messages = []

def add_messages(username, message):
    """ Add a message to the list """
    messages.append("{0}: {1}".format(username, message))
    
def get_all_messages():
    """Get all messages and separate them using a br"""
    return "<br>".join(messages)

@app.route("/")
def index():
    """Main Page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"
    
@app.route("/<username>")
def user(username):
    """ Display chat messages """
    messages_string = get_all_messages()
    return "<h1>Welcome {0}</h1><br> {1}".format(username, messages_string)
    
@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect to the user's page """
    add_messages(username, message)
    return redirect(username)



if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)