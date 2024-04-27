from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView

from accounts.models import Profile
from config.custom_permissions import OnlyLoggedSuperUser
from .models import Resource, HomeModel, Location
from .forms import ContactForm


def error_404_view(request, exception):
    return render(request, 'app/404_error.html')


def news_list(request):
    news_list = Resource.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "app/news_list.html", context)


class NewsUpdtaeView(OnlyLoggedSuperUser, UpdateView):
    model = Resource
    fields = ('title', 'author', 'body', 'DocumentFile', 'TestLink', 'CrosswordLink', 'YoutubeLink', 'status',)
    template_name = 'crud/news_edit.html'
    success_url = reverse_lazy('home_list')


class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = Resource
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_list')


class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = Resource
    template_name = 'crud/news_create.html'
    fields = ('title', 'body', 'DocumentFile', 'TestLink', 'CrosswordLink', 'YoutubeLink', 'status',)
    success_url = reverse_lazy('home_list')


@login_required(login_url='login')
def news_detail(request, news):
    news = get_object_or_404(Resource, slug=news, status=Resource.Status.Published)
    context = {
        "news": news
    }
    return render(request, 'app/news_detail.html', context)


def homePageView(request):
    news_list = HomeModel.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, 'app/index.html', context)


# def ContactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bog'langaningiz uchun rahmat</h2>")
#     context = {
#         "form": form,
#     }
#     return render(request, 'app/contact.html', context)
class ContactPageView(TemplateView):
    templates_name = 'app/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, "app/contact.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return redirect('home_list')
        context = {
            'form': form
        }
        return render(request, 'app/contact.html', context)


def CalendarPageView(request):
    return render(request, 'app/calendar.html')


class LocationView(TemplateView):
    template_name = 'app/location.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_location'] = Location.objects.first()
        return context


def search_view(request):
    query = request.GET.get('q')
    results = Resource.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query) | Q(author__icontains=query)
    )

    if not results:
        return render(request, 'app/no_results.html', {'query': query})
    else:
        return render(request, 'app/search_results.html', {'all_theme': results, 'query': query})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def admin_page(request):
    admin_users = User.objects.filter(is_superuser=True)
    users = User.objects.filter(is_superuser=False)
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None
    context = {
        'profile': profile,
        "admin_users": admin_users,
        "users": users,
    }
    return render(request, 'pages/admin_page.html', context)
