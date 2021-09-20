from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/left",methods=['POST'])
def left():
    target_weight = int(request.form['target_weight'])
    your_weight = int(request.form['your_weight'])
    left_weight = target_weight - your_weight
    left_weight = str(left_weight).replace("-","")
    return render_template("left_weight.html",left_weight = left_weight)
if __name__ == '__main__':
        app.run(host="0.0.0.0",port="5000",use_reloader=True, debug=True)
#target_weight = int(input("목표 몸무게가 무엇인가요? :"))
#your_weight = int(input("지금 몸무게가 무엇인가요? : "))
#left_weight = target_weight - your_weight
#left_weight = str(left_weight).replace("-","")
#print("남은 몸무게는{left_weight}kg 입니다".format(left_weight=left_weight))
