from django.views import generic
from django.shortcuts import render


class IndexView(generic.TemplateView):
    template_name = "index.html"

class SearchView(generic.TemplateView):
    template_name = "search.html"

class User_LoginView(generic.TemplateView):
    template_name = "user_login.html"

class Company_LoginView(generic.TemplateView):
    template_name = "company_login.html"
    
class User_EntryView(generic.TemplateView):
    template_name = "user_entry.html"
    
class User_DetailView(generic.TemplateView):
    template_name = "user_detail.html"
    
class Company_EntryView(generic.TemplateView):
    template_name = "company_entry.html"
    
class Company_DetailView(generic.TemplateView):
    template_name = "company_detail.html"
    
class Service_EntryView(generic.TemplateView):
    template_name = "service_entry.html"
    
class Service_DetailView(generic.TemplateView):
    template_name = "service_detail.html"
    
class Post_EntryView(generic.TemplateView):
    template_name = "post_entry.html"
    
class Post_DetailView(generic.TemplateView):
    template_name = "post_detail.html"

class Post_FinishView(generic.TemplateView):
    template_name = "post_finish.html"
    
class After_LoginView(generic.TemplateView):
    template_name = "after_login.html" 
