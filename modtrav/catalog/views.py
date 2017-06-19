from django.shortcuts import render

from .models import Tag, Location, Activity

# Create your views here.
def index(request):
    '''
    View function for the homepage of the site.
    '''
    # Generate counts of the main objects
    num_activities = Activity.objects.all().count()
    num_locations = Location.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_activites':num_activites,'num_locations':num_locations},
    )
