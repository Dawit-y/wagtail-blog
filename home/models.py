from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1

    body = RichTextField(blank = True)

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], )
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name= "+")
    banner_cta = models.ForeignKey("wagtailcore.Page", null=True, blank=False, on_delete=models.SET_NULL, related_name= "+")

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta"),
    ]

