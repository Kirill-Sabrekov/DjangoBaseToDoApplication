from django.contrib import admin
from django.urls import include, path
from todo.views import todoappView, addTodoView, deleteTodoView, addToDoTable, deleteToDoTable

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoappView),
    path('addTodoItem/<int:table_id>/',addTodoView),
    path('deleteTodoItem/<int:i>/', deleteTodoView),
    path('addToDoTable/', addToDoTable),
    path('deleteToDoTable/<int:table>/', deleteToDoTable),
    #path('accounts/', include('allauth.urls')),
    ]
