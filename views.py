from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from apiapp.models import Site

@api_view(["GET"])

def get_site(request):

    sites=Site.objects.all()

    for s in sites:
        print("site names are:\n",s.site_name)
        # print("/n")
        # print(s.rd_name)
        # print(s.rd_version)

        # s.save()
    return HttpResponse(sites)


@api_view(["POST"])
#
# def (height):
#
#     # import pdb
#     # pdb.set_trace()
#     try:
#         height1 = json.loads (height.body)
#         weight = str (height1 * 10)
#         return HttpResponse ("Ideal weight should be:" + weight + " kg")
#     except ValueError as e:
#         return HttpResponse (status.HTTP_400_BAD_REQUEST)
#

def insert_site(request,site_name):

    if Site.objects.filter(site_name=site_name):

       return HttpResponse("error")

    else:
        a=Site.objects.create(site_name=site_name,rd_name="xyz",rd_version="12.0.9")

    # if site_name=="Chennai":

        return HttpResponse(a)

@api_view(["DELETE"])

def delete_site(request,site_name):

    a=Site.objects.filter(site_name=site_name)
    b=a.delete()
    print("deleted site_name is",b.site_name)
    return HttpResponse(b)