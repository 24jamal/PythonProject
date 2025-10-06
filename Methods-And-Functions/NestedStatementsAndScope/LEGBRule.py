"""
Python looks for a variable in this specific order:

L → E → G → B

👉 Local → Enclosing → Global → Built-in
"""

#Local 

def hello():
    name = "Jamal"

    print(f"Hello {name}")

hello()


#Enclosing

def greeting():

    name = "Dennis"

    def hello_func():

        print(f"Greetings {name}")

    hello_func()

greeting()

#Global

var_name = "Dustin"

def wish():

    print(f"Good Morning {var_name}")

wish()


#Built-in

listsize = ["Jane","Joe","Dennis"]
print(len(listsize))
