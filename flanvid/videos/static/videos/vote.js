const VID_LIST_REFRESH_TIMEOUT = 10000;


function voteForVid(vidID, voteType) {
    $.ajax({
        url : ajaxUrl,
        type : "POST",
        data : {
            id   : vidID,
            type : voteType,
            user : 'sagge',
            csrfmiddlewaretoken : CSRF_TOKEN
        },

        success : function(json) {
            console.log(json);
            getVidList();
        },

        error : function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}

// Gets the list of videos, and puts it in the correct
// spot on the page
function getVidList() {
    $.ajax({
        url : vidListUrl,
        type : "GET",
        data : { },

        success : function(json) {
            $("#submitted_videos").html(json);
            bindVoteButtons();
        },

        error : function(xhr, errmsg, err) {
            $("#submitted_videos").html('<p>Something went wrong, videos could not be loaded...</p>')
        }
    });
}

function bindVoteButtons() {

    $button = $("a.vid-vote-btn");
    $button.unbind("click");

    $button.click(function(e) {

        e.preventDefault();
        voteForVid($(this).attr("data-for-vid"),  $(this).attr("data-vote-type"));
    });
}

$(function() {

    // Get the list of videos as soon as the page loads,
    // then reload it every x seconds
    getVidList();
    setInterval(getVidList, VID_LIST_REFRESH_TIMEOUT);

});
