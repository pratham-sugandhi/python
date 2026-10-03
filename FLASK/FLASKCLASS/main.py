from flask import Flask, render_template, url_for, request, jsonify, flash, redirect

# changing the static folder name from static to assets

# app = Flask(__name__)

app = Flask(__name__, static_folder="static", static_url_path="/assets")
app.secret_key = "mysecretkey"

@app.route("/")
def index():
    render_template("index2.html")
    return redirect(url_for("login"))

@app.route("/contact")
def contact():
    flash("Thank you for contacting us! We will get back to you shortly")
    return render_template("contact.html")




# URL => endpoint /
# @app.route("/")
# def hello_world():
#     # static file => dynamically generate the URL for the static file
#     # print(url_for("static", filename="style.css"))

#     query = request.args.get("q", default="Anonymous", type=str)
#     subject = request.args.get("subject", default="AI", type=str)

#     return render_template("index.html", query=query, sub=subject)


@app.route("/about")
def about():
    data = {
        "message": "This is a simple Flask application that demonstrates the use of templates, static files, and query parameters.",
    }
    return jsonify(data, status=200)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # jinja2 template variable
        friends = ["Alice", "Bob", "Charlie", "David"]
        header = "<header>Welcome to the Flask Application</header>"
        
        return render_template("welcome.html", username=username, password=password, friends=friends, header=header)
    else:
        return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True)
    