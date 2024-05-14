#nombre
#autor
#descripcion
#precio

import sys
from flask import Flask,jsonify,request

app = Flask(__name__)
app.debug = True

@app.route("/books",methods=["GET"])
def get_books():
    print("in getbooks",file=sys.stdout)
    return None

@app.route("/books/{id}",methods=["GET"])
def get_book_by_id():
    print("in get book by id",file=sys.stdout)
    print(request.args)
    return None

@app.route("/authors",methods=['GET'])
def get_authors():
    print("in get authors ",file=sys.stdout)
    print(request.get_json,file=sys.stdout)
    return None

@app.route("/authors/{id}",methods=['GET'])
def get_author_by_id():
    print("In get authors by id",file=sys.stdout)
    print(request.get_json())
    print(request.args,file=sys.stdout)
    #return request.args
    return None

if __name__ == '__main__': 
    app.run(debug=True, port=5000)

