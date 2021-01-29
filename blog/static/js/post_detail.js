// function to show all comments
function show_all_comments() {
    //grab all comments with the more-comments class
    var hidden_comments = document.getElementsByClassName("more-comments");
    for (var i = 0; i< hidden_comments.length; i++) {
        //remove the d-none class that hides things
        hidden_comments[i].classList.remove('d-none');
    }
    // hide the show all button
    document.getElementById('show-all-comments').classList.add('d-none');
}