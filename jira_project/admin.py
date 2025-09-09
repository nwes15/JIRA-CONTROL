from django.contrib import admin
from .models import Customer, Ticket, Jira, Comment

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('number', 'customer')
    search_fields = ('number', 'customer__name')
    list_filter = ('customer',)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    fields = ('author', 'text', 'informed_date')

class JiraAdmin(admin.ModelAdmin):
    list_display = ('jira_number', 'type', 'creation_date')
    search_fields = ('jira_number',)
    list_filter = ('type',)
    filter_horizontal = ('tickets',)
    inlines = [CommentInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Jira, JiraAdmin)