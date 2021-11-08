# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 21:42:00 2021

@author: Karen,Mariana,Maricruz y Leonardo
"""

from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def Main():
    return render_template("MainFrame.html")

@app.route("/infografia")
def page_2():
    return render_template("infografia.html")

@app.route("/grafica")
def graph():
    data = [
          ("COVID",1369484),
         ("Dinero y recuersos",381433),
         ("Otros",1508782),
        ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    
    return render_template("graph.html", labels=labels, values=values)

@app.route("/grafica2")
def graphtwo():
    data = [
          ("Inscritos ciclo 2019/2020",33635316),
         ("No inscritos ciclo 2019/2020",20627043),
         ("Concluyeron el año",32896922),
         ("No Concluyeron el año",738394),
        ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    
    return render_template("graph2.html", labels=labels, values=values)

if __name__ == '__main__':
    app.run(debug = True)