from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(unique=True, max_length=255)
    icon = models.CharField(max_length=255)
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'

    def __str__(self):
        return self.name


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_one_id = models.PositiveIntegerField()
    team_two_id = models.PositiveIntegerField()
    league_id = models.PositiveIntegerField()
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    start_time = models.DateTimeField()
    bet_start_time = models.DateTimeField(blank=True, null=True)
    bet_end_time = models.DateTimeField(blank=True, null=True)
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class League(models.Model):
    id = models.BigAutoField(primary_key=True)
    category_id = models.PositiveIntegerField()
    name = models.CharField(max_length=40)
    short_name = models.CharField(max_length=40)
    slug = models.CharField(unique=True, max_length=255)
    image = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leagues'


class Option(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_id = models.IntegerField()
    name = models.CharField(max_length=255)
    odds = models.DecimalField(max_digits=28, decimal_places=8)
    status = models.PositiveIntegerField()
    locked = models.IntegerField()
    winner = models.PositiveIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'options'


class Question(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    status = models.PositiveIntegerField()
    locked = models.IntegerField()
    result = models.PositiveIntegerField()
    refund = models.PositiveIntegerField()
    win_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    amount_refunded = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questions'


class Team(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

