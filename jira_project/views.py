from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Jira,  Comment, Ticket
from .forms import CommentForm, JiraForm, TicketForm
from django.views import View
from django.shortcuts import get_object_or_404, redirect


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'jira_project/ticket_form.html'
    success_url = reverse_lazy('jira_project:jira-create')  # volta pro form Jira depois de salvar

class JiraListView(ListView):
    model = Jira
    template_name = 'jira_project/jira_list.html'
    context_object_name = 'jiras'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        number = self.request.GET.get('number')
        jira_number = self.request.GET.get('jira_number')
        type_filter = self.request.GET.get('type')
        customer = self.request.GET.get('customer')

        if number:
            queryset = queryset.filter(tickets__number__icontains=number)
        if jira_number:
            queryset = queryset.filter(jira_number__icontains=jira_number)
        if type_filter:
            queryset = queryset.filter(type=type_filter)
        if customer:
            queryset = queryset.filter(tickets__customer__name__icontains=customer)

        return queryset.distinct()


class JiraDetailView(DetailView):
    model = Jira
    template_name = 'jira_project/jira_detail.html'
    context_object_name = 'jira'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context
    

class AddCommentView(View):
    def post(self, request, pk):
        jira = get_object_or_404(Jira, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.jira = jira
            comment.save()
            return redirect('jira_detail', pk=jira.pk)
        return redirect('jira_detail', pk=jira.pk)
    

class JiraCreateView(CreateView):
    model = Jira
    form_class = JiraForm
    template_name = 'jira_project/jira_form.html'
    success_url = reverse_lazy('jira_list')


class JiraUpdateView(UpdateView):
    model = Jira
    form_class = JiraForm
    template_name = 'jira_project/jira_form.html'
    success_url = reverse_lazy('jira_list')


class JiraDeleteView(DeleteView):
    model = Jira
    template_name = 'jira_project/jira_confirm_delete.html'
    success_url = reverse_lazy('jira_list')