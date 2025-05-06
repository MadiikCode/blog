from django.contrib import admin
from django.urls import path, include  # Добавь include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('notes.urls')),  # Подключение URLs приложения notes
]

