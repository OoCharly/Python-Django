from django.shortcuts import render

def handler404(request, exception=None):
	return render(request, 'errors/404.html', {'error': exception}, status=404)

def handler500(request, exception=None):
	return render(request, 'errors/500.html', {'error': exception}, status=500)