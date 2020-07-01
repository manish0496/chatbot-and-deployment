from flask import Flask,render_template,request
from nltk.chat.util import reflections,Chat 
import re


pairs = [
    [r"hi|hey|hello|hiiiiiiiiiii",["hello","hi"]],
    [r"what are the courses available|what are the course available|looking for course?",["which course you are looking for we have online as well offline courses."]],

    [r"online course|online|online courses|what are the online courses?|what are the online course?",["""we have following online courses available:  
    1. machine learning  
    2. deep learning 
    3.complete datascience course."""]],
    [r"offline course|offline|offline courses|what are the offline courses?",["we have following online courses available:  1. machine learning  2. deep learning 3.complete datascience course. "]],
    [r"machine learning|1|1.|machinelearning|machine|machinelearning course ?",["""we have following batch <br> 
        1.online classes <br>
        2. offline batch <br>
       "do you want to know about offline timing,please type: time"""]],
    [r"deep learning|2.|2|deeplearning|deep|deeplearning course ?",["""deep learning we have following batch timing <br>
       1.online classes <br>
        2. offline batch <br>
       "do you want to know about timing,please type: time """]],
    [r"data science|3.|3|complete datascience course|datascience ?",["""datascience we have following batch timing <br>
        1.online classes <br>
        2. offline batch <br>
       "do you want to know about timing,please type: time """]],
    [r"time|timing|batch time|batch timing ?",[""" we have following batch timing <br>
       1.morning (7:00-9:00 AM IST)\n <br>
       2. Evening batch (6:00-8:00 PM IST)\n <br>
       do you want to know about fee please type: fee """]],
    [r"course fee|what is the course fee|how much do we have to pay|how much fee?|fee",["""course </b>fee</b>: <br>
       1.machine learning the fee is 25k+GST <br>
       2.deep learning the fee is 20+GST\n <br>
       3. complete datascience the fee is 49k+GST\n.<br>
       do you want to know about validity please type: validity"""]],
    [r"machine learning fee?|machinelearning fee|fee for machine learning?",["machine learning the fee is 25k+GST "]],
    [r"deep learning fee?|deeplearning fee|fee for deep learning?",["machine learning the fee is 25k+GST "]],
    [r"datascience fee?|complete datascience fee|fee for datascience?",["datascience the fee is 25k+GST "]],
    #[r"coupon|coupon code?",["we have offer going on 50 % discount please use CHATBOT50 coupon code.if you want to know about validity tyoe validity"]],
    [r"what is the course availability?|validity|validityperiod|validy period?",["course availability is 1 year<br> do you want to know about more offer please type: coupon"]],
    [r"offer?|discount|coupon?",["please use CHATBOT50 coupon code to get discount<br> if you have more query and want to talk to customer care please call to this number 0102232345<br> thanks for connecting "]],










    [
        r"How are you ?",
        ["I am fine...thankyou\n What about you??"]
    ],
    [
        r"I am good",
        ["nice to hear"]
    ],
    [
        r"(.*) age?",
       [ "I am computer program.....dont you know that"]
    ],
    [
        r"(.*) location|city ?",
        ["Jaipur","Gwalior"]
    ],
    [
        r"how is weather in (.*)",
        ["Weather is awesome in %1.....you will love it"]
    ],
    [
        r"(.*) bye| bye (.*)|quit|bye",
        ["Okay bye it wasn't nice talking to you","bye bye take care"]
    ],
    [
        r"who created you?.*",
        ["A very sensible woman :)"]
    ],
    [
        r"w.* are you?",
        ['None of your business..']
    ],
    [
        r"I am (.*)",
        ['You are welcome %1']
    ],
    [
        r"(.*)",
        ["sorry i can't understand please for more info call to our customer support"]
    ]
]

chat = Chat(pairs,reflections)
#chat.converse()


app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/get")
def home():
    msg = request.args.get("msg")
    print(msg)
        #for var in pairs:
            #if re.search(var[0],msg):
                #return str(var[1])
    return chat.respond(msg)
            


app.run(port=80,debug=True)