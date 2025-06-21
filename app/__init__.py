import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Jung-Hyun Andrew Kim", url=os.getenv("URL"))

@app.route('/more')
def more():
    experience = [
        {
            "position": "Director of External Relations",
            "organization": "SFU Surge",
            "duration": "September 2024 - Present",
            "description": "Leading external relations efforts for SFU Surge, focusing on partnerships and community engagement."
        },
        {
            "position": "PlaceHolder1",
            "organization": "PlaceHolder1",
            "duration": "PlaceHolder1",
            "description": "PlaceHolder1"
        }
    ]

    education = [
        {
            "degree": "placeholder2",
            "institution": "placeholder2",
            "year": "placeholder2",
        },
    ]

    hobbies=[
        {
            "hobby": "Video Games",
            "description": "Enjoy playing a variety of video games specifically League and TFT.",
            "image": "static/images/logo.jpg"
        },
        {
            "hobby": "placeholder3",
            "description": "placeholder3",
            "image": "static/images/logo.jpg"
        }
    ]

    return render_template('more.html',
                            title="More about Jung-Hyun Andrew Kim",
                            experience=experience,
                            education=education,
                            hobbies=hobbies,
                            url=os.getenv("URL")
                            )