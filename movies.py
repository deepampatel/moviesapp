from flask import Flask, redirect, url_for, request,render_template
import json
import urllib.request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('movies.html')



@app.route('/getname',methods = ['POST', 'GET'])
def login():
        keymovie = request.form['name']
        url11 = ('https://api.themoviedb.org/3/search/movie?api_key=f1b1d0f56a3133579b63e4c47799126c&query=' + keymovie)
        url222=url11.replace(" ","%20")
        f = urllib.request.urlopen(url222)
        json_string = f.read()
        obj_json = json.loads(json_string.decode())
        poster_path = (obj_json['results'][0]['poster_path'])
        title = (obj_json['results'][0]['original_title'])
        overview = (obj_json['results'][0]['overview'])
        release_date = (obj_json['results'][0]['release_date'])
        average_vote = (obj_json['results'][0]['vote_average'])
        return render_template('abc.html', title=title, release_Date=release_date, average_vote=average_vote, overview=overview,poster=poster_path)

if __name__ == '__main__':
   app.run(debug = True)

