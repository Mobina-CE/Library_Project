from django.db import models
from accounts.models import CustomUser

class Author(models.Model):
    first_name = models.CharField(max_length=50 , verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last name")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category Name")

    def __str__(self):
     return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")
    publisher = models.CharField(max_length=100, verbose_name="Publisher")
    publish_year = models.IntegerField(verbose_name="Publish Year")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Category")
    is_available = models.BooleanField(default=True, verbose_name="Is Available?")

    def __str__(self):
        return self.title

class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Member")
    loan_date = models.DateField(auto_now_add=True, verbose_name="Loan Date")
    due_date = models.DateField(verbose_name="Dual Date")
    renew_count = models.IntegerField(default=0, verbose_name="Renew Count")
    is_returned = models.BooleanField(default=False, verbose_name="Is Returned?")
    fine_amount = models.IntegerField(default=0, verbose_name="Fine Amount")

    def __str__(self):
        return f"{self.book.title} - {self.member.username}"

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    member = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Member")
    reservation_date = models.DateField(auto_now_add=True, verbose_name="Reservation Date")
    is_active = models.BooleanField(default=True, verbose_name="Is Active?")

    def __str__(self):
        return f"Reservation: {self.book.title} by {self.member.username}"


