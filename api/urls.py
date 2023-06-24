from django.urls import path
from .views import book_list,overview,book_details,create_book,update_book,delete_book
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',overview,name='overview'),
    path('book-list/',book_list,name='Book List'),
    path('book-details/<str:pk>/',book_details,name='Book Details'),
    path('create-book/',create_book,name='Create Book'),
    path('update-book/<str:pk>/',update_book,name='Update Book'),
    path('delete-book/<str:pk>/',delete_book,name='Delete Book'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
