from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as filters
import core.models
import core.filters
import core.serializers


class SmallPaginator(PageNumberPagination):
    page_size = 5


class MovieViewSet(viewsets.ModelViewSet):
    queryset = core.models.Movie.objects.all().order_by("id")
    serializer_class = core.serializers.MovieSerializer
    pagination_class = SmallPaginator
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = core.filters.MovieFilter


class JobViewSet(viewsets.ModelViewSet):
    queryset = core.models.Job.objects.all().order_by("id")
    serializer_class = core.serializers.JobSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = core.filters.JobFilter
    pagination_class = SmallPaginator


class GenreViewSet(viewsets.ModelViewSet):
    queryset = core.models.Genre.objects.all().order_by("id")
    serializer_class = core.serializers.GenreSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = core.filters.GenreFilter
    pagination_class = SmallPaginator


class PersonViewSet(viewsets.ModelViewSet):
    queryset = core.models.Person.objects.all().order_by("id")
    serializer_class = core.serializers.PersonSerializer
    pagination_class = SmallPaginator
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = core.filters.PersonFilter


class MoviePersonViewSet(viewsets.ModelViewSet):
    queryset = core.models.MoviePerson.objects.all().order_by("id")
    serializer_class = core.serializers.MoviePersonSerializer
    pagination_class = SmallPaginator
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = core.filters.MoviePersonFilter


class HomeTemplateView(TemplateView):
    template_name = "home.html"
