"""
Resources used to write this code:
A Minimal Application n.d., Pallets, accessed 30 May 2026,
<https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application>
"""

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/chapters/<int:chapter_num>")
def show_chapter(chapter_num: int):
    chapters = [
        "It was the best of times, it was the worst of times.",
        "It was the age of wisdom, it was the age of foolishness.",
        "It was the spring of hope, it was the winter of despair."
    ]

    if chapter_num > len(chapters):
        abort(404)

    return render_template(
        "chapter.html",
        chapter_title=f"Chapter {chapter_num}",
        chapter_text=chapters[chapter_num - 1]
    )


@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
