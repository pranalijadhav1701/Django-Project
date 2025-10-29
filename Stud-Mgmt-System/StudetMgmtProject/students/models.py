from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.PositiveIntegerField(unique=True)
    email = models.EmailField(unique=True, default='default@example.com')
    course = models.CharField(max_length=100, default='Not Assigned')
    marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"



# Admin Panel → http://127.0.0.1:8000/admin/

# Student Portal → http://127.0.0.1:8000/