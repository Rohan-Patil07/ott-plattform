// alert("upload")
getVideos()
function getVideos(){
    let formData = new FormData();
    formData.append("txtID",$("#txtID").val());
    formData.append(
      "csrfmiddlewaretoken",
      $("input[name=csrfmiddlewaretoken]").val()
    );
    

    $.ajax({
        url: "/get_view_videos/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
        let video = response[0].v_video.substring(3,)
          $("#playvideo").append('<source src="'+video+'" type="video/mp4">')
          $("#video_title").html(response[0].v_title)
          $("#desc").text(response[0].v_desc)
          $('#Genre').text("Genre : " + response[0].v_cat)
          $('#channel_name').text(response[0].v_channel_name)
        }
        
        });
}