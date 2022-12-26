from flask import Flask, render_template,request,redirect

app = Flask(__name__)

dic=[]
@app.route("/create_user",methods=["POST","GET"])
def create_user():
    name=request.form.get("name")
    mobile=request.form.get("mobile")
    about=request.form.get("about")
    temp={"name":name,"mobile":mobile,"about":about}
    dic.append(temp)
    return render_template("create_user.html",data=dic)

if __name__=="__main__":
    app.run(debug=True)