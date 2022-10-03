# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Addresses(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    type = models.TextField(db_column='Type')  # Field name made lowercase.
    address = models.TextField(db_column='Address')  # Field name made lowercase.
    country = models.TextField(db_column='Country')  # Field name made lowercase.
    state = models.TextField(db_column='State')  # Field name made lowercase.
    city = models.TextField(db_column='City')  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='ZipCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Addresses'


class Authors(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='firstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName')  # Field name made lowercase.
    biography = models.TextField()
    publisher = models.TextField()

    class Meta:
        managed = False
        db_table = 'Authors'


class Bookratings(models.Model):
    userID = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    bookID = models.ForeignKey('Books', models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    rating = models.IntegerField()
    ratingtimestamp = models.TextField(db_column='ratingTimeStamp')  # Field name made lowercase. This field type is a guess.
    comment = models.TextField()
    commenttimestamp = models.TextField(db_column='commentTimeStamp')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'BookRatings'


class Books(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    isbn = models.TextField(db_column='ISBN', unique=True)  # Field name made lowercase.
    authorid = models.ForeignKey(Authors, models.DO_NOTHING, db_column='AuthorID')  # Field name made lowercase.
    genreid = models.ForeignKey('Genres', models.DO_NOTHING, db_column='GenreID')  # Field name made lowercase.
    name = models.TextField()
    description = models.TextField()
    price = models.TextField()  # This field type is a guess.
    publisher = models.TextField()
    yearpublished = models.IntegerField(db_column='yearPublished')  # Field name made lowercase.
    copiessold = models.IntegerField(db_column='copiesSold')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Books'


class Creditcards(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    type = models.TextField(db_column='Type')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    expirationdate = models.TextField(db_column='ExpirationDate')  # Field name made lowercase.
    cvv = models.IntegerField(db_column='CVV')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreditCards'


class Genres(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    genre = models.TextField()

    class Meta:
        managed = False
        db_table = 'Genres'


class Purchasedbooks(models.Model):
    orderhistory = models.AutoField(db_column='orderHistory', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasedBooks'


class Shoppingcarts(models.Model):
    ordernumber = models.AutoField(db_column='orderNumber', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ShoppingCarts'


class Users(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.TextField(db_column='userName', unique=True)  # Field name made lowercase.
    password = models.TextField()
    firstname = models.TextField(db_column='firstName', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='lastName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Wishlists(models.Model):
    UserID = models.OneToOneField(Users, models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    BookID = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    name = models.TextField(unique=True)

    class Meta:
        managed = False
        db_table = 'WishLists'
