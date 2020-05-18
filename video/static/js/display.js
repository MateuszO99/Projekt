function display() {
    var posts = document.getElementsByClassName("post");
    posts[0].style["display"] = "block";
}


function change_display(id){
    var posts = document.getElementsByClassName("post");

    for (let i = 0; i < posts.length; i++){
        posts[i].style["display"] = "none";
    }

    document.getElementById(id).style["display"] = 'block';
}


function enable_brightness(id){
    var id1 = 't' + id;
    var id2 = 'p' + id;
    document.getElementById(id1).style["filter"] = 'brightness(1.1)';
    document.getElementById(id1).style["outline"] = '3px #e21616 solid';
    document.getElementById(id2).style["cursor"] = 'pointer';
}


function disable_brightness(id){
    id = 't' + id;
    document.getElementById(id).style["filter"] = 'brightness(1)';
    document.getElementById(id).style["outline"] = 'none';
}
