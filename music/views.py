from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
import scrap
# Create your views here.

def test(request):
	return render_to_response('index.html')

def alphaSelect(request):
	x = {'y':scrap.alphaSelect}
	return render_to_response("alphaSelect.html" , x)