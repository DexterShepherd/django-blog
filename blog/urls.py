from django.conf.urls import url
from . import views

urlpatterns = [
    #home
    url(r'^$', views.index, name='blog_index'),

    #post crud TODO should be using http verbs instead of urls for crud actions
    url(r'^view/(?P<slug>[^\.]+)/$',
        views.view_post,
        name='view_blog_post'),

    url(r'^new/$',
        views.new_post,
        name='new_blog_post'),

    url(r'^destroy/(?P<slug>[^\.]+)/$',
        views.destroy_post,
        name='destroy_blog_post'),
    
    url(r'^edit/(?P<slug>[^\.]+)/$',
        views.edit_post,
        name='edit_blog_post'),

    #category crud
    url(r'^category/new/$',
        views.new_category,
        name='new_blog_category'),

    url(r'^category/destroy/(?P<slug>[^\.]+)/$',
        views.destroy_category,
        name='destroy_blog_category'),
    
    url(r'^category/edit/(?P<slug>[^\.]+)/$',
        views.edit_category,
        name='edit_blog_category'),

    url(r'^category/(?P<slug>[^\.]+)/$',
        views.view_category,
        name='view_blog_category'),
]

