from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def search_posts_by_user(user_id):
    url = f'https://jsonplaceholder.typicode.com/posts?userId={user_id}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']
        posts = search_posts_by_user(user_id)
        return render_template('index.html', posts=posts, user_id=user_id)

    return render_template('index.html', posts=None, user_id=None)

if __name__ == '__main__':
    app.run(debug=True)
