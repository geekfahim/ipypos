from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    
    # products
    path('products/', views.products,name='products'),
    path('create-product/',views.createProduct,name='create_product'),
    path('update-product/<str:pk>',views.updateProduct,name='update_product'),
    path('category',views.category,name='category'),
    path('create-category',views.createCategory,name='createcategory'),
    path('update-category/<str:pk>',views.updateCategory,name='updatecategory'),
    path('brand',views.brand,name='brand'),
    path('create-brand',views.createBrand,name='createbrand'),
    path('update-brand/<str:pk>',views.updateBrand,name='updatebrand'),


    
    # customer
    path('customer-Aj/',views.customerAj,name='customerAjx'),

    path('customer/',views.customers,name='customer'),

    path('customer/<str:pk>/', views.customerPage,name='customerpage'),
    path('create-customer/',views.createCustomer,name='create_customer'),
    path('update-customer/<str:pk>',views.updateCustomer,name='update_customer'),



    path('create-order/',views.createOrder,name='sell'),
    path('update-order/<str:pk>',views.updateOrder,name='update_order'),
    path('delete-order/<str:pk>',views.deleteOrder,name='delete_order'),


    path('expense',views.expense,name='expense'),
    path('create-expense',views.createExpense,name='createexpense'),
    path('updateexpense/<str:pk>',views.updateExpense,name='updateexpense'),


    # Software Settings
    path('settings/<str:pk>',views.appConfigUpdate,name='appconfig'),

    # customer api urls
    path('customer-list/', views.customerList, name="customerList"),
    path('customer-create/', views.customerCreate, name="customerCreate"),
]
