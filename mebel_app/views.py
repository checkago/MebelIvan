from django import views
from django.shortcuts import render


# Create your views here.
class IndexView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'index.html', context)


class ProjectView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'project.html', context)


class ProjectDetailView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'project_detail.html', context)


class AboutView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'about_us.html', context)


class ContactView(views.View):

    def get(self, request, *args, **kwargs):
        context = None
        return render(request, 'contact.html', context)