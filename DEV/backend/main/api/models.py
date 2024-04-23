"""models that define the db tables"""
from django.db import models

# if you are checking pylint ignore the id warnings

# Create your models here.
class User(models.Model):
    """table user"""

    name = models.CharField(max_length=200, default="", unique=True)
    password = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")

    __role_choices = ((1, "creator"), (2, "solver"))
    role = models.IntegerField(choices=__role_choices, default=1)

    def __str__(self) -> str:
        return f"{self.name}"


class Tag(models.Model):
    
    value = models.CharField(max_length=3, default="ES", unique=True)

    def __str__(self) -> str:
        return self.value

class Question(models.Model):
    """table question"""

    # user that is creating the question
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.CharField(max_length=500, default="")
    opt_text = models.CharField(max_length=400, default="")
    explanation = models.CharField(max_length=500, default="")

    #tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    __state_choices = (
        (1, "not_submitted"),
        (2, "in_evaluation"),
        (3, "rejected"),
        (4, "accepted"),
    )
    state = models.IntegerField(choices=__state_choices, default=1)

    num_tests = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.name}_{self.id}"


class Option(models.Model):
    """table option"""

    # question that the option belongs to
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    body = models.CharField(max_length=500, default="")
    is_correct = models.BooleanField(default=False)
    justification = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return f"{self.question.id}_{self.id}"


class Test(models.Model):
    """table test"""

    # user that is creating the test
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, default="")
    # the same question can belong to many tests
    # a test is composed of multiple questions
    questions = models.ManyToManyField(Question)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return f"{self.creator}_{self.id}"


class SolvedTest(models.Model):
    """table solved tests

    A solved test is a user's submitted answers to a test.
    """

    class Meta:
        """Inner Model class

        Using to create a custom primary key (unique constraint) with multiple fields
        """

        unique_together = (("user", "test"),)

    # user that is solving the test
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # the test that is being solved
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    # the same option can belong to many 'answer sheets'
    # an answer sheet is composed of multiple options
    options = models.ManyToManyField(Option)

    # save grade the user had
    grade = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.id}_{self.test.id}"


class Vote(models.Model):
    """table vote"""

    class Meta:
        """Inner Model class

        Using to create a custom primary key (unique constraint) with multiple fields
        """

        unique_together = (("user", "question"),)

    # user that is making the vote
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # question the vote is evaluating
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    is_approved = models.BooleanField(default=False)

    justification = models.CharField(max_length=500, default="")

    def __str__(self) -> str:
        return f"{self.user}_{self.question.id}"


all_classes = [User, Question, Option, Test, SolvedTest, Vote, Tag]
