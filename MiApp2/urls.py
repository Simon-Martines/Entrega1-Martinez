from django.urls import path

from MiApp2 import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('', views.mostrar_index, name='Inicio' ),
        path('mostrar_trabajo/', views.mostrar_trabajo, name='Mostrar Trabajo'),
        path('mostrar_empleado/', views.mostrar_empleado, name='Mostrar Empleados'),
        path('crear_trabajo/', views.crear_trabajo, name='Crear Trabajo'),
        path('crear_empleado/', views.crear_empleado, name='Crear Empleado'),
        path('buscar_trabajo/', views.buscar_trabajo, name='Buscar Trabajo'),
        path('buscar_empleado/', views.buscar_empleado, name='Buscar Empleado'),
        path('soporte/', views.soporte, name='Soporte'),
        path('actualizar_empleado/<empleado_id>', views.actualizar_empleado, name='actualizar empleado'),
        path('eliminar_empleado/<empleado_id>', views.eliminar_empleado, name='eliminar empleado'),
        path('actualizar_trabajo/<trabajo_id>', views.actualizar_trabajo, name='actualizar trabajo'),
        path('eliminar_trabajo/<trabajo_id>', views.eliminar_trabajo, name='eliminar trabajo'),
        path('trabajos_list/', views.TrabajoList.as_view(), name='List'),
        path('trabajo_detail/<pk>', views.TrabajoDetailView.as_view(), name='Detail'),
        path('trabajo_confirm_delete/<pk>', views.TrabajoDeleteView.as_view(), name='Delete'),
        path('trabajo_edit/<pk>', views.TrabajoUpdateView.as_view(), name='Update'),
        path('trabajo_form/', views.TrabajoCreateView.as_view(), name='Create'),
        path('login/', views.login_request, name='Login'),
        path('register/', views.register, name='Register'),
        path('logout/', LogoutView.as_view(template_name='MiApp2/logout.html'), name='Logout'),
]