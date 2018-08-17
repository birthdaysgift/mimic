from django.contrib.auth import models as auth_models
from django.db import models


class User(auth_models.User):
    avatar = models.URLField(default="https://i2.bongacams.com/00d/0e8/134/60307272da340d6aeccaf109399d57a2_thumb_big.jpg")