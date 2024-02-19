
from flask import Flask,render_template,url_for,request,jsonify
import random
import time
import random
import time

app = Flask(__name__)

current_temp = None
temp_history = []
humi_history=[]
mois_history=[]
data_dict = {"Temperature": None, "Temp_history": [],"Humidity":None,"Humi_history": [],"Moisture":None,"mois_history": [],"UV_Level": None,"Air_quality":None,"Co2_level":None,"Rain_level":None }

def generate_random_temp():
    return random.uniform(0,100),random.uniform(0,100),random.uniform(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)
 

@app.route("/")
def hello_world():
    
    return render_template("index.html",data=data_dict)

@app.route("/get_data", methods=["GET", "POST"])
def get_data():
    
    global current_temp, temp_history, data_dict

    current_temp,cur_humi,cur_mois,UV_level,Air_q,Co2_l,Rain_level = generate_random_temp()

    temp_history.append(int(current_temp))
    mois_history.append(int(current_temp))
    humi_history.append(int(current_temp))
    
    if len(temp_history) > 30:
        temp_history = temp_history[-30:]
    data_dict["Temperature"] = int(current_temp)
    data_dict["Temp_history"] = temp_history
    data_dict["Humidity"]=int(cur_humi)
    data_dict["Humi_history"]=humi_history
    data_dict["Moisture"]=int(cur_mois)
    data_dict["mois_history"]=mois_history
    data_dict["UV_Level"]=UV_level
    data_dict["Air_quality"]=Air_q
    data_dict["Co2_level"]=Co2_l
    data_dict["Rain_level"]=Rain_level
    return jsonify(data_dict)
    

    
if __name__ == '__main__':
	app.run(debug=True)
