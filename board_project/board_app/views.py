from django.shortcuts import render,get_object_or_404
from .models import ProductType, Product, Review, Genre, Article, Job, Event
from .forms import ProductForm, ArticleForm, JobForm, EventForm
from django.contrib.auth.decorators import login_required


# Create views
def index (request):
    return render(request, 'board_app/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'board_app/types.html' ,{'type_list' : type_list})

def getproducts(request):
    products_list=Product.objects.all()
    return render(request, 'board_app/products.html', {'products_list': products_list})

@login_required
def productdetails(request, id):
    prod=get_object_or_404(Product, pk=id)
    discount=prod.memberdiscount
    reviews=Review.objects.filter(product=id).count()
    context={
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews,
    }
    return render(request, 'board_app/proddetails.html', context=context)

@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'board_app/newproduct.html', {'form': form})


def getarticle (request):
    article_list=Article.objects.all()
    return render(request, 'board_app/article.html', {'article_list' : article_list})

@login_required
def getarticledetail (request, id):
    article_detail=get_object_or_404(Article, pk=id)
    return render(request, 'board_app/articledetail.html', {'article_detail' : article_detail})

@login_required
def newArticle(request):
     form=ArticleForm
     if request.method=='POST':
          form=ArticleForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ArticleForm()
     else:
          form=ArticleForm()
     return render(request, 'board_app/newArticle.html', {'form': form})


def getjobs(request):
    type_list=Job.objects.all()
    return render(request, 'board_app/jobs.html' ,{'type_list' : type_list})

@login_required
def getjobsdetails(request, id):
    job=get_object_or_404(Job, pk=id)
    return render(request, 'board_app/jobsdetails.html',{'job' : job})

@login_required
def newJob(request):
     form=JobForm
     if request.method=='POST':
          form=JobForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=JobForm()
     else:
          form=JobForm()
     return render(request, 'board_app/newjob.html', {'form': form})

def getEvent(request):
    event_list = Event.objects.all()
    return render(request, 'board_app/event.html', {'event_list': event_list})

@login_required
def eventDetail(request, id):
    detail = get_object_or_404(Event, pk=id)

    return render(request, 'board_app/eventDetail.html', {'detail': detail})

@login_required
def newEvent(request):
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
            form = EventForm()
    else:
        form = EventForm()
    return render(request, 'board_app/newevent.html', {'form': form})


def loginmessage(request):
    return render(request, 'board_app/loginmessage.html')

def logoutmessage(request):
    return render(request, 'board_app/logoutmessage.html')