from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    name = models.CharField(max_length=20)#назва міста
    gaming_rooms_count = models.IntegerField()#кількість ігрових кімнат у місті

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
        ordering = ['name']


class GamingConsole(models.Model):
    name = models.CharField(max_length=20)
    generation = models.IntegerField()#покоління консолі
    controllers_count = models.IntegerField(default=1)#кількість геймпадів
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)#ціна за годину

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gaming Console"
        verbose_name_plural = "Gaming Consoles"
        ordering = ['name']


class GamingRoom(models.Model):
    number = models.IntegerField()#номер кімнати в якості назви
    capacity = models.IntegerField(default=1)#кількість можливих гравців на сеансі
    price_per_hour = models.IntegerField()#ціна за годину
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    # consoles = models.ManyToManyField(GamingConsole, related_name='rooms')#консолі, доступні в кімнаті
    def __str__(self):
        return f"Room #{self.number} - Capacity: {self.capacity}"
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ['number']

# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # Користувач, який зробив бронювання
#     gaming_room = models.ForeignKey(GamingRoom, on_delete=models.CASCADE)  # Броньована кімната
#     start_time = models.DateTimeField()  # Дата та час початку бронювання
#     end_time = models.DateTimeField()  # Дата та час завершення бронювання
#     created_at = models.DateTimeField(auto_now_add=True)  # Дата створення бронювання
#     def __str__(self):
#         return f"Booking by {self.user.username} for Room #{self.gaming_room.number}"
#     class Meta:
#         verbose_name = "Booking"
#         verbose_name_plural = "Bookings"
#         ordering = ['start_time']

class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gaming_room = models.ForeignKey(GamingRoom, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room Booking by {self.user.username} for Room #{self.gaming_room.number}"

    class Meta:
        verbose_name = "Room Booking"
        verbose_name_plural = "Room Bookings"
        ordering = ['start_time']

class ConsoleBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gaming_console = models.ForeignKey(GamingConsole, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Console Booking by {self.user.username} for Console {self.gaming_console.name}"

    class Meta:
        verbose_name = "Console Booking"
        verbose_name_plural = "Console Bookings"
        ordering = ['start_time']