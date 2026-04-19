import json

import reflex as rx


class Media(rx.Base):
    email: str = ""
    cv: str = ""
    github: str = ""
    likedin: str = ""


class Technology(rx.Base):
    icon: str = ""
    name: str = ""


class Info(rx.Base):
    icon: str = ""
    title: str = ""
    subtitle: str = ""
    description: str = ""
    date: str = ""
    certificate: str = ""
    technologies: list[Technology] = []
    image: str = ""
    url: str = ""
    github: str = ""


class Extra(rx.Base):
    image: str = ""
    title: str = ""
    description: str = ""
    url: str = ""


class Data(rx.Base):
    title: str = ""
    description: str = ""
    image: str = ""
    avatar: str = ""
    name: str = ""
    skill: str = ""
    location: str = ""
    media: Media = Media()
    about: str = ""
    technologies: list[Technology] = []
    experience: list[Info] = []
    projects: list[Info] = []
    training: list[Info] = []
    extras: list[Extra] = []


with open("assets/data/data.json", encoding="utf-8") as file:
    json_data = json.load(file)

data = Data(**json_data)
