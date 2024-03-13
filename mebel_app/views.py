from django import views
from django.shortcuts import render, get_object_or_404
from django.views import View

from mebel_app.models import Contact, About, Project, Employee


# Create your views here.
class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'index.html', context)


class ProjectView(views.View):
    title = 'Услуги'
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        context = {
            'projects': projects,
            'title': self.title
        }
        return render(request, 'project.html', context)


class ProjectDetailView(views.View):

    def get(self, request, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=pk)
        context = {
            'project': project
        }
        return render(request, 'project_detail.html', context)


class AboutView(views.View):
    title = 'О нас'
    projects = Project.objects.all()
    employers = Employee.objects.all()

    def get(self, request, *args, **kwargs):
        about = About.objects.filter(active=True)
        context = {
            'about': about,
            'projects': self.projects,
            'employers': self.employers,
            'title': self.title
        }
        return render(request, 'about_us.html', context)


class ContactView(views.View):
    title = 'Контакты'
    def get(self, request, *args, **kwargs):
        contact = Contact.objects.filter(active=True)
        context = {
            'contact': contact,
            'title': self.title
        }
        return render(request, 'contact.html', context)