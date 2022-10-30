# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import Avg


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


class AverageRating(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='BookID')
    rating = models.IntegerField()


class Bookratings(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    rating = models.SmallIntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(1)])
    ratingtimestamp = models.TextField(
        db_column='ratingTimeStamp')  # Field name made lowercase. This field type is a guess.
    comment = models.TextField()
    commenttimestamp = models.TextField(
        db_column='commentTimeStamp')  # Field name made lowercase. This field type is a guess.

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
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchasedBooks'


class Shoppingcarts(models.Model):
    ordernumber = models.AutoField(db_column='orderNumber', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey('Books', models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.

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
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookID')  # Field name made lowercase.
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'WishLists'
        constraints = [
            models.UniqueConstraint(fields=['bookid', 'userid', 'name'], name='constraint_userId_bookId_name')]


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
