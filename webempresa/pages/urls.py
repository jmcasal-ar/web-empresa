from django.urls import path
from . import views

urlpatterns = [
    path ('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
    #<>/ es un campo dinamico. Con eso pasamos un parametro, que la url pasará a la vista como category_id
    #Es importante que se pasa como cadena de caracteres. Como necesitamos que sea un int (xq el id es un int)
    #agregamos int: para castear.
]