from django.shortcuts import redirect
from django.http import JsonResponse

from .view_helper import initiate_item_collection_service
from .forms import AddToCartForm, AddToWishlistForm

import json


def delete_button_cart(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == 'PUT':
        data = json.load(request)
        service = initiate_item_collection_service(request)
        response, status = service.delete_button_item_collection_service(data, "Cart")
        JsonResponse(response, status=status)

    return redirect('home')

def delete_button_wishlist(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    if is_ajax and request.method == 'PUT':
        data = json.load(request)
        service = initiate_item_collection_service(request)
        response, status = service.delete_button_item_collection_service(data, "Wishlist")
        return JsonResponse(response, status=status)

    return redirect('home')

def add_to_wishlist(request):
    if request.method == 'PUT' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = json.loads(request.body.decode('utf-8'))
        service = initiate_item_collection_service(request)
        response, status = service.add_to_item_collection(data, "Wishlist")
        return JsonResponse(response, status=status)

    return JsonResponse({"status": "error", "message": "Invalid data"})

def add_to_cart(request):
    if request.method == 'PUT' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = json.loads(request.body.decode('utf-8'))
        service = initiate_item_collection_service(request)
        response, status = service.add_to_item_collection(data, "Cart")
        return JsonResponse(response, status=status)

    return JsonResponse({"status": "error", "message": "Invalid data"})
