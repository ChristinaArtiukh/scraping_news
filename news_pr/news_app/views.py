from django.shortcuts import render, redirect
from django.urls import reverse

from .scraping import scraping_headers_pages, return_name_link_for_page
from .forms import SendURLForm


def home_view(request):
    form = SendURLForm()
    if request.method == 'POST':
        form = SendURLForm(request.POST)
        if form.is_valid():
            form.name = request.POST.get('name')
            name = form.name
        return redirect(reverse('news_page', kwargs={'name': name}))
    context = {
        'page': scraping_headers_pages(),
        'form': form,
    }
    return render(request, 'index.html', context)


def news_page_view(request, name):
    news_list = scraping_headers_pages()
    list_links = []
    for i in news_list:
        links = i['link']
        list_links.append(links)
    for link in list_links:
        link_name = link.split('/')[-1]
        if name == link_name:
            url = link
    context = {
        'page': return_name_link_for_page(url),
    }
    return render(request, 'news_page.html', context)

