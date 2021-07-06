from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Notes(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)


class Attachment(models.Model):
    # for uploading the doc
    file = models.FileField(upload_to='static/uploads')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
