from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=10)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish_date = models.DateField(null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):

        return f"{self.id}- {self.title}"



class comment(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    Text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.Text