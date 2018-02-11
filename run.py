import os
from datetime import datetime
from flask import Flask, redirect, render_template, request


app = Flask(__name__)

def write_to_file(filename, data):
    """Write data to a file"""
    with open(filename, "a") as file:
            file.writelines(data)
        

def add_messages(username, message):
    """ Add a message to the list """
    now = datetime.now().strftime("%H:%M:%S")
    message_dict = {'timestamp': now, 'from':username, 'message':message}
    
    """Write the chat message to messages.txt"""
    write_to_file("data/messages.txt", "{0} - {1}: {2} \n".format(message_dict['timestamp'], message_dict['from'].title(), message_dict['message']))
    
def get_all_messages():
    """Get all messages and separate them using a br"""
    with open("data/messages.txt", "r") as chat_list:
        messages = chat_list.readlines()
    return messages

@app.route("/", methods = ["GET", "POST"])
def index():
    """Gets the user's name and stores it to the user.txt file"""
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n" )
        return redirect(request.form["username"])
        
    return render_template('index.html')
    
@app.route("/<username>", methods=["GET", "POST"])
def user(username):
    # Handle the post request
    if request.method == "POST":
        return redirect(username + "/" + request.form["message"])

    # Handle the get request
    return render_template('username.html', username=username, messages=get_all_messages())
    
@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect to the user's page """
    add_messages(username, message)
    return redirect(username)



if __name__ == "__main__":
    app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)