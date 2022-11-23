from flask import Flask, render_template, request
import requests, json

app = Flask(__name__)

@app.route("/")
def render_img():
    f = open("key_nasa.txt", "r") # opens key_nasa.txt
    api_key = f.read() # reads the api key
    response = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}") # gets from the url
    # print (response)
    data = response.text # changes into readable json
    # print(data)
    data_dict = json.loads(data) # loads the json into a dictionary
    # print(data_dict)
    return render_template("main.html", title=data_dict["title"], image=data_dict["url"], desc=data_dict["explanation"]) # renders the page

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
