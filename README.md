# ![](https://raw.githubusercontent.com/birthdaysgift/mimic/master/app/common/static/common/img/favicon.png "Mimic") Mimic

[Mimic](http://195.133.1.11:8000/) is a django-based social network, written while practicing python/django backend programming.

I've implemented some of the features that [vk.com](https://vk.com) has:
- Register users
- Edit user's page (add info about user, change his status and avatar)
- Upload and watch some media-content (video and images)
- Create posts on user's page
- Leave comments on images and video, uploaded by user
- Like/dislike some content (posts, images and video)
- Add friends and list them (including common friends)
- Send messages between registered users
- Search for people by the username

## Getting started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Docker ([https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/))
- Docker Compose ([https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/))

Optionally (to run container in VSCode):
- Visual Studio Code ([https://code.visualstudio.com/](https://code.visualstudio.com/))
- Remote-Containers extension for VSCode ([https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers))

### Installation

Clone repository
```bash
git clone https://github.com/birthdaysgift/mimic.git
```
go to project folder
```bash
cd mimic
```
and run
```bash
docker-compose --file docker-compose.dev.yml \
                run --publish=8000:8000 app  \
                python manage.py runserver 0.0.0.0:8000
```
or you can open folder in VSCode as remote folder via Remote-Containers extension ([https://code.visualstudio.com/docs/remote/containers](https://code.visualstudio.com/docs/remote/containers))
