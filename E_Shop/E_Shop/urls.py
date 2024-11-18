from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index" ),
    path('Products/',views.Products,name="Products"),
    path('Product_details/',views.Product_details,name="Product_details")
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
