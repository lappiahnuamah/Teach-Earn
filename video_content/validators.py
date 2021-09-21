from django.core.exceptions import ValidationError



def file_size(value):
    filesize = value.size
    if filesize > 419430400:
        raise validationError("Maximum size is 50 megabyte. Upload a lesser size!!")