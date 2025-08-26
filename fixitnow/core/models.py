from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


from django.db import models

class ServiceRequest(models.Model):
    CATEGORY_CHOICES = [
        ("plumbing", "Plumbing"),
        ("gardening", "Gardening"),
        ("electrical", "Electrical"),
        ("cleaning", "Cleaning"),
        ("painting", "Painting"),
        ("other", "Other"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="other")
    status = models.CharField(max_length=50, default="pending")  # for admin use

    def __str__(self):
        return f"{self.title} - {self.category}"


class ServiceUpdate(models.Model):
    servicerequest = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        related_name='updates'
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.servicerequest.title} at {self.created_at}"
class About (models.Model):
    aboutus= models.TextField
