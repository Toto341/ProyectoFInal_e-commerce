from django.urls import path
from AppEcommerce import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static
   

urlpatterns = [

    path('',views.index),
    path('inicio',views.index, name="inicio"),    
    path('nosotros',views.nosotros, name="nosotros"),
    path('contacto',views.contacto, name="contacto"),

    path('productos/<int:id_categoria>/<str:categoria>',views.productos, name="productos"),
    path('productos_todos/',views.productos_todos, name="productos_todos"),
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('detalle_producto/<int:id_producto>/', views.detalle_producto, name='detalle_producto'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('editar_producto/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),

    path('buscar/', views.buscar_productos, name='buscar_productos'),


    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'register'),
    path('editar_perfil', views.editar_perfil, name = 'editar_perfil'),
    path('mostrar_perfil', views.mostrar_perfil, name = 'mostrar_perfil'),
    path('cambiar_clave', views.cambiar_clave, name='cambiar_clave'),
    path('salir', views.salir, name = 'salir'),
    path('newsletter', views.newsletter, name ='newsletter'),
]

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


