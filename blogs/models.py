from django.db import models
from helpers.models import BaseModel
from users.models import User

# Create your models here.

class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)

    # admin페이지에서 어떻게 보여줄지
    def __str__(self):
        return "%s" % (self.title)

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return "%s - %s" % (self.post, self.content)