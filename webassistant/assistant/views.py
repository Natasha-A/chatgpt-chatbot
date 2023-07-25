from django.shortcuts import render

# Home View
def home(request):
    return render(request, 'assistant/home.html')
  
  
def new_chat(request):
  return render(request, 'assistant/base.html')


# Error View
def error_handler(request):
    return render(request, 'assistant/404.html')
