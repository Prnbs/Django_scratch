from django.shortcuts import render
from links_everywhere.models import User, URL, Tags
from links_everywhere.forms import AddLinkForm, SaveLinkForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def get_my_url(request):
    username = request.user.username
    saved_links = {}
    users = User.objects.get(email=username)
    urls = users.url.all()
    urls_and_tags = []
    saved_links['add_link'] = AddLinkForm()
    for url in urls:
        my_urls_tagged = {}
        my_urls_tagged['url'] = url.url
        print(my_urls_tagged['url'])
        tags = url.tags.all()
        this_urls_tags = []
        for tag in tags:
            this_urls_tags.append(tag)
        my_urls_tagged['tags'] = this_urls_tags
        urls_and_tags.append(my_urls_tagged)
    saved_links['tags_and_urls'] = urls_and_tags
    return render(request, 'users_links.html', {'saved_links': saved_links})


@login_required
def get_my_tags(request):
    '''
    Gets the tags associated with an url
    :param request:
    :return:
    '''
    errors = []
    form = AddLinkForm(request.GET)
    empty_save_form = SaveLinkForm()
    if form.is_valid():
        cd = form.cleaned_data
        url = cd['link']
        if not url:
            return render(request, 'add_links.html', {'form':empty_save_form})
        else:
            urls = URL.objects.filter(url=url)
            unique_tags = set()
            for url in urls:
                tags = url.tags.all()
                for tag in tags:
                    unique_tags.add(str(tag))
            data = {'link': url, 'tags': ",".join(unique_tags) }
            save_form = SaveLinkForm(initial=data)
            return render(request, 'add_links.html', {'form':save_form})
    else:
        return render(request, 'add_links.html', {'form':empty_save_form})


@login_required
def get_related_url(request, tags_input):
    '''
    For a given tag return all the User's links which match that tag
    :param request:
    :return:
    '''
    tags = str(tags_input)
    if tags is not None:
        mail_id = request.user.email
        input_tag = tags
        user = User.objects.get(email=mail_id)
        urls = user.url.all()
        tagged_urls = set()
        for url in urls:
            tags = url.tags.all()
            for tag in tags:
                if str(tag) == input_tag:
                    tagged_urls.add(url)
        return render(request, 'search_tag.html', {'tagged_url':tagged_urls})
    else:
        return render(request, 'search_tag.html')


@login_required
def save_url(request):
    '''
    Save the url and it's tags
    :param request:
    :return:
    '''
    form = SaveLinkForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = User.objects.get(email=request.user.username)
        try:
            # if this user already has this url then get it
            url = user.url.get(url=cd['link'])
        except:
            url = URL.objects.create(url=cd['link'])
        tags_list = cd['tags'].strip().split(',')
        for tag in tags_list:
            tag = tag.strip()
            try:
                # if the Tag table already has this tag then reuse it
                tag = Tags.objects.get(tags=tag)
            except:
                tag = Tags.objects.create(tags=tag)
            url.tags.add(tag)
        user.url.add(url)

    return HttpResponseRedirect("/links/getmyurl/")





