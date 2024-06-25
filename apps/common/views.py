from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView, ListView, DetailView
from apps.common import models


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context["announcement"] = models.EventsAnnouncements.objects.first()
        context["announcement"] = models.EventsAnnouncements.objects.latest('created_at')

        context["carousel"] = models.Carousel.objects.all()
        context["gallery"] = models.Gallery.objects.all().order_by("-id")[:3]

        # context["event"] = models.EventsEvents.objects.first()
        context["event"] = models.EventsEvents.objects.latest('created_at')


        return context


class AboutConfederationView(TemplateView):
    template_name = "about_confederation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["confederation"] = models.AboutConfederation.objects.first()

        return context


class AboutGuidesView(TemplateView):
    template_name = "about_guides.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["guides"] = models.AboutGuides.objects.first()

        return context


class AboutDocumentsView(TemplateView):
    template_name = "about_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.AboutDocuments.objects.all()

        return context


class AboutRegulationsView(TemplateView):
    template_name = "about_regulations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.AboutRegulations.objects.all()

        return context


class AboutSymbolsView(TemplateView):
    template_name = "about_symbols.html"


class AboutMembershipView(TemplateView):
    template_name = "about_membership.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["membership"] = models.AboutMembership.objects.first()

        return context


class CompetitonCalendarsView(TemplateView):
    template_name = "competition_calendars.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitonCalendars.objects.all()

        return context


class CompetitionReportsView(TemplateView):
    template_name = "competition_reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitionReports.objects.all()

        return context


class CompetitionDocumentsView(TemplateView):
    template_name = "competition_documents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.CompetitionDocuments.objects.all()

        return context


class KurashHistoryView(TemplateView):
    template_name = "kurash_history.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["history"] = models.KurashHistory.objects.first()
        return context


class KurashRulesView(TemplateView):
    template_name = "kurash_rules.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rules"] = models.KurashRules.objects.first()
        return context


class KurashProvisionsView(TemplateView):
    template_name = "kurash_provisions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["documents"] = models.KurashProvisions.objects.all()

        return context


class EventsAnnouncementsListView(ListView):
    model = models.EventsAnnouncements
    template_name = "events_announcements.html"
    context_object_name = "announcements"


class EventsEventsListView(ListView):
    model = models.EventsEvents
    template_name = "events_events.html"
    context_object_name = "events"


class EventsAnnouncementsDetailView(DetailView):
    model = models.EventsAnnouncements
    template_name = "events_announcements_detail.html"
    context_object_name = "events_announcements_detail"


class EventsAboutUsView(ListView):
    model = models.EventsAboutUs
    context_object_name = "events_about_us"
    template_name = "events_about_us.html"


class ContactsView(TemplateView):
    template_name = "contacts.html"


class GalleryPhotoListView(ListView):
    model = models.GalleryPhoto
    context_object_name = "gallery_photo"
    template_name = "gallery_photo.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery_photo = self.get_queryset()
        paginator = Paginator(gallery_photo, self.paginate_by)

        page = self.request.GET.get("page")
        try:
            gallery_photo = paginator.page(page)
        except PageNotAnInteger:
            gallery_photo = paginator.page(1)
        except EmptyPage:
            gallery_photo = paginator.page(paginator.num_pages)

        context["gallery_photo"] = gallery_photo
        return context


class GalleryVideoListView(ListView):
    model = models.GalleryVideo
    context_object_name = "gallery_video"
    template_name = "gallery_video.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery_video = self.get_queryset()
        paginator = Paginator(gallery_video, self.paginate_by)

        page = self.request.GET.get("page")
        try:
            gallery_video = paginator.page(page)
        except PageNotAnInteger:
            gallery_video = paginator.page(1)
        except EmptyPage:
            gallery_video = paginator.page(paginator.num_pages)

        context["gallery_video"] = gallery_video
        return context
