from django.shortcuts import render, redirect
from django.db.models import Q, Sum
from .forms import PollingUnitResultForm
from .models import AnnouncedPuResults, Lga, PollingUnit


# Create your views here.
def home(request):
    return render(request, "home.html")


def polling_unit_result(request):
    # get the 'q' parameter from the request GET dictionary
    # if it does not exist, set q to an empty string
    if request.GET.get("q") is not None:
        q = request.GET.get("q")
    else:
        q = ""

    # query the AnnouncedPuResults table for the polling unit with the given uniqueid
    polls = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=q)

    # query the PollingUnit table for all polling unit numbers that are not in LGA '0', and order them by polling_unit_id
    polling_unit_number = PollingUnit.objects.exclude(lga_id="0").order_by(
        "polling_unit_id"
    )

    # print the polls queryset for debugging purposes
    print(polls)

    # create a dictionary with the querysets as values and variable names as keys
    context = {
        "polls": polls,
        "polling_unit_number": polling_unit_number,
    }

    # render the poll_result.html template with the context dictionary as an argument
    return render(request, "poll_result.html", context)


def lga_results(request):
    # Retrieve all LGAs from the database
    lgas = Lga.objects.all()

    # Retrieve the selected LGA from the query parameters
    lga_id = request.GET.get("lga_id")

    # Initialize the variable to hold the total results for the selected LGA
    total_results = None

    # If an LGA is selected, retrieve its name, its polling units, and the total results for each party in those polling units
    if lga_id:
        # Retrieve the LGA object with the specified ID
        lga = Lga.objects.get(lga_id=lga_id)

        # Retrieve all polling units in the selected LGA
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)

        # Compute the total results for each party in the polling units of the selected LGA
        total_results = (
            AnnouncedPuResults.objects.filter(polling_unit_uniqueid__in=polling_units)
            .values("party_abbreviation")
            .annotate(total=Sum("party_score"))
            .order_by("-total")
        )
    # Prepare the context to be passed to the template
    if lga_id:
        context = {
            "lga": lga,  # The selected LGA (if any)
            "lgas": lgas,  # All LGAs
            "total_results": total_results,  # The total results for the selected LGA (if any)
        }

    else:
        context = {
            "lgas": lgas,  # All LGAs
            "total_results": total_results,  # The total results for the selected LGA (if any)
        }

    # Render the template and return the resulting HTTP response
    return render(request, "lga_results.html", context)


def add_polling_unit_result(request):
    if request.method == "POST":
        form = PollingUnitResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PollingUnitResultForm()

    context = {"form": form}

    return render(request, "add_polling_unit_result.html", context)
