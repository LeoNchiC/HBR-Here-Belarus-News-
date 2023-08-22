from django.urls import path

from . import views

from .views import index
from .views import detail


urlpatterns = [
	path('', index, name="index_page"),
	path('<int:article_id>/', detail, name='detail_page'),
	path('<int:article_id>/leave_comment', views.leave_comment, name='leave_comment'),
	path('<int:article_id>/image', views.image, name='image'),
]