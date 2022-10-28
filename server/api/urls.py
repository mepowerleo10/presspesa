from django.urls import path
from management.views import CompanyDetails, CompanyList, TokenList, TokenDetails, CampainList, CampainDetails

urlpatterns = [
    # Company endpoints
    path('company/', CompanyList.as_view(), name='company_list'), # Endpoint for listing all company or create a new one
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company_details'), # Endpoint for retrieving, update or delete a company instance.

    # Token Endpoints
    path('token/', TokenList.as_view(), name='tokens'), # Endpoint for listing all tokens
    path('token/<int:pk>/', TokenDetails.as_view(), name='token_details'), # Endpoint for retrieving , update or delete a token instance

    # Token Endpoints
    path('campain/', CampainList.as_view(), name='campains'), # Endpoint for listing all tokens
    path('campain/<int:pk>/', CampainDetails.as_view(), name='campain_details'), # Endpoint for retrieving , update or delete a token instance


]
