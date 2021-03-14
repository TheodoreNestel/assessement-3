from flask import Flask , render_template , request ,redirect
#from forex_python.converter import CurrencyRates 

#flask import errors couldnt solve so ill right the logic pretending it works
#I spent 4 hours trying to resolve these issues they are on the flask side of things not python 
#so I will build the back end as best I can without the logic from that module \
#ill instead to basic calculation in lieu of until either someone who knows more can help me fix it
#or I am given an alternative module / api to use
app = Flask(__name__)
app.config['SECRET_KEY'] ="HarlowIsCute" 
from flask.helpers import flash

print('hello')

#pseudo data bases of valid currencies and the fake converstion function
CURRENCY_DATABASE = ["EUR","USD","GBP","YEN","CNY","CAD"]

def convert(cur1 , cur2 , val):
    """ This isnt a real converstion """
    return val * 2

#error message checking function

def check_cur(cur , cur2):
    if cur not in CURRENCY_DATABASE:
        flash(f"{cur} is not a valid currency")
    

    if cur2 not in CURRENCY_DATABASE:
        flash(f"{cur2} is not a valid currency")
    






@app.route("/")
def home_page():

    
    return render_template("form.html")


@app.route("/conversion")
def conversion():

    input1 = request.args["input1"]
    input2 = request.args["input2"]
    value = int(request.args["value"])

    print(input1,input2,value)

    check_cur(input1.upper(),input2.upper())

    if   input1.upper() not in CURRENCY_DATABASE: 

            
            return redirect("/") 


       
    elif  input2.upper() not in CURRENCY_DATABASE:
            
            return redirect("/")



    else:

            #Here I would put the module logic that converts based on the currencies passed in but since I cant
            #we will do some pretend math 

        converter_value = convert(input1 , input2 ,value)
            

        return render_template("conversion.html",conversion=converter_value,currency=input2)




