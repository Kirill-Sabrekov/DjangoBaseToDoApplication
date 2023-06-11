from django.db import models

class ToDoTables(models.Model):
    name_table = models.CharField(max_length=50)

    def __str__(self):
        return self.name_table

class ToDoListItem(models.Model):
    content = models.TextField()
    todo_tables = models.ForeignKey(ToDoTables, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.todo_tables) + " " + self.content
