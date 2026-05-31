"""
Resources used to write this code:
A Minimal Application n.d., Pallets, accessed 30 May 2026,
<https://flask.palletsprojects.com/en/stable/quickstart/#a-minimal-application>
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

chapters = [
    {"title": "Chapter 1", "content": "It was the best of times, it was the worst of times."},
    {"title": "Chapter 2", "content": "It was the age of wisdom, it was the age of foolishness."},
    {"title": "Chapter 3", "content": "It was the spring of hope, it was the winter of despair."}
]



@app.route("/chapters/<int:chapter_num>")
def show_chapter(chapter_num: int):
    if chapter_num > len(chapters):
        abort(404)

    chosen_chapter = chapters[chapter_num - 1]
    chapter_title = chosen_chapter["title"]
    chapter_text = chosen_chapter["content"]

    return render_template(
        "chapter.html",
        chapter_title=chapter_title,
        chapter_text=chapter_text
    )


@app.route("/")
def home_page():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
