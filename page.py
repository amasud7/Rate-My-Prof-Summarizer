from flask import Flask, render_template
import summarizer

app = Flask(__name__)

test = summarizer.summarize(summarizer.reviews, summarizer.model)
@app.route('/')
def load():
    return render_template("index.html", test=test)


app.run()