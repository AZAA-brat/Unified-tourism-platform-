from django.db import models

class Region(models.Model):
    name = models.CharField("Name of the Region", max_length=100)

    class Meta:
        verbose_name = "Regions"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name

class Hotel(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.PROTECT,
        related_name="hotels"
    )
    name = models.CharField("Name of the hotel", max_length=100)
    description = models.TextField("Description")
    email = models.EmailField()
    link = models.URLField(blank=True)
    min_price = models.DecimalField("Minimal price of staying per day(in soms)", max_digits=20, decimal_places=2)
    working_hours = models.SlugField("Working hours")
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Hotel"
        verbose_name_plural = "Hotels"

    def __str__(self):
        return self.name

class Address(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.PROTECT,
        related_name="address"
    )
    address = models.CharField("Address:", max_length=100)

    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return self.address

class Phone(models.Model):
    LABELS = [
        ("reception", "Reception"),
        ("reservation", "Reservation"),
    ]
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.PROTECT,
        related_name="phones"
    )
    label = models.CharField(max_length=30, choices=LABELS)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.phone_number

class Photo(models.Model):
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.PROTECT,
        related_name="photos"
    )
    photos = models.ImageField(upload_to="hotels/")
    caption = models.CharField("Caption:", max_length=30)

    def __str__(self):
        return self.caption