// alert("upload")
getVideos()
function getVideos(){
    let formData = new FormData();
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    

    $.ajax({
        url: "/get_videos/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
          for(let i = 0; i < response.length; i++) {
              let lclImage = response[i].v_image.substring(3,);
            $("#videos").append('<div class="card"> <article class="video-container"> <a href="/view1page?q='+response[i].v_id+'" class="thumbnail"> <img class="thumbnail-image" src="'+lclImage+'" height="100"/> </a> <div class="video-bottom-section"> <a href="/channelview/"> <img class="channel-icon" src="http://unsplash.it/36/36?gravity=center"/> </a> <div class="video-details"> <a href="/view1page?q='+response[i].v_id+'" class="video-title">'+response[i].v_title+'</a> <div class="video-metadata"> <span>'+response[i].v_views+' views</span>  <span></span> </div></div></div></article> </div>');
          }
        }
        
        });
}
