from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from messenger import views


urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='Posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='PostDetail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='PostUpdate'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='PostDelete'),
    path('post/create/', views.PostCreateView.as_view(), name='PostCreate'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
