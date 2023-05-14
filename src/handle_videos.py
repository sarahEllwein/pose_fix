import sqlalchemy
from db_conn import conn, engine
from sqlalchemy.orm import Session
import os


def insert_videos(user_id: str, title: str, desc: str, filename: str):
    file_path = "/user_videos/" + filename
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)

    with open(parent_directory + "/squat1.mp4", "rb") as f:
        video_data = f.read()

    with open(parent_directory + file_path, "wb") as f:
        f.write(video_data)

    sql = "INSERT INTO user_videos (user_id, title, description, video_path) VALUES (:p1, :p2, :p3, :p4)"

    with Session(engine) as session, session.begin():
        session.execute(
            sqlalchemy.text(sql),
            {"p1": user_id, "p2": title, "p3": desc, "p4": file_path},
        )


insert_videos("1", "title", "descr", "squat1.mp4")
