from email import message
import pandas as pd
import sqlite3 as sql
import secrets
from flask import Flask, request, url_for, redirect, render_template,flash

app = Flask(__name__)

secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "exception", 500

@app.errorhandler(ZeroDivisionError)
def server_error(err):
    app.logger.exception(err)
    return "Cannot divide by 0", 500

@app.route('/')
def hello():
    conn = sql.connect('database.db')
    print("Opened database successfully")

    conn.execute('DROP table IF EXISTS matches')

    conn.execute('DROP table IF EXISTS deliveries')

    conn.execute('CREATE TABLE "matches" ("id" INTEGER,"season" INTEGER,"city" TEXT,"date" TEXT,"team1" TEXT,"team2" TEXT,"toss_winner" TEXT,"toss_decision" TEXT,"result" TEXT,"dl_applied" INTEGER,"winner" TEXT,"win_by_runs" INTEGER,"win_by_wickets" INTEGER,"player_of_match" TEXT,"venue"  TEXT,"umpire1" TEXT,"umpire2" TEXT,"umpire3" TEXT)')

    conn.execute('CREATE TABLE "deliveries" ("match_id" INTEGER,"inning" INTEGER,"batting_team" TEXT,"bowling_team" TEXT,"over" INTEGER,"ball" INTEGER,"batsman" TEXT,"non_striker" TEXT,"bowler" TEXT,"is_super_over" INTEGER,"wide_runs" INTEGER,"bye_runs" INTEGER,"legbye_runs" INTEGER,"noball_runs" INTEGER,"penalty_runs" INTEGER,"batsman_runs" INTEGER,"extra_runs" INTEGER,"total_runs" INTEGER,"player_dismissed" TEXT,"dismissal_kind" TEXT,"fielder" TEXT)')
   
    print("Matches and Deliveries Table created successfully")

    matches = pd.read_csv('dataset/matches.csv')
    matches.to_sql('matches', conn, if_exists='append', index = False)

    deliveries = pd.read_csv('dataset/deliveries.csv')
    deliveries.to_sql('deliveries', conn, if_exists='append', index = False)
    
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/match-list/')
def matchlist():

    conn = sql.connect('database.db')
    
    matchlist = conn.execute('SELECT * FROM matches').fetchall()
    
    conn.commit()

    if matchlist:
        message = "All the matches were listed below"
    else:
        message = "Match list is empty"
    
    return render_template('match-list.html',matchlist=matchlist,message=message)

@app.route("/view-match-data/<int:id>")
def viewmatchdata(id):
    conn = sql.connect('database.db')
    particularmatchdata = conn.execute('SELECT * FROM deliveries WHERE match_id=?',(id,)).fetchall()
    singlematchdata = conn.execute('SELECT * FROM deliveries WHERE match_id=?',(id,)).fetchone()
    conn.commit()
    if particularmatchdata:
        message = "This match related deliveries were listed below"
    else:
        message = "This match related data is blank."
    return render_template('match-data.html',particularmatchdata=particularmatchdata,singlematchdata=singlematchdata,message=message)

@app.route("/remove-match-data/<int:id>")
def removematch(id):
    conn = sql.connect('database.db')
    deletematchdata = conn.execute('DELETE FROM matches WHERE id=?',(id,)) 
    deletedeliveriesdata = conn.execute('DELETE FROM deliveries WHERE match_id=?',(id,)) 
    conn.commit()
    return redirect(url_for('matchlist'))

if __name__ == "__main__":
    app.run()