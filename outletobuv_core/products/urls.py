from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

from .views import parse_tsgoods_view, ProductsListView, ProductDetailView, ProductUpdateView, products2, hide, search_by_name, about


app_name = 'products'

urlpatterns = [
        
    # path('', index, name='index'),
    # path('category/<int:category_id>/', products2, name='test2'),
    path('test/<int:page_number>/', products2, name='test'),
    # path('detail/<int:product_id>/', product, name='detail'),

    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductsListView.as_view(), name='category'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path('product/<int:pk>/update_image/', ProductUpdateView.as_view(), name='update_product_image'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),

        path('about/', about, name='about'),
    path('search/', search_by_name, name='search'),
    
    path('parse-tsgoods/', parse_tsgoods_view, name='parse_tsgoods'),
    path('hide/', hide, name='hide'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        