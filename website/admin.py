from django.contrib import admin
from website import models
# Register your models here.

# Register the Hero model
class HeroAdmin(admin.ModelAdmin):
    list_display = ('hero_title', 'hero_position', 'hero_bgimage')
    search_fields = ('hero_title', 'hero_position')

admin.site.register(models.Hero, HeroAdmin)

# Register the About model
class AboutAdmin(admin.ModelAdmin):
    list_display = ('about_title', 'about_birthday', 'about_mobile', 'about_city', 'about_age')
    search_fields = ('about_title', 'about_email')

admin.site.register(models.About, AboutAdmin)

# Register the Skills model


admin.site.register(models.Skills)

# Register the Resume model
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('resume_summary', 'education_title', 'education_year', 'project_name')
    search_fields = ('resume_summary', 'project_name')

admin.site.register(models.Resume, ResumeAdmin)

# Register the Portfolio model
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('app_title', 'product_title', 'gallery_title')
    search_fields = ('app_title', 'product_title', 'gallery_title')

admin.site.register(models.Portfolio, PortfolioAdmin)

# Register the Testimonials model
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_position', 'client_review')
    search_fields = ('client_name', 'client_position')

admin.site.register(models.Testimonials, TestimonialsAdmin)

# Register the Contact model
class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_address', 'contact_mobile', 'contact_email')
    search_fields = ('contact_address', 'contact_email')

admin.site.register(models.Contact, ContactAdmin)
