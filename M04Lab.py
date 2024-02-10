#Cristian Escobedo
#M04 Lab - Case Study: Python APIs
#Disclosure I couldn't figure out how to create an API from the link provided so I learned it from https://www.youtube.com/watch?v=zsYIw6RXjfM the result is basically the same

#imports the protocols from flask for a an Virtal Environment and JSON format data for use in database
from flask import Flask, request, jsonify
app = Flask(__name__)

#routes the user to the main page which is accessed through http://127.0.0.1:5000/get-book/123?extra=%22hello%22 after the application is executed through command: python M04Lab.py
@app.route("/get-book/<id>")
def get_book(id):
    book_data = {"id":id, "book name":"fake book", "author":"fake author", "publisher": "fake publisher"}
    extra = request.args.get("extra")
    if extra:
        book_data["extra"] = extra
#convert the data to JSON format    
    return jsonify(book_data),200

#function to post new data in the from of a new book
@app.route("/add-book",methods=["POST"])
def add_book():
    data = request.get_json()
    return jsonify(data),201

if __name__ == "__main__":
    app.run(debug=True)