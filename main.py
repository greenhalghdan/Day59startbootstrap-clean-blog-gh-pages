from flask import Flask, render_template, request
import requests
import smtplib
import os
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


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form

        with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
            connection.starttls()
            print(os.environ.get("emailusername"))
            print(os.environ.get("emailpassword"))
            connection.login(user=os.environ.get("username"), password=os.environ.get("password"))
            connection.sendmail(from_addr="smtp@suffolkmotorcyclespares.co.uk",
                                to_addrs="danielgreenhalgh@suffolkmotorcyclespares.co.uk",
                                msg=f"subject:New Message\n\nname: {data['name']}\nemail: {data['email']}\nPhone: "
                                    f"{data['phone']}\nMessage: {data['message']}")
        return render_template('contact.html', status="Message sent")

    return render_template('contact.html', status="Contact Me")

@app.route('/form-entry', methods=["POST"])
def receive_data():
    data = request.form
    print(type(data))
    print(data["name"])
    print(data["email"])
    print(data["phone"])
    print(data["message"])
    return "<h1>Successfully sent your message</h1>"

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