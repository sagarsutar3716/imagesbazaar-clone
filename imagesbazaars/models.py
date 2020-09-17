from django.db import models


class Categorie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    added_date = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Categorie,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
