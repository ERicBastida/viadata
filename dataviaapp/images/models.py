from django.db import models
from django.core.validators import  FileExtensionValidator
from django.urls import reverse
# Create your models here.
class Files(models.Model):

    image_formats = ["png", "tiff","bmp"]
    video_formats = ["ogg","webm","mp4","wmv","avi"]


    # imagen = models.FileField(upload_to='images/imagenes/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file',)
    imagen = models.FileField(upload_to='images/imagenes/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','OGG','WEBM','MP4'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif ,.tiff , .bmp , .webm , .ogg , .mp4 ', verbose_name='file',)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name = string.split('.')[0]
        return name

    def is_image(self):
        result = False
        if self.extension() in self.image_formats:
            result = True
        return result

    def is_video(self):
        result = False
        if self.extension() in self.video_formats:
            result = True
        return result

    def extension(self):
        string = str(self.imagen)
        name = string.split('.')[1]
        return name
    def delete(self, *args, **kwargs):
    
        self.imagen.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

class Files2(models.Model):


    imagen2 = models.FileField(upload_to='images/imagenes2/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file2',)
    timestamp2 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name2 = string.split('.')[0]
        return name2

    def delete(self, *args, **kwargs):
        
        self.imagen2.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File2'
        verbose_name_plural = 'Files2'

class Files3(models.Model):


    imagen3 = models.FileField(upload_to='images/imagenes3/', validators= [ FileExtensionValidator(['BMP','PNG','TIF','TIFF','MP4','AVI','MOV','WMV'], 'The image was not uploaded:invalid format')], help_text='Introduce only format images .png , .tif , .avi , .wmv , .mp4 , .tiff or .bmp ', verbose_name='file3',)
    timestamp3 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        string = str(self.imagen)
        name3 = string.split('.')[0]
        return name3

    def delete(self, *args, **kwargs):
        
        self.imagen3.delete()
        super().delete(*args, **kwargs)


    class Meta:
        verbose_name = 'File3'
        verbose_name_plural = 'Files3'


# Author : Eric Bastida
# Contact: eribastida@gmail.com - Date:
# Date: 23 March 2019




from .views import *


class PreviewFiles(models.Model):
    "Clase encargada de obtener los archivos compatibles para ser previsualizados."

    UNSUPPORT_FORMAT_MESSAGE = "Incompatible Format."
    CONTENT_HTML = ""
    FILE = None
    FILE_ID = 0


    def Files_Preview(self,request,pk):
        self.FILE_ID = pk
        print("vamooooos biiiien ----> ")
        pass

    def view_web_file(self, id):
        "Muestra el archivo en el formato web correspondiente para ser insertado directamente en la pagina"

        try:
            self.FILE = Files.objects.get(pk=id)

            style_image = """
                            position: fixed; 
                            top: 0; 
                            left: 0; 

                            /* Preserve aspet ratio */
                            min-width: 100%;
                            min-height: 100%;
                        """

            name_file = "/media/" + self.FILE.__str__() + "." + self.FILE.extension()

            resultado = "Incompatible Format."
            print("-----> ", name_file)
            if self.FILE.is_image() == True:

                resultado = '<img src="' + name_file + '" class="img-responsive" style="' + style_image + '";">'
            elif self.FILE.is_video():
                resultado = '<video   controls   autoplay > <source   src = "' + name_file + '"   type = "video/' + self.FILE.extension() + '" > </source > </video >'

                # resultado = '<head> <link href="https://vjs.zencdn.net/7.4.1/video-js.css" rel="stylesheet"><script src="https://vjs.zencdn.net/ie8/ie8-version/videojs-ie8.min.js"></script></head><body><video  id = "my-video" class ="video-js" controls preload="auto" width="640" height="264"   poster="/media/images/imagenes/datavia_logo.png"   data-setup = "{}">  <source src = "'+name_file+'"  type = "video/'+self.FILE.extension() + '"> <p  class ="vjs-no-js"> To view this video please enable   JavaScript, and consider upgrading to a web browser that <a  href = "https://videojs.com/html5-video-support/"  target = "_blank" > supports HTML5  video </a > </p> </video><script    src = "https://vjs.zencdn.net/7.4.1/video.js" ></script></body >'

        except:

            return None

        return resultado



        