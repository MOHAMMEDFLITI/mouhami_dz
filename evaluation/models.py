from django.db import models




from django.db import models

class Lawyer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.id

class Evaluation(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(null=True)
    confirmed = models.BooleanField(default=False,null=True)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(null=True)
    comment = models.TextField(null=True)
    

