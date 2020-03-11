from django.shortcuts import render , get_object_or_404
from .models import Project, Expense
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .forms import ExpenseForm
# Create your views here.
def project_list(request):
    return render(request, 'Xpense_manager/project-list.html')

def project_detail(request, project_slug):
    project= get_object_or_404(Project, slug=project_slug)
    if request.method == 'GET':
        return render(request, 'Xpense_manager/project-detail.html', {'project' : project, 'expense_list': project.expenses.all()})

    elif request.method == 'POST':
        #process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            date = form.cleaned_data['date']
        
            ExpenseForm.objects.create(
                project=project,
                title=title,
                amount=amount,
                date=date
            ).save()   


    return HttpResponseRedirect(project_slug)
class ProjectCreateView(CreateView):
    model = Project
    template_name = 'Xpense_manager/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object= form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return slugify(self.request.POST['name'])
     