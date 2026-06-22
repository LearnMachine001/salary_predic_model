from flask import Flask,render_template,redirect,request,session,flash
import webbrowser
import sqlite3
import numpy as np
import joblib

app = Flask(__name__)
app.secret_key = "salary_predict_key"

model = joblib.load("salary_model.pkl")


@app.route('/')
def home():
    username = session.get("user")

    return render_template("home.html",username = username)

@app.route("/signup",methods =["GET","POST"])
def signup():
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]


        conn = sqlite3.connect("salary_predict.db")
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO users(name,email,password) VALUES (?,?,?)

''',(name,email,password))
        
        conn.commit()
        conn.close()
        flash("Sign Up successfull,Please login !")
        return redirect("/login")

    return render_template("signup.html")

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        session.permanent = True

        conn = sqlite3.connect("salary_predict.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM users
            WHERE email=? AND password=?
    ''',(email,password)
    )
        
        user = cursor.fetchone()

        conn.close()

        if user:
            session["user"] = user[1]
            flash("Login Successfull !")
            return redirect("/home")
        else:
            return "invalid email or password"

    return render_template("login.html")
    
@app.route("/predict",methods = ["GET","POST"])
def predict():

    if "user" not in session:
        return redirect("/login")
    
    prediction = None

    if request.method == "POST":

        experience = float(request.form["experience"])
        input_data = np.array([[experience]])
        result = model.predict(input_data)

        prediction = round(result[0],2)

        conn = sqlite3.connect("salary_predict.db")
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO prediction
            (username,experience,predicted_salary)
                VALUES(?,?,?)
            ''',(session["user"],
                experience,
                prediction))
        
        conn.commit()
        conn.close()

    return render_template("predict.html",prediction = prediction)


@app.route("/about")
def about():
    flash("You can visit about page without login ")
    return render_template("about.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")
    
    conn = sqlite3.connect("salary_predict.db")
    cursor = conn.cursor()

    cursor.execute('''
        SELECT experience,predicted_salary
        FROM prediction
        WHERE username=?
        ORDER BY id DESC
''',(session["user"],))
    
    history = cursor.fetchall()

    conn.close()
    
    return render_template("dashboard.html",username = session["user"],history = history)

@app.route("/logout")
def logout():
    session.pop("user",None)
    flash("Logout successfully !")

    return render_template("home.html")


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug = True)