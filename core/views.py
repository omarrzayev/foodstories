from django.shortcuts import render
from core.models import *
from core.forms import *

def home(request):
    stories = Story.objects.order_by('-id')[:4]
    recent_story = stories.first()
    categories = Category.objects.all()
    holiday_stories = Story.objects.filter(category__title='Holiday')
    context = {
        'stories': stories,
        'recent_story': recent_story,
        'categories': categories,
        'holiday_stories': holiday_stories,
    }
    return render(request, 'index.html', context=context)

def story_detail(request,id):
    if request.method ==  'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.story = Story.objects.get(id=id)
            comment.user = request.user
            comment.save() 
    form = CommentForm()
    story = Story.objects.get(id=id)
    categories = Category.objects.all()
    recent_stories = Story.objects.order_by('-id')[:3]
    tag = Tag.objects.all()
    context = {
        'data': story,
        'categories': categories,
        'recent_stories': recent_stories,
        'tags':tag,
        'form':form,
    }
    return render(request, 'single.html', context=context)

def stories(request):
    search = request.GET.get('search')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    stories = Story.objects.all()
    if search:
        stories = Story.objects.filter(title__contains=search)    
    if cat:
        stories = Story.objects.filter(category__title=cat)
    if tag:
        stories = Story.objects.filter(tags__title=tag)    
    categories = Category.objects.all()
    context = {
        'stories': stories,
        'categories': categories,
    }
    return render(request, 'stories.html', context=context)


def recipes(request):
    search = request.GET.get('search')
    cat = request.GET.get('cat')
    recipes = Recipe.objects.all()
    if search:
        recipes = Recipe.objects.filter(title__contains=search)    
    if cat:
        recipes = Recipe.objects.filter(category__title=cat)    
    categories = Category.objects.all()
    context = {
        'recipes' : recipes,
        'categories' : categories,
    }
    return render(request, 'recipes.html', context=context)

def recipe_detail(request, id):
    recipe = Recipe.objects.get(id=id)
    categories = Category.objects.all()
    recent_stories = Recipe.objects.order_by('-id')[:3]
    tag = Tag.objects.all()
    context = {
        'data': recipe,
        'categories': categories,
        'recent_stories': recent_stories,
        'tags':tag
    }
    return render(request, 'single.html', context=context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {
        'form' : form
    }
    return render(request, 'contact.html', context=context)

def about(request):
    return render(request, 'about.html')