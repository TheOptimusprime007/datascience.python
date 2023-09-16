from flask import Flask
#ans1
#API stands for Application Programming Interface. It is a set of rules and protocols that allows different software
#  applications to communicate with each other. APIs define the methods 
# and data formats that applications can use to request and exchange information or functionality.

#api are used everywhere where we need to connect with different lanuage and we have a connection between them 
#like banks and #3rd party upi apps

#ans2
#Advantages of api:
#can work with different language applications 
#processing speed is good.
#can be resued
#efficient

#disadvantages
#high in cost.
#security risks
#latency issues

#ans3
#web api:it is an application programming interface for either a web server or a web brower. As
# a web development concept, it can be related to a web applications client side.
#web api uses only HTTP protocol which is used in every web search.
# other api can use TCP,SMTP,HTTP

#ans4
#Rest and soap are 2 different kinds of architecture
#rest api:
# it uses http protocol 
# it uses functions like PUT,GET,POST,DELETE
# It is simple to make can be easily scalabal and is flexiable with the working.

#soap api:
#uses tcp/smtp protocol
# it uses xml
# It uses wsdl (web server description language)
# it is more secure than rest 



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/add")
def number():
    a=10
    b=20
    c = a + b
    return f"The sum of {a} and {b} is {c}"

if __name__=="__main__":
    app.run(host="0.0.0.0")
