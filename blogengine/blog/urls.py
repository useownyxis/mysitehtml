from django.urls import path

from .views import *

urlpatterns = [
	path('', post_list, name='post_list_url'),
	path('post/create/', PostCreate.as_view(), name='post_create_url'),
	path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
	path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
	path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
	path('tags/', tags_list, name='tags_list_url'),
	path('tags/create/', TagCreate.as_view(), name='tag_create_url'),
	path('tags/<str:slug>/', TagDetail.as_view(), name='tags_detail_url'),
	path('tags/<str:slug>/update/', TagUpdate.as_view(), name='tags_update_url'),
	path('tags/<str:slug>/delete/', TagDelete.as_view(), name='tags_delete_url'),
	path('game/', ShowGame, name='game_show_url'),
	path('gameeditor/',EditGame, name='game_edit_url'),
]
