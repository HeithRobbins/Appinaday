from flask import Flask, request, render_template
import dict


app = Flask(__name__)

@app.route("/")
def home():
    #will render the html
    pass

@app.route("/", methods=["POST"])
def return_info(string):
    #look at what gets returned
    #pars it into a useable set of indexes
    console.log("good")


if __name__ == "__main__":
    app.run(debug=True)
