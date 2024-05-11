from django.db import models

# Create your models here.
class Record(models.Model):
    # it will keep track of created date 
    created_at=models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.PositiveBigIntegerField(null=True)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=40)
    zipcode=models.PositiveIntegerField(null=True)
    
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")