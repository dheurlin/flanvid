var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// Create the player
let player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        videoId: current_vid_id,
        events: {
            'onReady'       : onPlayerReady,
            'onStateChange' : onStateChange,
        }
    });
}

function onPlayerReady(event) {
    event.target.playVideo();
}

function onStateChange(event) {
    if (event.data === YT.PlayerState.ENDED) {
        loadNextVideo();
    }
}

function loadNextVideo() {
    $.ajax({
        url : next_vid_url,
        type : "POST",
        data : {
            id : current_id,
            csrfmiddlewaretoken : CSRF_TOKEN
        },

        success : function(json) {
            // If another video is in the queue, load it in the player
            if(json.content["has_new_vid"]) {
                current_vid_id = json.content["new_vid_id"];
                current_id = json.content["new_id"];
                player.loadVideoById(current_vid_id);
            // Otherwise, just reload the page to get the default message
            } else {
                location.reload();
            }
        },

        error : function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}
