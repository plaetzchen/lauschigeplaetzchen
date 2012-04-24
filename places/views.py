from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404
from django.shortcuts import render_to_response, redirect
from django import forms
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.conf import settings

from places.models import Place,Comment
from places.forms import PlaceForm,CommentForm
from os.path import join as pjoin
import string, random, os

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

try:
    from PIL import Image, ImageOps
except ImportError:
    import Image
    import ImageOps
    
def index(request):
    places = Place.objects.all()
    return render_to_response('places/index.html',
                            {'object_list': places},
                            context_instance=RequestContext(request))

def detail(request, slug):
    try:
        place = Place.objects.get(slug=slug)
    except Place.DoesNotExist:
        raise Http404
    
    comments = Comment.objects.filter(place=place)
    
    return render_to_response('places/detail.html', { 'object' : place, 'comments' : comments, 'form' : CommentForm() }, context_instance=RequestContext(request))
    
def add_comment(request, slug):
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(place=Place.objects.get(slug=slug))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("places.views.detail", args=(slug,)))
    
def submit(request):

    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES or None)
        if form.is_valid():
                cmodel = form.save()
                if cmodel.image:
                    fn, ext = os.path.splitext(cmodel.image.name)
                    im = Image.open(cmodel.image)
            	    if im.mode not in ("L", "RGB"):
                	    im = image.convert("RGB")
                    im.thumbnail((300,300), Image.ANTIALIAS)
                    th_fl = fn + '_thumb' + ext
                    im.save(settings.MEDIA_ROOT + '/' + th_fl, "JPEG")
                    cmodel.thumb =  th_fl
                
                cmodel.save()

                return redirect(index)

        return render_to_response('places/submit.html',
                                {'contact_form': form},
                                context_instance=RequestContext(request))
    else:
        form = PlaceForm()                            
        return render_to_response('places/submit.html',
                                {'contact_form': form},
                                context_instance=RequestContext(request))
                                
def about(request):
	return render_to_response('places/about.html',
                            context_instance=RequestContext(request))
