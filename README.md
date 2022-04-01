# Indian Premier League (Cricket)

## :video_game:Demo Application
:point_right: (https://iplflaskapplication.herokuapp.com/) <br>

## Context
Cricket is a bat-and-ball game played between two teams of eleven players each on a cricket field, at the centre of which is a rectangular 20-metre (22-yard) pitch with a target at each end called the wicket (a set of three wooden stumps upon which two bails sit). Each phase of play is called an innings, during which one team bats, attempting to score as many runs as possible, whilst their opponents bowl and field, attempting to minimise the number of runs scored. When each innings ends, the teams usually swap roles for the next innings (i.e. the team that previously batted will bowl/field, and vice versa). The teams each bat for one or two innings, depending on the type of match. The winning team is the one that scores the most runs, including any extras gained (except when the result is not a win/loss result). Source: https://en.wikipedia.org/wiki/Cricket

## Content
All Indian Premier League Cricket matches between 2008 and 2016.

This is the ball by ball data of all the IPL cricket matches till season 9.

The dataset contains 2 files: deliveries.csv and matches.csv.

matches.csv(It contains 637 Rows) contains details related to the match such as location, contesting teams, umpires, results, etc.

deliveries.csv(It contains 150461 Rows) is the ball-by-ball data of all the IPL matches including data of the batting team, batsman, bowler, non-striker, runs scored, etc.

## Installation

We can start developing our application to display the data. Create a new project folder called 'FlaskApplication' and then cd into the folder via the terminal and execute these commands:

```bash
pyenv local 3.8.9 
python3 -m venv .venv
source .venv/bin/activate 
pip install --upgrade pip [ this is optional]
```

So after getting this done we have to install basic libraries

```bash
pip install Flask
pip install pandas #Pandas and sqlite3 can also be used to transfer between the CSV and SQL formats.
pip install gunicorn
```
## Installed Packages 
| Name|Version |
|--|--|
| click | 8.1.1 |
| Flask | 2.1.1 |
| gunicorn | 20.1.0 |
| importlib-metadata | 4.11.3 |
| itsdangerous | 2.1.2 |
| Jinja2 | 3.1.1 |
| MarkupSafe | 2.1.1 |
| numpy | 1.22.3 |
| pandas | 1.4.1 |
| pip | 22.0.4 |
| python-dateutil | 2.8.2 |
| pytz | 2022.1 |
| setuptools | 49.2.1 |
| six | 1.16.0 |
| Werkzeug | 2.1.0 |
| zipp | 3.7.0 |
