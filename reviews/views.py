from django.shortcuts import render


def review_view(request):
    return render(request, 'reviews/review.html')