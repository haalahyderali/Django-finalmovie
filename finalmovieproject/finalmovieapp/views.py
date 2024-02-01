# from django.core.paginator import InvalidPage, EmptyPage
# from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView

from . models import Movie, Category
from . forms import MovieForm,CommentForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Comment


# ...




def home(request):
    return render(request,'test.html')

def index(request):
     return render(request,"test.html")

def allMoviesCat(request,c_slug=None):
    c_page=None
    movies=None
    if c_slug!=None: #if it is a category page
        c_page=get_object_or_404(Category,slug=c_slug)
        movies=Movie.objects.all().filter(category=c_page)

    else: #if it is home page
        movies = Movie.objects.all()

    # paginator=Paginator(products_list,6)
    # try:
    #     page=int(request.GET.get('page','1'))
    # except:
    #     page=1
    # try:
    #     products=paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     products=paginator.page((paginator.num_pages))
    return render(request,"category.html",{'category':c_page, 'movies':movies})



def movieDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug, slug=movie_slug)



    except Exception as e:
        raise e
    return render(request,'movie.html',{'movie':movie})


def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name', )
        desc = request.POST.get('desc', )
        date = request.POST.get('date', )
        actors = request.POST.get('actors', )
        category = request.POST.get('category', )
        youtubelink = request.POST.get('youtubelink', )
        image = request.FILES['image']

        movie=Movie(name=name,desc=desc,date=date,actors=actors,category=category,youtubelink=youtubelink,image=image)
        movie.save()
        return redirect('/')


    return render(request,"add.html")




class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie

    fields = ['name','desc','date','image','actors','category','youtubelink']
    success_url = reverse_lazy('finalmovieapp:allMoviesCat')
    # success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Movie was added successfully.")
        return super(MovieCreateView, self).form_valid(form)

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    # fields = ['name','body','movie']
    success_url = ('finalmovieapp:allMoviesCat')
    # success_url = '/'

    def form_valid(self, form):
        form.instance.movie_id = self.kwargs['pk']
        messages.success(self.request, "Added comment successfully.")
        return super(CommentCreateView, self).form_valid(form)

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    template_name = 'update.html'
    context_object_name = 'movie'
    fields = ('name','desc','date','image','actors','category','youtubelink')

    success_url = reverse_lazy('finalmovieapp:allMoviesCat')
    # def get_success_url(self):
    #     return reverse_lazy('ss',kwargs={'pk':self.object.id})

    def form_valid(self, form):
        messages.success(self.request, "Movie was updated successfully.")
        return super(MovieUpdateView, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(MovieUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('finalmovieapp:allMoviesCat')

    def form_valid(self, form):
        messages.success(self.request, "Movie was deleted successfully.")
        return super(MovieDeleteView, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(MovieDeleteView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

class MovieListView(LoginRequiredMixin,ListView):
    model = Movie
    context_object_name = 'movies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = context['movies'].filter(user=self.request.user)
        return context

