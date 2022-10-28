from django.urls import path
from management.views import CompanyDetails, CompanyList, TokenList, TokenDetails, CampaignList, CampaingDetails

urlpatterns = [
    # Company endpoints
    path('company/', CompanyList.as_view(), name='company_list'), # Endpoint for listing all company or create a new one
    path('company/<int:pk>/', CompanyDetails.as_view(), name='company_details'), # Endpoint for retrieving, update or delete a company instance.

    # Token Endpoints
    path('token/', TokenList.as_view(), name='tokens'), # Endpoint for listing all tokens
    path('token/<int:pk>/', TokenDetails.as_view(), name='token_details'), # Endpoint for retrieving , update or delete a token instance

    # Token Endpoints
    path('campaign/', CampaignList.as_view(), name='campaigns'), # Endpoint for listing all tokens
    path('campaign/<int:pk>/', CampaingDetails.as_view(), name='campaign_details'), # Endpoint for retrieving , update or delete a token instance


]
