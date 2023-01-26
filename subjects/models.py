from django.db import models
from django.contrib.auth.models import User


class Chemistry(models.Model):
    chapter = models.CharField(max_length=700)

    def __str__(self):
        return self.chapter


class ChemistryHard(models.Model):
    chemistry = models.ForeignKey(Chemistry, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class ChemistryHardOptions(models.Model):
    chemistry = models.ForeignKey(ChemistryHard, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class ChemistryEasy(models.Model):
    chemistry = models.ForeignKey(Chemistry, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class ChemistryEasyOptions(models.Model):
    chemistry = models.ForeignKey(ChemistryEasy, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class ChemistryMedium(models.Model):
    chemistry = models.ForeignKey(Chemistry, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class ChemistryMediumOptions(models.Model):
    chemistry = models.ForeignKey(ChemistryMedium, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class Physics(models.Model):
    chapter = models.CharField(max_length=700)

    def __str__(self):
        return self.chapter


class PhysicsHard(models.Model):
    chemistry = models.ForeignKey(Physics, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class PhysicsHardOptions(models.Model):
    chemistry = models.ForeignKey(PhysicsHard, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class PhysicsEasy(models.Model):
    chemistry = models.ForeignKey(Physics, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class PhysicsEasyOptions(models.Model):
    chemistry = models.ForeignKey(PhysicsEasy, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class PhysicsMedium(models.Model):
    chemistry = models.ForeignKey(Physics, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class PhysicsMediumOptions(models.Model):
    chemistry = models.ForeignKey(PhysicsMedium, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class Maths(models.Model):
    chapter = models.CharField(max_length=700)

    def __str__(self):
        return self.chapter


class MathsHard(models.Model):
    chemistry = models.ForeignKey(Maths, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class MathsHardOptions(models.Model):
    chemistry = models.ForeignKey(MathsHard, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class MathsEasy(models.Model):
    chemistry = models.ForeignKey(Maths, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class MathsEasyOptions(models.Model):
    chemistry = models.ForeignKey(MathsEasy, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class MathsMedium(models.Model):
    chemistry = models.ForeignKey(Maths, on_delete=models.CASCADE)
    question = models.CharField(max_length=2083)

    def __str__(self):
        return self.question


class MathsMediumOptions(models.Model):
    chemistry = models.ForeignKey(MathsMedium, on_delete=models.CASCADE)
    options = models.CharField(max_length=2083)
    answer = models.BooleanField()

    def __str__(self):
        return self.options


class ResultChemistry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chemistry_hard = models.IntegerField(default=0)
    chemistry_easy = models.IntegerField(default=0)
    chemistry_medium = models.IntegerField(default=0)


class ResultMaths(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    maths_hard = models.IntegerField(default=0)
    maths_easy = models.IntegerField(default=0)
    maths_medium = models.IntegerField(default=0)


class ResultPhysics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    physics_hard = models.IntegerField(default=0)
    physics_easy = models.IntegerField(default=0)
    physics_medium = models.IntegerField(default=0)


class Chat(models.Model):
    message = models.CharField(max_length=2083)


