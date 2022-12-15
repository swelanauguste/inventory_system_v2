from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name.upper()


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name.upper()


class Equipment(models.Model):
    GRN = "Ground"
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    
    FLOOR_LIST = (
        (GRN, "Ground"),
        (FIRST, "1st"),
        (SECOND, "2nd"),
        (THIRD, "3rd"),
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="equipment_list"
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="manufacturer_list",
        null=True,
    )
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    user_section = models.CharField(max_length=100, null=True)
    floor = models.CharField(max_length=100, choices=FLOOR_LIST)
    office = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "equipment"

    def __str__(self):
        return self.name


class Ink(models.Model):
    printer = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="ink_list",
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=100, unique=True)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "ink"

    def __str__(self):
        return self.name
