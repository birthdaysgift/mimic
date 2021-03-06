$('.detail-video-background').click(function(event) {
    event.stopPropagation();
    $('.detail-video-background').remove();
});

$('.detail-video-window').click(function(event) {
    event.stopPropagation();
})

// =======================LIKE/DISLIKE==========================================

function setLike(elem) {
    var likeIcon = $(elem).find('.like-icon');
    if (!likeIcon.hasClass('like-selected')) {
        likeIcon.addClass('like-selected');
        var likeValue = $(elem).find('.like-value');
        var value = parseInt(likeValue.text());
        if (isNaN(value))
            value = 0;
        value++;
        if (value === 0)
            value = '';
        likeValue.text(value);
    }
}

function clearLike(elem) {
    var likeIcon = $(elem).find('.like-icon');
    if (likeIcon.hasClass('like-selected')) {
        likeIcon.removeClass('like-selected');
        var likeValue = $(elem).find('.like-value');
        var value = parseInt(likeValue.text());
        if (isNaN(value))
            value = 0;
        value--;
        if (value === 0)
            value = '';
        likeValue.text(value);
    }
}

function setDislike(elem) {
    var dislikeIcon = $(elem).find('.dislike-icon');
    if (!dislikeIcon.hasClass('dislike-selected')) {
        dislikeIcon.addClass('dislike-selected');
        var dislikeValue = $(elem).find('.dislike-value');
        var value = parseInt(dislikeValue.text());
        if (isNaN(value))
            value = 0;
        value++;
        if (value === 0)
            value = '';
        dislikeValue.text(value);
    }
}

function clearDislike(elem) {
    var dislikeIcon = $(elem).find('.dislike-icon');
    if (dislikeIcon.hasClass('dislike-selected')) {
        dislikeIcon.removeClass('dislike-selected');
        var dislikeValue = $(elem).find('.dislike-value');
        var value = parseInt(dislikeValue.text());
        if (isNaN(value))
            value = 0;
        value--;
        if (value === 0)
            value = '';
        dislikeValue.text(value);
    }
}

$('.like').click(function(event) {
    var url = $(event.currentTarget).find('.like-link').attr('href');
    console.log(url);
    $.get({
        url: url
    });
    var likeIcon = $(event.currentTarget).find('.like-icon');
    var dislike = $(event.currentTarget).siblings('.dislike');
    if (likeIcon.hasClass('like-selected')) {
        clearLike(event.currentTarget);
    } else {
        setLike(event.currentTarget);
        clearDislike(dislike);
    }
});

$('.dislike').click(function(event) {
    var url = $(event.currentTarget).find('.dislike-link').attr('href');
    $.get({
        url: url
    });
    var dislikeIcon = $(event.currentTarget).find('.dislike-icon');
    var like = $(event.currentTarget).siblings('.like');
    if (dislikeIcon.hasClass('dislike-selected')) {
        clearDislike(event.currentTarget);
    } else {
        setDislike(event.currentTarget);
        clearLike(like);
    }
})

//=========================END=LIKE/DISLIKE=====================================
