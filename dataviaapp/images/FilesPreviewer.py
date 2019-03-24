# Author : Eric Bastida
# Contact: eribastida@gmail.com - Date:
# Date: 23 March 2019

import vlc, easygui, os


from .views import *


class Files_Preview:
    "Clase encargada de obtener los archivos compatibles para ser previsualizados."

    UNSUPPORT_FORMAT_MESSAGE = "Incompatible Format."
    CONTENT_HTML = ""
    FILE = None

    def Files_Preview(self):
        pass

    def view_web_file(self,id):
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

            if self.FILE.is_image() == True:


                resultado = '<img src="' + name_file + '" class="img-responsive" style="' + style_image + '";">'
            elif self.FILE.is_video():
                # resultado = '<video   controls   autoplay > <source   src = "' + name_file + '"   type = "video/' + self.FILE.extension() + '" > </source > </video >'

                resultado = '<head> <link href="https://vjs.zencdn.net/7.4.1/video-js.css" rel="stylesheet"><script src="https://vjs.zencdn.net/ie8/ie8-version/videojs-ie8.min.js"></script></head><body><video  id = "my-video" class ="video-js" controls preload="auto"   poster="/media/images/imagenes/datavia_logo.png"   data-setup = "{}">  <source src = "'+name_file+'"  type = "video/'+self.FILE.extension() + '"> <p  class ="vjs-no-js"> To view this video please enable   JavaScript, and consider upgrading to a web browser that <a  href = "https://videojs.com/html5-video-support/"  target = "_blank" > supports HTML5  video </a > </p> </video><script    src = "https://vjs.zencdn.net/7.4.1/video.js" ></script></body >'

        except:

            return None


        return resultado



