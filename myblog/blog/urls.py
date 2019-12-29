from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('',views.PostListView.as_view(), name="post_list" ),
    path('about/', views.AboutView.as_view(), name="about"),
    path('post/new',views.PostCreateView.as_view(),name="post_create"),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(), name="post_detail"),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name="post_update"),  # in post_detail.html
    url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name="post_delete"),  # in post_detail.html
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name="post_publish"),
    path('drafts/',views.DraftListView.as_view(), name="post_draft_list"),
    ##############
    # path('post/<pk>/comment', views.CommentCreateView.as_view(), name='add_comment_to_post'),
    # url(r'^post/(?P<pk>\d+)/comment/$',views.CommentCreateView.as_view(), name="add_comment_to_post"),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post, name="add_comment_to_post"),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name="comment_approve"),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name="comment_remove"),

]