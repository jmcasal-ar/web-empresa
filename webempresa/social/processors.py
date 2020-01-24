from .models import Link
#Importamos el modelo

#creamos una funcion
def ctx_dict(request):
    ctx = {}
    #creamos la variable ctx
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
        #Para cada link en la key se le asigna una url
    return ctx