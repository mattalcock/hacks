from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

"""
dataset = [('name, [(x,y),(x1,y1)]), ('name2', [(x2,y2),(x3,y3)])]
data is a list of series where each series is a list of tuples
"""

def maxy(dataset):
    maxy=0
    for name, s in dataset:
        m=max([y for x, y in s])
        if m > maxy:
            maxy = m
    return maxy

def linechart(name, dataset, size=(400,400)):
    max_y = maxy(dataset)
    chart = SimpleLineChart(size[0], size[1], y_range=[0, max_y])
    legend = []
    for series_name, s in dataset:
        chart.add_data([y for x, y in s])
        legend.append(series_name)
    
    chart.set_colours(['057D9F', '8106A9', 'E9FB00', 'FF8100'])
    chart.set_legend(legend)
    chart.set_grid(0, 25, 5, 5)
    
    left_axis = range(0, int(max_y + 1), 25)
    left_axis[0] = ''
    chart.set_axis_labels(Axis.LEFT, left_axis)
    
    bottom_axis = [x for x, y in dataset[0][1]]
    chart.set_axis_labels(Axis.BOTTOM, bottom_axis)
    chart.download(name)
    
if __name__ == '__main__':
    data =[
            [(1000, 6.107497215270996), (2000, 13.0964994430542), (3000, 20.646286010742188), (4000, 28.435134887695312), (5000, 37.9558801651001),
            (6000, 45.04199028015137), (7000, 52.11312770843506), (8000, 59.99007225036621), (9000, 68.20797920227051)],
            [(1000, 0.2487659454345703), (2000, 0.5492925643920898), (3000, 0.857090950012207), (4000, 1.1699199676513672), (5000, 1.5373945236206055),
             (6000, 1.8898963928222656), (7000, 2.2233009338378906), (8000, 2.5486230850219727), (9000, 2.9711246490478516)]
          ]
    linechart('line.png', data)
