from django.contrib import admin

# Register your models here.
from .models import*

admin.site.register(categories)
admin.site.register(commande)
admin.site.register(produit)
admin.site.register(PortfolioProduit)
admin.site.register(PortfolioService)
admin.site.register(PortfolioExperts)
admin.site.register(Reservations)