from flask import Flask, render_template, request #import modules


app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    return render_template( 'login.html' )

@app.route("/auth") # /auth is referenced in form action in the html #, methods=['GET', 'POST']) # By default the user can both post and request info but passing the methods parameter specifies which operations can be done
def authenticate():
    name = request.args['name']
    return render_template('response.html', name=name)


if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()
