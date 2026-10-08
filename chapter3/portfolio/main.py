from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,
            template_folder="templates", static_folder='static') # optional

@app.get("/")
def index():
    message = request.args.get("message", "")
    context = {
        "message" : request.args.get("message", ""),
        'fullname' : "Mahdi"
    }
    return render_template('index.html', context=context)


@app.post("/contact")
def contact():
    app.logger.debug(request.form.get["name"]) 
    return redirect(url_for("index"), message = 'ticket successfully send')
    