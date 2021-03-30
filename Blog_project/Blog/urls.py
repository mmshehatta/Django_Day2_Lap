from django.urls import path

from .views import index ,create_article , article_delete,article_update


urlpatterns = [
    path('', index, name='index'),
    path('create/',  create_article, name='create'), #article_delete
    path('delete/<int:id>',  article_delete, name='delete'),
    path('update/<int:id>',  article_update ,  name='update'),


    # we dont reference static url by hard code but we will reference url methods as
    # index  , create and so on.
    # another reaaon is that app dont know under what prefix he will be

]