from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tool-selector/', views.tool_selector, name='tool_selector'),
    path('files/', views.files, name='files'),
    path('delete-file/', views.delete_file, name='delete_file'),  
    path('delete-folder/', views.delete_folder, name='delete_folder'),
    path('download-folder/<path:folder_path>/', views.download_folder, name='download_folder'),
    path('tool-addition/', views.add_tool, name='tool_addition'),
    path('install-tool/', views.install_tool, name='install_tool'),
    path('tool-help/', views.tool_help, name='tool_help'),
    path('tool-deletion/', views.tool_deletion, name='tool_deletion'),
    path('delete-tool/', views.delete_tool, name='delete_tool'),

]
