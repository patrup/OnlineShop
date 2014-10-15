from django.db import models


class Adresse(models.Model):
    strasse = models.CharField(max_length=30)
    hausnummer = models.CharField(max_length=10)
    plz = models.CharField(max_length=10)
    ort = models.CharField(max_length=30)
    land = models.CharField(max_length=30)
    telefon = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.title
    
    
class Lieferant(models.Model):
    name = models.CharField(max_length=100)
    adresse = models.ForeignKey(Adresse, null=True)
    kurzbeschreibung = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adresse = models.ForeignKey(Adresse, null=True)
    nutzername = models.CharField(max_length=20)
    passwort = models.CharField(max_length=12)
    administrator = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    
class Artikel(models.Model):
    bezeichnung = models.CharField(max_length=100)
    kurzbeschreibung = models.CharField(max_length=200)
    detailbeschreibung = models.TextField(blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    bild = models.ImageField(null=True, blank=True)
    gewicht = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    vorrat = models.IntegerField(blank=True)
    lieferant = models.ForeignKey(Lieferant, null=True, blank=True)
    
    def __str__(self):
        return self.bezeichnung
    
    
class Warenkorb(models.Model):
    artikel = models.ForeignKey(Artikel, null=True)
    anzahl = models.IntegerField(max_length=5)
    kunde = models.ForeignKey(Person, null=True)
    
    
class Vorauskasse(models.Model):
    kunde = models.ForeignKey(Person, null=True) 
     
     
class Kreditkarte(models.Model):
    karte = models.CharField(max_length=20)
    kartennummer = models.BigIntegerField(max_length=16)
    expDatum = models.DateField()
    
    
class Bankeinzug(models.Model):
    iban = models.CharField(max_length=30)
    bic = models.CharField(max_length=12)
     

class Rechnung(models.Model):
    kunde = models.ForeignKey(Person, null=True)

     
class Kasse(models.Model):
    bezahlt = models.BooleanField(default=False)
