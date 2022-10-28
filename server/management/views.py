from ast import Add
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from management.models import Campaign, Company, Token
from management.serializers import CompanySerializer, TokenSerializer, CampaignSerializer


class CompanyList(APIView):
    """ List all companies or create new company """
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializers = CompanySerializer(companies, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        


class CompanyDetails(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        serializers = CompanySerializer(company)
        return Response(serializers.data)
        
    def put(self, request, pk, format=None):
        company = self.get_object(pk)
        serializers = CompanySerializer(company, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class TokenDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

class CampaingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
