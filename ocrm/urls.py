from django.urls import path

from . import views

app_name = 'ocrm'
urlpatterns = [
    path('', views.index, name='index'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('contacts/', views.ContactListView.as_view(), name='contacts'),
    path('leads/', views.LeadListView.as_view(), name='leads'),
    path('create_lead/', views.create_lead, name='create_lead'),
    path('convert_lead_to_contact/<int:lead_id>/', views.convert_lead_to_contact, name='convert_lead_to_contact'),
    path('contacts/<int:pk>/', views.ContactView.as_view(), name='contact_detail'),
    path('leads/<int:pk>/', views.LeadView.as_view(), name='lead_detail'),
    path('contacts/<int:contact_id>/create_owned_product/', views.create_owned_product, name='create_owned_product'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/edit_product/<int:product_id>', views.edit_product, name='edit_product'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
]