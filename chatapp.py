import os
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

#
banned_words = [
    'sucker'
    'bom'
    'duck'
    ]
messages = []


# @app.route('rooms/add')
# def add_room():
#     roomname = request.form['roomname']
#     rooms[roomname] = []
#     return redirect(....)

@app.route("/")
def get_index():
    return render_template("index.html")
    
@app.route("/login")
def do_login():
    username = request.args['username']
    return redirect(username)

@app.route("/<username>") 
def get_userpage(username):
    newlist=[]
    for message in messages:
        if not message['body'].startswith('@'):
            newlist.append(message)
        elif message['body'].startswith('@' + username):
            newlist.append(message)
        elif message['sender'] == username:
            newlist.append(message)
    return render_template("chat.html", logged_in_as=username, all_the_messages=newlist)
 
@app.route("/<username>/new", methods=["POST"]) 
def add_message(username):
    
    text= request.form['message']
    
    #  newlist=[]


   
   #replace banned words in message using list-python
    words = text.split()
    words = [ "*" * len(word) if word.lower() in banned_words else word for word in words]
    
    text = " ".join(map(str,words))
        
    
    message = {
        'sender': username,
        'body': text
    }
   
    messages.append(message)
    return redirect(username)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))