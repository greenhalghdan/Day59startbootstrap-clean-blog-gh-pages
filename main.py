from flask import Flask, render_template
import requests

response = requests.get(url="https://api.npoint.io/8347437be697b0341b03")

posts = response.json()
print(posts)

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello_world():
    return render_template("index.html", all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    return render_template('post.html', all_posts=posts, post_id=post_id)
# @app.route('/<int:guess>')
# def show_post(guess):
#     # show the post with the given id, the id is an integer
#     if guess == randnumber:
#         return "<h1>Correct</h1>" \
#                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
#     elif guess > randnumber:
#         return "<h1>To High</h1>" \
#                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
#     else:
#         return "<h1>To Low</h1>" \
#                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)