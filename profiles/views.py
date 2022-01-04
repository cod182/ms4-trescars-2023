from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ Shows User Profile"""

    request.session['vehicle_bag'] = {}
    user_profile = get_object_or_404(UserProfile, user=request.user)

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'profile': user_profile,
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
