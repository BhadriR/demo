
import sqlite3
from flask_mail import Mail, Message
import sqlite3
from flask import*
app= Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'playmusic43103@gmail.com'
app.config['MAIL_PASSWORD'] = 'Playmusic12309'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)
@app.route("/")
def al():
    return render_template("index.html")

@app.route("/send",methods=["POST"])
def aaa():
    if request.method=='POST':
        name=request.form['n1']
        email=request.form['e1']
        msg=request.form['m1']


        c=sqlite3.connect("semail.db")
        cur=c.cursor()
        cur.execute("create table if not exists t1(name text,email text,message text)")
        cur.execute("insert into t1 values(?,?,?)",(name,email,msg))
        c.commit()
        msg1 = Message('Query from music site', sender='playmusic43103@gmail.com', recipients=['playmusic43103@gmail.com'])
        mssg = "message:     " + msg + "              from:      " + email
        msg1.body = mssg
        mail.send(msg1)
    return "success"






if __name__=='__main__':
    app.run(debug=True)