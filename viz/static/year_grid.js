var buckets = 52,
    days = [
        { name: 'Monday', abbr: 'Mo' },
        { name: 'Tuesday', abbr: 'Tu' },
        { name: 'Wednesday', abbr: 'We' },
        { name: 'Thursday', abbr: 'Th' },
        { name: 'Friday', abbr: 'Fr' },
        { name: 'Saturday', abbr: 'Sa' },
        { name: 'Sunday', abbr: 'Su' }
    ],
    day_names = ['M', 'T', 'W','T', 'F', 'S', 'S'],
    hours = ['12a', '1a', '2a', '3a', '4a', '5a', '6a', '7a', '8a', '9a', '10a', '11a', '12p', 
                '1p', '2p', '3p', '4p', '5p', '6p', '7p', '8p', '9p', '10p', '11p'];

/* Lookup how to convert adict into a list */

createWeekTiles('#weekgrid');
createTiles('#grid', hours, day_names, 'day_tiles');
registerHover();


/* ************************** */

function registerHover() {

    $('#day_tiles td').hover(function() {
        $(this).addClass('sel');
    }, function() {
        
        $(this).removeClass('sel');

    });

}

/* ************************** */

function createTiles(dest, xlist, ylist, id) {

    var html = '<table id=' + id + ' class="front">';

    html += '<tr><th><div>&nbsp;</div></th>';

    for (var x = 0; x < xlist.length; x++) {
        html += '<th class="x' + x + '">' + xlist[x] + '</th>';
    }
    
    html += '</tr>';

    for (var y = 0; y < ylist.length; y++) {
        html += '<tr class="y' + y + '">';
        html += '<th>' + ylist[y] + '</th>';
        for (var x = 0; x < xlist.length; x++) {
            html += '<td id="y' + y + 'x' + x + '" class="y' + y + ' x' + x + '"><div class="tile"><div class="face front"></div><div class="face back"></div></div></td>';
        }
        html += '</tr>';
    }
    
    html += '</table>';
    d3.select(dest).html(html);
}

/* ************************** */

function createWeekTiles(dest) {

    var html = '<table id="tiles" class="front">';

    html += '<tr><th><div>&nbsp;</div></th>';

    for (var h = 0; h < hours.length; h++) {
        html += '<th class="h' + h + '">' + hours[h] + '</th>';
    }
    
    html += '</tr>';

    for (var d = 0; d < days.length; d++) {
        html += '<tr class="d' + d + '">';
        html += '<th>' + days[d].abbr + '</th>';
        for (var h = 0; h < hours.length; h++) {
            html += '<td id="d' + d + 'h' + h + '" class="d' + d + ' h' + h + '"><div class="tile"><div class="face front"></div><div class="face back"></div></div></td>';
        }
        html += '</tr>';
    }
    
    html += '</table>';
    d3.select(dest).html(html);
}