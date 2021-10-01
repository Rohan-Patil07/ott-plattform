
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
          alert("Uploaded")
        }
        
        });
}

