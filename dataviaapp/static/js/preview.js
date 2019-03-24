

function preview(e) {




    var format_videos = [ "mov", "avi", "ogg", "mp4" , "webm","wmv"];
    var format_image = [ "jpg","png", "bmp", "tiff" ];



    // Look at row has contains file_list to add preview
    var row_to_span = $( "#row-files-preview" );

    var aaa = row_to_span.children('div');

    var children_lenght = row_to_span.children("div").length;

    var button = $(this);


    if ( children_lenght == 1){

        button.textContent = "Close";

        var style_image = "display: flex; text-align:center; position: center;  min-width: 100%; min-height: 100%;";
        var file_to_show ="";


        style_element = " justify-content: center; align-items: center;";


        var name_file = e.parentElement.parentElement.children[2].textContent;


        var extension_file = String(name_file.split(".")[1]).trim(" ");





        if (format_image.includes(extension_file) ){

            file_to_show = '<img src="'+
                name_file+
                '" class="img-responsive" style="' + style_image + '">';
        }else{


            file_to_show = '<video  id = "my-video" class ="video-js" controls preload="auto"   poster="/media/images/imagenes/datavia_logo.png"   data-setup = "{}" style="height:100%; width:100%;" >  <source src = "'+name_file+'"  type = "video/'+extension_file + '"> <p  class ="vjs-no-js"> To view this video please enable   JavaScript, and consider upgrading to a web browser that <a  href = "https://videojs.com/html5-video-support/"  target = "_blank" > supports HTML5  video </a > </p> </video>';

        }

        var   str = "<div id='preview-col' style='background:black' class='col-lg-6' > <h1 class='row justify-content-center text-primary' >Preview</h1>"+
                "<div id='preview-col'  style= "+style_element+">"+
                         file_to_show +
                 " </div></div>";

        html = $.parseHTML( str );
        nodeNames = [];

        // Append the parsed HTML
        row_to_span.append( html );
    }else{
        button.textContent = "View file";
        $('#preview-col').remove();


    }





}

