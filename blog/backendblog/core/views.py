from django.shortcuts import render, HttpResponse

html_base = '''
<h1>My personal web</h1>
<hr>

<ul>
    <li>
        <a href="/">Home</a>
    </li>
    <li>
        <a href="/about">About me</a>
    </li>
</ul>
'''

# Create your views here.
def home(request):
    html_response = f'{html_base} <h2>Home</h2>'
    return HttpResponse(html_response)

def about(request):
    html_response = f'{html_base} <h2>About me</h2>'
    return HttpResponse(html_response)