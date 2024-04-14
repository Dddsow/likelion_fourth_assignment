from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # READ
    path('', views.home, name='home'), #1번 URL 기본 base URL 2번 views.home 호출 뒤에 name은 별명임
    # DETAIL READ
    path('blog/<int:blog_id>', views.detail, name='detail'),
    # CREATE
    path('blog/new', views.new, name='new'),
    path('blog/create', views.create, name='create'),
    # UPDATE
    path('blog/edit/<int:blog_id>', views.edit, name='edit'),
    path('blog/update/<int:blog_id>', views.update, name='update'),
    # DELETE
    path('blog/delete/<int:blog_id>', views.delete, name='delete'),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
