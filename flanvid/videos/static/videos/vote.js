
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
        },

        error : function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
}

$("a.vid-vote-btn").click(function(e) {
    e.preventDefault();
    voteForVid($(this).attr("data-for-vid"),  $(this).attr("data-vote-type"));
});
