from flask import Flask, render_template, request, redirect
import summarizer

app = Flask(__name__)
link = []

@app.route('/', methods=['GET', 'POST'])
def load():
    if request.method == "POST":
        link.append(request.form.get('gate'))
        return redirect("/summary")
    return render_template("index.html") # this is blank flask page with empty form and question



@app.route('/summary')
def summary():
    test = summarizer.summarize(link[0], summarizer.model)
    return render_template("results.html", results=test)

if __name__ == '__main__':
    app.run()

