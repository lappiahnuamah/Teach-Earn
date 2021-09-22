from django.core.exceptions import  ValidationError



def file_size(value):
    filesize = value.size
    if filesize >419430400:
        raise ValidationError("Maximum size is  400 Megabyte")
         