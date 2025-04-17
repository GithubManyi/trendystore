from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from .forms import ReviewForm

def home(request):
    query = request.GET.get('q', '')
    print("🟢 You searched for:", query)

    category = request.GET.get('category', '')

    # Start with all products
    products = Product.objects.all().order_by('-created_at')

    # Improved Search: match name, description, quality, and category
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(quality_description__icontains=query) |
            Q(category__icontains=query)
        )

    # Filter by category
    if category:
        products = products.filter(category__iexact=category)

    # Weekly Offers, New Arrivals, Discounts (from all products)
    all_products = Product.objects.all()
    weekly_offers = all_products.filter(is_weekly_offer=True)
    new_arrivals = all_products.filter(is_new_arrival=True)
    discounted_products = all_products.filter(is_discounted=True)

    # Pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)

    # Unique categories for dropdown
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        'products': products_page,
        'weekly_offers': weekly_offers,
        'new_arrivals': new_arrivals,
        'discounted_products': discounted_products,
        'categories': categories,
        'query': query,
        'selected_category': category,
    }

    return render(request, 'store/home.html', context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    reviews = product.reviews.all().order_by('-created_at')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('store:product_detail', id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'store/product_detail.html', {
        'product': product,
        'form': form,
        'reviews': reviews,
    })

def about_view(request):
    return render(request, 'store/about.html')

def contact_view(request):
    return render(request, 'store/contact.html')
