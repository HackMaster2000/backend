from django.urls import path
from app import views


urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('users/register/', views.registerUser, name='register'),
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', views.getProducts, name='getProducts'),
    path('testimonials/', views.getTestimonials, name='getTestimonials'),
    path('team-members/', views.getTeamMembers, name='getTeamMembers'),
    path('blogs/', views.getBlogs, name='getBlogs'),
    path('user/profile/', views.getUserProfiles, name='getUserProfiles'),
    path('products/<str:pk>', views.getProduct, name='getProduct'),
    path('product/<str:pk>/update_stock/', views.updateProductStock, name='update-product-stock'),
    path('products/update_stock/', views.update_multiple_products_stock, name='update-multiple-products-stock'),
    path('users/', views.getUsers, name='getUsers'),
    path('orders', views.CrearOrden.as_view(),),
    path('orders/capture', views.CapturarOdernPaypal.as_view(),),
]
