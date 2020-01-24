from django.urls import path
from . import views

urlpatterns = [

    #Paths del Blog
    path('blog/', views.blog, name="blog"),
    path ('blog/category/<int:category_id>/', views.category, name="category"),
    #<>/ es un campo dinamico. Con eso pasamos un parametro, que la url pasará a la vista como category_id
    #Es importante que se pasa como cadena de caracteres. Como necesitamos que sea un int (xq el id es un int)
    #agregamos int: para castear.
]