from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
#from league_manager.models import Author,Book
from league_manager.models import player
from league_manager.models import ref_roster
from league_manager.models import ref_roster_line
from league_manager.models import ref_skills
from league_manager.models import xp_rolls
from league_manager.models import team
from league_manager.models import league
from league_manager.models.general_post import GeneralPost
from league_manager.models.pages.general_page import GeneralPage
from league_manager.models.coach import Coach
from league_manager.models.club import Club
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

#author_extra_fieldsets = ((None, {"fields": ("dob",)}),)

#class BookInline(admin.TabularInline):
#    model = Book.Book
#
#class AuthorAdmin(PageAdmin):
#    inlines = (BookInline,)
#    fieldsets = deepcopy(PageAdmin.fieldsets) + author_extra_fieldsets
#
admin.site.register(league.League)
admin.site.register(GeneralPost)

admin.site.register(Coach)
admin.site.register(GeneralPage)
admin.site.register(Club)