from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url

# from listings.views import (
#     listing_create_view,
#     )

from .views import (
    home_page,
    home_search_page,

    buyer_seminar_page,
    buyer_guide_page,
    mortgage_calc_page,
    cash_flow_page,

    consultation_page,
    move_list_page,
    resources_page,

    #neighbourhood_page,

    contact_page,

    renters_page,
    testimonials_page
)

urlpatterns = [
    path('', home_page),

    #path('listings-new/', listing_create_view),
    #path('listings/', include('listings.urls')),

    path('home-search/', home_search_page),
    path('buyer-seminar/', buyer_seminar_page),
    path('buyer-guide/', buyer_guide_page),
    path('mortgage-calculator/', mortgage_calc_page),
    path('cash-flow/', cash_flow_page),

    path('listing-consultation/', consultation_page),
    path('moving-list/', move_list_page),
    path('moving-resources/', resources_page),
    
    path('contact/', contact_page),

    path('renters/', renters_page),
    path('testimonials/', testimonials_page),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    # Test Mode
    from django.conf.urls.static import static
    #urlpatterns += static_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)