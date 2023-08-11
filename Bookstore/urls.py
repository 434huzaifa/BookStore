from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from frontend.views import book_list,book_details,cart,create_book,order_submited
urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',book_list,name='Book List'),
    path('book-details/<str:pk>/',book_details,name='Book Details'),
    path('cart/',cart,name='Cart'),
    path('create-book/',create_book,name='Create Book'),
    path('order-submited/',order_submited,name='Order Submited')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)