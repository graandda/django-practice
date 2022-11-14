from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tag"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Task(models.Model):
    STATUS_CHOICES = (
        (True, "Done"),
        (False, "Not done"),
    )

    content = models.TextField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(choices=STATUS_CHOICES, default=False, blank=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["status", "-created_at"]

    def __str__(self):
        return self.content
