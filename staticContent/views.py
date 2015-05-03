from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from staticContent.models import StaticContent
from staticContent.forms import EditStaticContentForm

def static_content_view(request, pk):
    c = get_object_or_404(StaticContent, pk=pk)
    try :
        f = request.GET['f']
    except :
        f = ''
    return render(request, 'staticContent/staticContent.html', { 'content' : c.content,
                                                    'from' : f, 
                                                    'num':c.pk, 
                                                    'style':c.style,
                                                    'title':c.title})
def static_content_style_view(request, pk):
    c = get_object_or_404(StaticContent, pk=pk)
    return HttpResponse(c.style, content_type='text/plain')

@login_required(login_url='/member/login/')
def edit_static_content(request, pk=0):
    if request.method == 'POST':
        form = EditStaticContentForm(request.POST, request.FILES)
        if form.is_valid():
            author = request.user.member
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            style = form.cleaned_data['style']
            if pk==0:
                page = StaticContent(author=author, title=title, content=content, style=style)
                page.save()
            else:
                page = get_object_or_404(StaticContent, pk=pk)
                page.author = author
                page.title = title
                page.content = content
                page.style = style
                page.save()
            return HttpResponseRedirect('/member/static_pages/')
    else:
        if pk==0:
            form = EditStaticContentForm()
        else:
            page = get_object_or_404(StaticContent, pk=pk)
            form = EditStaticContentForm(initial={  'title':page.title,
                                                    'content':page.content,
                                                    'style':page.style,})
    if pk == 0:
        send_to = '/staticcontent/new/'
    else :
        send_to = '/staticcontent/' + pk + '/edit/'
    return render(request, 'staticContent/edit.html', locals())