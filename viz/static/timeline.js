var buckets = 11,
	data = [{a:67, b:45} , {a:54, b:56}, {a:23, b:12}, {a:56, b:98}, {a:89, b:23}, {a:54, b:67}];

/* Lookup how to convert adict into a list */

drawChart('#chart', data);
registerHover();


/* ************************** */

function registerHover() {

	$('#tiles td').hover(function() {
		$(this).addClass('sel');
	}, function() {
		
		$(this).removeClass('sel');

	});

}

/* ************************** */

function drawChart(dest, data) {
	
	/* d3.selectAll('#hourly_values svg').remove();   --- If you want to redraw dynamically */
	
	var w = 300,
		h = 150;
	
	/* var weeklyData = data[state].views[day] */
	
	view = d3.select('#type label.sel span').attr('class');
	view = 'a';
		
		
	var y = d3.scale.linear()
		.domain([0, d3.max(data, function(d) { return (view === 'all') ? d.a + d.b : d[view] })])
		.range([0, h]);

	
	var chart = d3.select(dest + ' .svg')
		.append('svg:svg')
		.attr('class', 'chart')
		.attr('width', 300)
		.attr('height', 170);
		
	var rect = chart.selectAll('rect'),
		text = chart.selectAll('text');
	
	rect.data(data)
		.enter()
			.append('svg:rect')
				.attr('x', function(d, i) { return i * 12; })
				.attr('y', function(d) { return (view === 'all') ? h - y(d.a + d.b) : h - y(d[view]) })
				.attr('height', function(d) { return (view === 'all') ? y(d.a + d.b) : y(d[view]) })
				.attr('width', 10)
				.attr('class', function(d, i) { return 'hr' + i});
	
	/* text.data(hours)
		.enter()
			.append('svg:text')
				.attr('class', function(d, i) { return (i % 3) ? 'hidden hr' + i : 'visible hr' + i })
				.attr("x", function(d, i) { return i * 12 })
				.attr("y", 166)
				.attr("text-anchor", 'left')
				.text(String); */
}

