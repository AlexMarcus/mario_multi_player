#(201) 371-4413

from flask import Flask, request
import threading
import atexit
from twilio.twiml.messaging_response import MessagingResponse

POOL_TIME = 10 #seconds

data = []
dataLock = threading.Lock()
backgroundThread = threading.Thread()

def createApp():
    app = Flask(__name__)

    def interrupt():
        global backgroundThread
        backgroundThread.cancel()
    
    def doStuff():
        global data
        global backgroundThread
        with dataLock:
        # Do your stuff with data here
            data.append("1")
            print(data)
            
        # Set the next thread to happen
        backgroundThread = threading.Timer(POOL_TIME, doStuff, ())
        backgroundThread.start()   

    def doStuffStart():
        # Do initialization stuff here
        global backgroundThread
        # Create your thread
        backgroundThread = threading.Timer(POOL_TIME, doStuff, ())
        backgroundThread.start()

        
    doStuffStart()
    atexit.register(interrupt)
    return app

app = createApp()
        
@app.route('/sms', methods=['POST', 'GET'])
def sms():
    
    sender = request.form['From']
    message = request.form['Body']

    print(sender + " :::  " +message)

    message = message.lower()

    response = 'Mario will obey'
    error = 'Invalid command (right, left, jump, b)'
    
    approvedCommands = {"right", "left", "jump", "b"}


    
    if(message in approvedCommands):
        f= open("request.txt","w+")
        f.write(message)
    else:
        response = error
        
    resp = MessagingResponse()
    resp.message(response)

    return str(resp)

@app.route("/")
def main():

    return "hello world"

if __name__ == '__main__':
    app.run(debug=False)
