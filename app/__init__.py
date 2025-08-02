import datetime
import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()

app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase("file:memory?mode=memory&cache=shared", uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

experience = [
    {
        "position": "Director of External Relations",
        "organization": "SFU Surge",
        "duration": "September 2024 - Present",
        "description": "Leading external relations efforts for SFU Surge, focusing on partnerships and community engagement. Acquiring sponsorships with AMD, Scalar, Vercel, Defang and more.",
    },
    {
        "position": "Production Engineer Fellow",
        "organization": "Meta x MLH",
        "duration": "June 2025 - Present",
        "description": "Participating in a fellowship program with Meta and Major League Hacking, focusing on production engineering and software development. Stay tuned for what I do!",
    },
    {
        "position": "Associate Vice President Equity and Sustainability",
        "organization": "Simon Fraser Student Society",
        "duration": "June 2024 - May 2025",
        "description": "Overseeing equity and sustainability initiatives within the Simon Fraser Student Society. Bringing new scholarship opportunities for students with accessibility needs.",
    },
    {
        "position": "Vice President of Finance",
        "organization": "Society of Arts and Social Sciences",
        "duration": "October 2024 - April 2025",
        "description": "Managing financial operations and budgeting for the Society of Arts and Social Sciences.",
    },
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
    },
]

hobbies = [
    {
        "name": "Video Games",
        "description": "I really enjoy playing a variety of video games specifically League and TFT. (It has consumed my life :D)",
        "image": "./static/img/T1Art.jpeg",
    },
    {
        "name": "Organzing Hackathons",
        "description": "I am passionate about organizing hackathons and tech events to foster innovation and collaboration. StormHacks is an MLH partner and everyone should apply for it!",
        "image": "./static/img/StormHacks.jpg",
    },
    {
        "name": "Watching Esports",
        "description": "I am a avid fan of esports, particularly League of Legends (Huge fan of T1 and Faker). Although my sleep schedule is ruined by watching the LCK at 3 am every night.",
        "image": "./static/img/EsportsWatching.PNG",
    },
]

routes = [
    {
        "name": "Home",
        "url": "/",
    },
    {
        "name": "Hobbies",
        "url": "/hobbies",
    },
    {
        "name": "Timeline",
        "url": "/timeline",
    },
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Jung-Hyun Andrew Kim",
        experience=experience,
        education=education,
        routes=routes,
        url=os.getenv("URL"),
    )


@app.route("/hobbies")
def hobbiesPage():
    return render_template(
        "hobbies.html",
        title="Jung-Hyun Andrew Kim",
        hobbies=hobbies,
        routes=routes,
        url=os.getenv("URL"),
    )


@app.route("/timeline")
def timeline():
    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template(
        "timeline.html",
        title="Timeline",
        timeline_posts=timeline_posts,
        routes=routes,
        url=os.getenv("URL"),
    )


@app.route("/api/timeline_post", methods=["POST"])
def post_time_line_post():
    name = request.form.get("name")
    if not name:
        return {"status": "error", "message": "Invalid name"}, 400

    email = request.form.get("email")
    if not email or "@" not in email:
        return {"status": "error", "message": "Invalid email"}, 400

    content = request.form.get("content")
    if not content:
        return {"status": "error", "message": "Invalid content"}, 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_time_line_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route("/api/timeline_post/<int:id>", methods=["DELETE"])
def delete_time_line_post(id):
    try:
        timeline_post = TimelinePost.get(TimelinePost.id == id)
        timeline_post.delete_instance()
        return {"status": "success", "message": "Post deleted successfully"}
    except TimelinePost.DoesNotExist:
        return {"status": "error", "message": "Post not found"}, 404

@app.route("/api/timeline_post/all", methods=["DELETE"])
def delete_all_time_line_posts():
    try:
        TimelinePost.delete().execute()
        return {"status": "success", "message": "All posts deleted successfully"}
    except Exception as e:
        return {"status": "error", "message": f"Failed to delete posts: {str(e)}"}, 500
