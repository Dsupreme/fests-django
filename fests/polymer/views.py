from django.shortcuts import render, render_to_response, RequestContext, HttpResponse

# Create your views here.
def index(request):
	context = RequestContext(request,{
								'request': request,
								'user': request.user
							})
	return render_to_response('polymer/index.html',context_instance=context)