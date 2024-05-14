#nombre
#autor
#descripcion
#precio
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/books",methods=["GET"])
def get_books():
    return None

@app.route("/books/{id}",methods=["GET"])
def get_book_by_id():
    print(request.args)
    return None

@app.route("/authors",methods=['GET'])
def get_authors():
    return None

@app.route("/authors/{id}",methods=['GET'])
def get_author_by_id():
    return request.args
    return None

