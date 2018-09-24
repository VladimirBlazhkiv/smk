from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [

      url(r'^$', views.index, name='index'),
      
      url(r'^ship_model/$', views.Ship_ModelListView.as_view(), name='Ship_model'),
      url(r'^ship_detail/(?P<pk>\d+)$', views.Ship_modelDetailView.as_view(), name='Ship_model-detail'),
      
      url(r'^author/$', views.AuthorListView.as_view(), name='Author'),
      url(r'^author_detail/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='Author-detail'),
#--------------------------------------------------------------------------------------------------------------
      ]
##-------------------------------------------------------------------------------------------------------------
urlpatterns += [
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_detail_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    url(r'^ship_model/create/$', views.Ship_modelCreate.as_view(), name='ship_model_create'),
    url(r'^ship_model/(?P<pk>\d+)/update/$', views.Ship_modelUpdate.as_view(), name='ship_model_update'),
    url(r'^ship_model/(?P<pk>\d+)/delete/$', views.Ship_modelDelete.as_view(), name='ship_model_delete'),
]
