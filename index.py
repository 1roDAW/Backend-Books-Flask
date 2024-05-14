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
    if len(request.args) == 0:
        print("NO args",file=sys.stdout)
    else:
        print(request.args['id'],file=sys.stdout)
    return jsonify({"result":200})

@app.route("/books/<int:Id>",methods=["GET"])
def get_book_by_id(Id):
   print("in get book by id",file=sys.stdout)
   print(Id,file=sys.stdout)
   return jsonify({"result":200,"Id":Id})

@app.route("/authors",methods=['GET'])
def get_authors():
    print("in get authors ",file=sys.stdout)
    print(request.get_json,file=sys.stdout)
    return jsonify({"result":200})

@app.route("/authors/<int:Id>",methods=['GET'])
def get_author_by_id(Id):
    print("In get authors by id",file=sys.stdout)
    print(Id,file=sys.stdout)
    return jsonify({"result":200,"Id":Id})

if __name__ == '__main__': 
    app.run(debug=True, port=5000)

