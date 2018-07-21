from django.db import models


class People(models.Model):
    """
    Model describing people table structure
    """

    name = models.CharField(max_length=150, help_text='Enter the name (e.g. Christopher Nolan)')
    birth_date = models.CharField(max_length=50, help_text='Use the following format: dd/mm/yyyy', null=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Studio(models.Model):
    """
    Model describing studio table structure
    """

    name = models.CharField(max_length=150, help_text='Enter the name (e.g. Warner Bros)')
    city = models.CharField(max_length=150, help_text='Enter the city name (e.g. Los Angeles)')

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

# class Film(models.Model):
#     """
#     Class representing the Film Model
#     """

#     title = models.CharField(max_length=255, blank = False)
#     studio = models.OneToOneField(Studio, on_delete=models.SET_NULL, null=True)
#     release_date = models.CharField(max_length=30)
#     director = models.CharField(max_length=80)
#     actors = models.ForeignKey(People, on_delete=models.SET_NULL, null=True)