from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='main'
urlpatterns = [
    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
