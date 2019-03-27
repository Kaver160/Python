from app import app
from flask import render_template
from movies import MoviesList
from curses import curses
from pogoda import weather

import requests

import lxml
from lxml import html

@app.route('/')
def index():
	return render_template('index.html', movies = MoviesList().create_movies_list())
	pass

@app.route('/pogoda')
def pogoda():
	return render_template('pogoda.html', pogoda = weather())
	pass

@app.route('/curs')
def curs():
	return render_template('curs.html', curs = curses())
	pass

@app.route('/movies')
def movies():
	return render_template('movies.html', movies = MoviesList().create_movies_list())
	pass
@app.route('/zadanie')
def zadanie():
	return render_template('zadanie.html')
