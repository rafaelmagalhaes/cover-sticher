from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . import collage
from .serializers import CoverSerializer
from .models import Covers
import shutil


def index(request):
    covers = Covers.objects.all()
    return render(request, 'covers/index.html', {'covers': covers})


class CoversViews(CreateAPIView):
    model = Covers
    serializer_class = CoverSerializer
    queryset = Covers.objects.all()

    def perform_create(self, serializer):
        name = self.request.GET['name']
        ibns = self.request.GET['q'].split(',')
        images = collage.createIBNS(ibns)
        collapse_image = collage.create_collage(images, cols=3, rows=2)
        serializer.save(name=name, total_amount=len(ibns), cover_image=collapse_image)
        shutil.rmtree('../static')  # delete folder once collapse image is saved
