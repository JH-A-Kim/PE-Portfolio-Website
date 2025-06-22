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
            "position": "Production Engineer Fellow",
            "organization": "Meta x MLH",
            "duration": "June 2025 - Present",
            "description": "Participating in a fellowship program with Meta and Major League Hacking, focusing on production engineering and software development."
        },
        {
            "position": "Associate Vice President Equity and Sustainability",
            "organization": "Simon Fraser Student Society",
            "duration": "June 2024 - May 2025",
            "description": "Overseeing equity and sustainability initiatives within the Simon Fraser Student Society."
        },
        {
            "position": "Vice President of Finance",
            "organization": "Society of Arts and Social Sciences",
            "duration": "October 2024 - April 2025",
            "description": "Managing financial operations and budgeting for the Society of Arts and Social Sciences."
        }
    ]

    education = [
        {
            "degree": "Bachelors of Applied Science in Computing Science",
            "institution": "Simon Fraser University",
            "year": "2027",
        },
        {
            "degree": "Associates of Arts in Arts and Social Sciences",
            "institution": "Coquitlam College",
            "year": "2023",
        }
    ]

    hobbies=[
        {
            "hobby": "Video Games",
            "description": "Enjoy playing a variety of video games specifically League and TFT.",
            "image": "./static/img/T1Art.jpeg"
        },
        {
            "hobby": "Organzing Hackathons",
            "description": "Passionate about organizing hackathons and tech events to foster innovation and collaboration.",
            "image": "./static/img/StormHacks.jpg"
        },
        {
            "hobby": "Watching Esports",
            "description": "Avid fan of esports, particularly League of Legends (Huge fan of T1 and Faker).",
            "image": "./static/img/EsportsWatching.PNG"
        }
    ]

    return render_template('more.html',
                            title="More about Jung-Hyun Andrew Kim",
                            experience=experience,
                            education=education,
                            hobbies=hobbies,
                            url=os.getenv("URL")
                            )