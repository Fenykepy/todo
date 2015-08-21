from django.db import models

from user.models import User



class Task(models.Model):
    """
    Table for todo tasks entrys.
    """
    description = models.CharField(max_length=254,
            verbose_name="Description")
    completed = models.BooleanField(default=False, db_index=True,
            verbose_name="Task completed")
    due_time = models.DateTimeField(blank=True, null=True, db_index=True,
            verbose_name="Due time")
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User)

    class Meta:
        ordering = ['-due_time', '-date_created']
