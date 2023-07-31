from django.shortcuts import render, redirect
import openai
from .secret_key import API_KEY
from assistant import controller 

openai.api_key = API_KEY

# Home View
def home(request):
    try:
        # if the session does not have a messages key, create one
        if 'messages' not in request.session:
          controller.initializeSession(request)

        if request.method == 'POST':
            response, temperature = controller.retrieveUserInput(request)
            controller.formatResponse(request, response)
            
            context = controller.createContext(request, temperature)

            return render(request, 'assistant/home.html', context)
        else:
            # if the request is not a POST request, render the home page
            context = controller.createContext(request)

            return render(request, 'assistant/home.html', context)
    except Exception as e:
        print(e)
        # if there is an error, redirect to the error handler
        return redirect('error_handler')

# this is called when the user clicks the "New Chat+" button.
def new_chat(request):
    # clear the messages list
    request.session.pop('messages', None)
    return redirect('home')


# this is the view for handling errors
def error_handler(request):
    return render(request, 'assistant/404.html')
