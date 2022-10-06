'''
ZEMZEM is AWZOME Ziying Jian, Maya Nelson, Elizabeth Paperno
SoftDev
K07 -- Flask
2022-10-03
time spent:
'''

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* Flask builds on similar object-oriented programming fundamentals as Java and Python
* Name the file with the same name as the Flask variable
QCC:
0.Similar to initializing an instance of a class, learned in Java. Also similar to other __init__ keywords we see in Java.
1.Based on using terminal commands in class, we have used this backslash when
constructing file paths. This is likely the root directory.
2. It will print in the terminal.
3.It will print __main__ to terminal when you run the code.
4.The print statement will appear on the web server when we call app.run() as this is where the app is routed to.
5.Similar to the way you would call any method of a class in Java (such as main()). Also similar to the run() method in ReactJS.
...
INVESTIGATIVE APPROACH:
<We first read through the code and attempted to try
to predict its behavior, using prior knowlege from
other languages. Then we ran the code in terminal 
which gave us a link to a web server, which we opened.
The website displayed the text "No hablo queso!". We also
noted that when opened the page output is printed to
terminal (including the timestamp, etc.).>
'''
