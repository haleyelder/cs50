from django.shortcuts import render, redirect
from django import forms
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.http import HttpResponseRedirect
import markdown2
import random

from . import util

# renders homepage with listed entries
def index(request):
   if "entries" not in request.session:
       request.session["entries"] = []

   return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# display entry on page /wiki/ENTRY TITLE
def entry(request, title):
    entries = util.list_entries()
    if (entries):
        return render(request, "encyclopedia/entry.html", {
            "entry": markdown2.markdown(util.get_entry(title)),"title": title
        })

#search bar
def search(request):
    if request.method == "GET":
        query = request.GET.get('q')
        # gets full entry, not titles
        result = util.get_entry(query)
        titles = util.list_entries()
        
        # if entry matches, redirect to entry
        if result:
            content = markdown2.markdown(result)
            return redirect(entry, query)
        else:
            partial_search = []
            for x in titles:
                if query in x or query in x.lower():
                    partial_search.append(x)
            return render(request,  "encyclopedia/search_results.html", {"content": partial_search})

# add new entry form
def add(request):
    if request.method == "POST":
        add_form = NewEntryForm(request.POST)

        if add_form.is_valid():
            title = add_form.cleaned_data['title']
            entry = add_form.cleaned_data['entry']

            util.save_entry(title,entry)
            return redirect("wiki/" + title)
            
        else:    
            return render(request, "encyclopedia/add.html", {
                "add_form": add_form
            })
        
    return render(request, "encyclopedia/add.html", {
        "add_form": NewEntryForm()
    })
    
class NewEntryForm(forms.Form):
    title = forms.CharField()
    entry = forms.CharField(widget=forms.Textarea(attrs={'style':'height: 400px'})) 

    
    def clean_title(self):
        data = self.cleaned_data['title']  
        entries = util.list_entries()
        if data in entries:        
            raise forms.ValidationError('Entry already exists')
        return data

    

def edit(request, title):
    edit_entry = util.get_entry(title)

    if request.method == 'POST':
        edit_form = EditEntryForm(request.POST)
        if edit_form.is_valid():
            edit_entry = edit_form.cleaned_data['edit_entry']            
            util.save_entry(title,edit_entry)

            return redirect('/wiki/' + title)
    else:
        edit_form = EditEntryForm(initial={'edit_entry': edit_entry})

    return render(request, 'encyclopedia/edit.html', {'edit_form': edit_form})



class EditEntryForm(forms.Form):
    edit_entry = forms.CharField(widget=forms.Textarea(attrs={'style':'height: 400px'})) 
    
def randompage(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    return render(request, "encyclopedia/randompage.html", {
        "content": markdown2.markdown(util.get_entry(selected_page))
    })

def error404(request, exception, template_name='encyclopedia/404.html'):
    return render(request, template_name)

def error500(request):
    data = {}
    return render(request,'encyclopedia/500.html', data)

