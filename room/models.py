from django.db import models
from django.contrib.auth.models import User  

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=512)
    description=models.CharField(max_length=150,null=True,blank=True)
    def __str__(self) -> str:
        return str(self.name)
        
class Chat(models.Model):
    content=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(auto_now=True)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.room.name)

class MCQ(models.Model):
    problem_statement=models.CharField(max_length=250,null=False,blank=False)
    options=models.ManyToManyField(to='Option')
    correct=models.ForeignKey(to='Option',related_name='correct_for_mcqs', on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "MCQs"
    def __str__(self) -> str:
        return str(self.problem_statement)
        

class Option(models.Model):
    statement=models.CharField(max_length=150,null=False,blank=False)
    valid=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Options"
    def __str__(self) -> str:
        return str(self.statement)

class Quiz(models.Model):
    host=models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.OneToOneField(Room, on_delete=models.CASCADE)
    questions=models.ManyToManyField(to=MCQ)
    datetime=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Quizes"
    def __str__(self) -> str:
        return str(self.room)


'''
class MCQ(models.Model):
    problem_statement=models.CharField(max_length=250)
    # options=models.ManyToManyField(Option)
    correct=models.ForeignKey('Option', on_delete=models.CASCADE)

class Option(models.Model):
    question=models.ForeignKey(MCQ,on_delete=models.CASCADE)
    statement=models.CharField(max_length=150)
    valid=models.BooleanField(default=False)

class Quiz(models.Model):
    room=models.OneToOneField(Room, on_delete=models.CASCADE)
    questions=models.ManyToManyField(MCQ)
    datetime=models.DateField(auto_now_add=True)
    completed=models.BooleanField(default=False)
'''