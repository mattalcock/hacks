var types = {
		organic: 'Organic',
		paid: 'Paid',
		all: 'All'
	},
	buckets = 11,
	data = [{organic:67, paid:45} , {organic:54, paid:56}, {organic:23, paid:12}, {organic:56, paid:98}, {organic:89, paid:23}, {organic:54, paid:67}];

/* Lookup how to convert adict into a list */

drawChart('#keychart', data);
drilldownListener();

/* ************************** */

function drawChart(dest, chart_data) {

	d3.selectAll(dest + ' svg').remove();

	var w = 300,
		h = 150;

	weeklyData = chart_data
	view = d3.select('#type label.sel span').attr('class');

	var y = d3.scale.linear()
		.domain([0, d3.max(weeklyData, function(d) { return (view === 'all') ? d.organic + d.paid : d[view] })])
		.range([0, h]);

	console.log(view)

	var chart = d3.select(dest + ' .svg')
		.append('svg:svg')
		.attr('class', 'chart')
		.attr('width', 300)
		.attr('height', 170);

	var rect = chart.selectAll('rect'),
		text = chart.selectAll('text');

	rect.data(weeklyData)
		.enter()
			.append('svg:rect')
				.attr('x', function(d, i) { return i * 12; })
				.attr('y', function(d) { return (view === 'all') ? h - y(d.organic + d.paid) : h - y(d[view]) })
				.attr('height', function(d) { return (view === 'all') ? y(d.organic + d.paid) : y(d[view]) })
				.attr('width', 10)
				.attr('class', function(d, i) { return 'hr' + i});

	
}

function selectedType() {
	
	//return d3.select('input[name="type"]:checked').property('value'); // IE8 doesn't like this
	return $('input[name="type"]:checked').val();
}

function drilldownListener(){

	$('input[name="type"]').change(function() {
		
		var type = $(this).val()
		
		d3.selectAll('fieldset#type label').classed('sel', false);
		d3.select('label[for="type_' + type + '"]').classed('sel', true);
		var type = types[selectedType()];

		drawChart('#keychart', data);

		//d3.select('#wtf .subtitle').html(type  + ' traffic daily');
	});

}
