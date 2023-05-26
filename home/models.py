from django.db import models

from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField


class Carousel(blocks.StructBlock):
    image = ImageChooserBlock()
    text = blocks.RichTextBlock()

class HomePage(Page):
    
    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, default='Welcome to my homepage!')
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
        )

    body = StreamField([
        # ('name', blocks.SomethingBlock()),
        ('heading', blocks.CharBlock(template="heading_block.html")),
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('carousel', Carousel()),
    ], use_json_field=True, null=True)

    content_panels = Page.content_panels + [
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            FieldPanel("banner_image"),
            FieldPanel("body"),
    ]