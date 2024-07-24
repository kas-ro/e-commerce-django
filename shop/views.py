from django.shortcuts import render

from shop.models.collection import Collection
from shop.models.product import Product
from shop.models.slider import Slider

def home_view(request):
    template_name = 'shop/index.html'
    sliders = Slider.objects.all()
    collections = Collection.objects.all()
    best_sellers = Product.objects.filter(is_best_seller=True)
    news_arrivals = Product.objects.filter(is_news_arrival=True)
    featured = Product.objects.filter(is_featured=True)
    special_offers = Product.objects.filter(is_special_offer=True)
    context = {
        "sliders": sliders,
        "featured": featured,
        "best_sellers": best_sellers,
        "collections": collections,
        "news_arrivals": news_arrivals,
        "special_offers": special_offers,
    }
    return render(request, template_name, context)
