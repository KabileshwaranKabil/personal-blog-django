from django.urls import path
from . import views


handler404='myapp.views.py.custom_page_not_found'
app_name='blog'
urlpatterns=[
    path("blog/",views.index,name="blog-index"),
    path("blog/post/<str:post_id>",views.detail,name="detail"),
    path("new_url",views.new_url_view,name="new_page_url"),
    path("old_url",views.old_url_redirect,name="old_url")
]