from django.db import models

# Create your models here.


class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def save_editor(self):
        self.save()

    def delete_editor(self, first_name):
        self.objects.filter(first_name=first_name).delete()

    def update_editor(self, first_name, new_name):
        self.objects.filter(first_name=first_name).update(first_name=new_name)

    def display_all():
        all = Editor.objects.all()

        return all

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
