import json
import string

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.
from forum.textProcessor import textToDict


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE, related_name="profile")
    _blacklist = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


    def getBlacklist(self):
        s = self._blacklist
        if len(s) == 0:
            d = dict()
        else:
            d = json.loads(s)
        return d

    def appendBlacklist(self, text):
        d1 = self.getBlacklist()
        d2 = textToDict(text)

        d1.update(d2)
        self._blacklist = json.dumps(d1)

    def deleteWord(self, word):
        d = self.getBlacklist()
        del d[word]
        self._blacklist = json.dumps(d)
        self.save()

    blacklist = property(getBlacklist)