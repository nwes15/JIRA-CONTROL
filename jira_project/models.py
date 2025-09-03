from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Ticket(models.Model):
    number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='tickets')

    def __str__(self):
        return f'Ticket {self.number} for {self.customer.name}'
    

class Jira(models.Model):
    TYPE_CHOICES = [
        ('SERVER', 'Server'),
        ('MAUI', 'Maui'),
    ]

    jira_number = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    first_release = models.CharField(max_length=10)
    applied_releases = models.JSONField(default=list)
    creation_date = models.DateField()
    solution_date = models.DateField(null=True, blank=True)
    tickets = models.ManyToManyField(Ticket, related_name='jiras')

    def __str__(self):
        return f'Jira {self.jira_number} ({self.type})'
    

class Comment(models.Model):
    jira = models.ForeignKey(Jira, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    informed_date = models.DateField()

    def __str__(self):
        return f'Comment by {self.author} on {self.informed_date.strftime("%d/%m/%Y")}'