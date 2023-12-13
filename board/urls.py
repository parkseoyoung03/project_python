from django.urls import path
from .views import index, detail, create, UpdateBoard, DeleteBoard, PaginatedBoardList

app_name = "board"

urlpatterns = [

    path('create/', create.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBoard.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteBoard.as_view(), name='delete'),
    path('<int:board_id>/', detail, name='check'),
    path('',  index , name='list'),
]