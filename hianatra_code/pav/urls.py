from django.urls import path

from .import views

urlpatterns = [
   path('',views.homeView,name="home"),
   path('boutique/',views.VueBoutiqueView, name="boutique"),
   path('portfolio',views.portfolioView,name='portfolio'),
   path('portfoliocreate/',views.PortfoliocreateView,name='portfoliocreate'),
   #path('portfolioForm/',views.PortfolioformView,name='portfolioForm')
]

