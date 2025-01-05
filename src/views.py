from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def recycler(request):
    template = loader.get_template("src.html")
    context = {
        "stn": {
            "name": "Vingåkersplan 12",
            "id": "16102",
            "next_clean_up": "2025-01-07",
            "last_clean_up": "2025-01-02",
        }
    }
    return HttpResponse(template.render(context=context, request=request))
