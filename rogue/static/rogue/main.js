var dummy_entity = {
    'x': 5,
    'y': 6,
}

function draw_game(canvas_id) {
    var canvas = document.getElementById(canvas_id);
    var ctx    = canvas.getContext('2d');

    var hero = dummy_entity;
}

$(document).ready(function() {
    var canvas_id = "canvas";
    draw_game(canvas_id);
});
