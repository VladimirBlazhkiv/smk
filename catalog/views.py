from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AuthorForm, Ship_modelForm

# Create your views here.
from .models import Author, Ship_model
from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_ship_model=Ship_model.objects.all().count()
    num_authors=Author.objects.count()
    # Метод 'all()' применен по умолчанию.


    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    #--------------------------------------------------------------------


    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_ship_model':num_ship_model,'num_authors':num_authors,'num_visits':num_visits},
    )
###-----------------------------загрузка фото  ------------------------------------------------
@login_required
def Upload_file(request):

  if request.method == 'POST':
    form = Ship_modelForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/catalog/ship_model/')
  else:
    form = Ship_modelForm()

  return render(
      request, 
      'ship_model_form.html', {'form': form},
      )


  if request.method == 'POST':
    form = AuthorForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/catalog/author/')
  else:
    form = AuthorForm()

  return render(
      request, 
      'author_form.html', {'form': form},
      )
#-----------------------------------------------------------------------------------------------------
from django.views import generic

class Ship_ModelListView(generic.ListView):
    model = Ship_model
    paginate_by = 15
class Ship_modelDetailView(generic.DetailView):
    model = Ship_model
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 15
class AuthorDetailView(generic.DetailView):
    model = Author
##-----------------------------------------------------------------------
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial={'date_of_birth':'12/10/1970',}
    success_url = reverse_lazy('Author')
class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__'
    #fields = ['first_name','last_name','date_of_birth']
    success_url = reverse_lazy('Author')

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

##------------------------------------------------------------------------

from .models import Ship_model
class Ship_modelCreate(CreateView):
    model = Ship_model
    fields = '__all__'
    initial={'date_start':'12/10/2016',}
    success_url = reverse_lazy('Ship_model')


class Ship_modelUpdate(UpdateView):
    model = Ship_model
    fields = '__all__'
    success_url = reverse_lazy('Ship_model')

class Ship_modelDelete(DeleteView):
    model = Ship_model
    success_url = reverse_lazy('Ship_model')

##------------------------------------------------------------------------
