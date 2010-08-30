# Create your views here.

def download(request):
    "We need from the post request: username"
    return render_to_response('refuge.downloadegg.html')


