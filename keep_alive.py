from flask import Flask, render_template, redirect
from threading import Thread
import sockets

app = Flask('')

@app.route('/')
def home():
  return render_template("index.html")


@app.route("/contactme")
def contactme():
    return render_template("contactme.html")

@app.route("/babaganoush")
def babaganoush():
    return render_template("babaganoush.html")



@app.route("/about")
def about():
    return render_template("about.html")

  
if __name__ == "__main__":
    app.run(debug=True)



def run():
  app.run(host ='0.0.0.0', port = 8080)









def keep_alive():
  t = Thread(target = run)
  t.start()