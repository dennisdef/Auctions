from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=20)     

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['category']

    def __str__(self):
        return self.category



class Listing(models.Model):
    user = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE, null= True)
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name="kind", on_delete=models.CASCADE, null= True)
    listing = models.TextField(null=True)
    image = models.FileField(default='default.png')
    date = models.DateTimeField(null=True)     
    active = models.BooleanField(default=True)
    watchlist = models.ManyToManyField(User, related_name="in_watchlist",blank=True)
    price = models.FloatField(
        default = 0,
        validators=[
            MinValueValidator(0)
        ]
    ) 

    class Meta:
        verbose_name = "Listing"
        verbose_name_plural = "Listings"
        ordering = ['-date']

    def __str__(self):
        return self.title 


class Comment(models.Model):
    post = models.ForeignKey(Listing,on_delete=models.CASCADE,related_name='comments',null=True)
    name = models.ForeignKey(User, related_name="user_name", on_delete=models.CASCADE, null= True)
    comment = models.TextField(null=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)


class Bid(models.Model):
    post = models.ForeignKey(Listing,on_delete=models.CASCADE,null=True,related_name="bids")
    name = models.ForeignKey(User, related_name="bidder", on_delete=models.CASCADE, null= True)
    price = models.FloatField(
        default = 0,
        validators=[
            MinValueValidator(0)
        ]
    )  

    def __str__(self):
        return 'Latest Bid: {}'.format(self.price)
