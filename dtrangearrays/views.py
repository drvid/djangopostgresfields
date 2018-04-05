from django.http import HttpResponse
from .models import DateTimeRangeArray


def index(request):
    qs = DateTimeRangeArray.objects.all().values('durations')
    return HttpResponse(str(qs), content_type="text/plain") 