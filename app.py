from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://alphaville.github.io/optimization-engine/img/docker.gif",
    "https://cdn.dribbble.com/users/1008970/screenshots/6140230/blog_post_docker.gif",
    "https://miro.medium.com/max/1000/1*E8IgOSkMTpBRs0w0-Zsx2g.gif",
    "https://i.pinimg.com/originals/f5/5e/80/f55e8059ea945abfd6804b887dd4a0af.gif"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")