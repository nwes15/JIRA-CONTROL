from django.urls import path
from . import views

app_name = 'jira_project'

urlpatterns = [
    path('', views.JiraListView.as_view(), name='jira-list'),
    path('jira/<int:pk>/', views.JiraDetailView.as_view(), name='jira-detail'),
    path('jira/<int:pk>/add-comment/', views.AddCommentView.as_view(), name='add-comment'),
    path('jira/create/', views.JiraCreateView.as_view(), name='jira-create'),
    path('jira/<int:pk>/update/', views.JiraUpdateView.as_view(), name='jira-update'),
    path('jira/<int:pk>/delete/', views.JiraDeleteView.as_view(), name='jira-delete'),
    path('ticket/create/', views.TicketCreateView.as_view(), name='ticket-create'),
    path('customer/create/', views.CustomerCreateView.as_view(), name='customer-create'),
]