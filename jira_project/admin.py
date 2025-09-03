from django.contrib import admin
from .models import Customer, Ticket, Jira, Comment

admin.site.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'customer')
    search_fields = ('number', 'customer__name')
    list_filter = ('customer',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ('author', 'text', 'informed_date')

admin.site.register(Jira)
class JiraAdmin(admin.ModelAdmin):
    list_display = ('jira_number', 'type', 'creation_date')
    search_fields = ('jira_number',)
    list_filter = ('type',)
    filter_horizontal = ('tickets',)