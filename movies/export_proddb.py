# import modules

import pandas as pd
import sqlite3
import requests
import json
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


def export_prod():
    with app.app_context():
        headers = {
            'Authorization': 'ujbOsdlknfsodiflksdonosB4aA=',
            'Accept': 'application/json'
        }
        r = requests.get(
            'https://railwayapps-production.up.railway.app/api/movies/',
            headers=headers
        )

        conn = sqlite3.connect('db.sqlite3')

        # with connect("db.sqlite3") as db:
        curs = conn.cursor()

        data = json.loads(r.text)

        # print(data)

        json_str = json.dumps(data, indent=4)

        # data = json.load(open('json_file.json'))

        df = pd.DataFrame(data["objects"])

        insert_statement = 'INSERT INTO movies_movie_prod (title, release_year, number_in_stock, daily_rate, genre_id, date_created) VALUES (:title,:release_year,:number_in_stock,:daily_rate,:genre_id,:date_created)'

        print(df)

        df = df.drop('resource_uri', axis=1)

        df.to_sql('movies_movie_prod', conn, if_exists='replace', index=False)

        # URL = 'https://railwayapps-production.up.railway.app/api/movies/'
        # df = pd.read_json(URL)
        print("Export reached!")

        # return redirect(url_for('export_complete.html'))
