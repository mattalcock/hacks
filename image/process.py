from PIL import ImageDraw, Image
from collections import defaultdict

"""
    LimitedList - A list only containing the last n elements seen (not in order)
    seeded with None if no seed is defined. Use getall to get the list.
"""
class LimitedList():
    def __init__(self, max, seed=None):
        self.seed, self.max = seed, max
        self.counter, self.data = 0, []
        for i in xrange(max):
            self.data.append(seed)

    def add(self, item):
        loc = self.counter%self.max
        self.data[loc]=item
        self.counter +=1

    def getall(self):
        return [i for i in self.data if i!=self.seed]

"""
    Utility functions to check colours
"""
def check_colour(value, threshold):
    if threshold is None:
        threshold=0
    r,g,b = value
    if r <= r+threshold and r >= r-threshold:
        if g <= g+threshold and g >= g-threshold:
            if b <= b+threshold and b >= b-threshold:
                return True
    else:
        return False

def check_colour_against_set(value, backgrounds, threshold):
    if threshold is None:
        threshold=0
    bol = False
    for back in backgrounds:
        r,g,b = value
        r2,g2,b2 = back
        if r <= r2+threshold and r >= r2-threshold:
            if g <= g2+threshold and g >= g2-threshold:
                if b <= b2+threshold and b >= b2-threshold:
                    return True
    return False

"""
    Getting a set of background colours based of seed locations and swab radius called surround
"""
def get_backgounds(image, seed_locations, surround):
    backgrounds=set()
    pixel = image.load()
    for sx, sy in seed_locations:
        for x in xrange(surround):
            for y in xrange(surround):
                backgrounds.add(pixel[sx+x, sy+y])
                backgrounds.add(pixel[sx+x, sy-y])
                backgrounds.add(pixel[sx-x, sy+y])
                backgrounds.add(pixel[sx-x, sy+y])

    return list(backgrounds)

"""
    A floodfiil algorithm. ("Fill bounded region.")
    Based on a rough implementation by Eric S. Raymond which I've heavily adapted.

    For perfoamce we check the colour to see it's the mask if not don't process
"""
def floodfill(image, xy, value, backgrounds, back_threshold=None, threshold=None, debug=True, validate_seed=True, test_seed_area=False):   
    pixel = image.load()
    x, y = xy

    #data structures we will need
    like_background = defaultdict(lambda:0)
    like_last = defaultdict(lambda:0)
    stack = LimitedList(30)  #A list only containing the last n elements seen (not in order)
    edge = [(x, y)]

    if test_seed_area:
        saved_threshold = threshold
        threshold=0

    if validate_seed:
        try:
            background = pixel[x, y]
            pixel[x, y] = value
        except IndexError:
            return # seed point outside image

    edge = [(x, y)]
    while edge:
        newedge = []
        for (x, y) in edge:
            for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                try:
                    p = pixel[s, t]
                except IndexError:
                    pass  #outside of image
                else:

                    if test_seed_area and len(stack.getall())>10:
                        #We are going now so lets assume this is a flood
                        threshold=saved_threshold
                    if p!=value: 
                        #The pixel is already the mask so lets not process
                        if check_colour_against_set(p, backgrounds, back_threshold):
                            #checking if point is like background
                            like_background[p]+=1
                            pixel[s, t] = value
                            newedge.append((s, t))
                            stack.add(p)

                        elif check_colour_against_set(p, stack.getall(), threshold):
                            #checking if point is like last points checked (gradient backgrounds)
                            like_last[p]+=1
                            pixel[s, t] = value
                            newedge.append((s, t))
                            stack.add(p)
        edge = newedge
    
    colours_removed = set()
    for k, v in like_last.items():
        colours_removed.add(k)
    for k, v in like_background.items():
        colours_removed.add(k)

    if debug:
        print "Processing Image from Start Point %s,%s" % xy
        print "\t Like Last colours:%s, pixels:%s" % (len(like_last), sum([v for k, v in like_last.items()]))
        print "\t Like Background colours:%s, pixels:%s" % (len(like_background), sum([v for k, v in like_background.items()]))
        print "\t Colors Removed In This Pass: %s" % len(colours_removed)


    return list(colours_removed)

def remove_background(image, mask_colour, new_file_name, meta={}, debug=True):
    trial = image.copy()
    x, y = trial.size

    #Edge Detection and Corner Filling

    offset = meta.get('corner_offset', 20)
    swabr = meta.get('swab_radius', 15)
    back_threshold = meta.get('background_colour_variance', 5)
    threshold = meta.get('flood_colour_varinace', 3)

    seed_locations =[(offset,offset), (x-offset,offset), (offset,y-offset), (x-offset,y-offset)]
    backgrounds = get_backgounds(trial, seed_locations, swabr)
    colours_removed = set()

    for sx, sy in seed_locations:
        removed = floodfill(trial, (sx,sy), mask_colour, backgrounds, back_threshold=back_threshold, threshold=threshold)
        for colour in removed:
            colours_removed.add(colour)
    
    if debug:
        print "Total Colors Removed After Corner Filling: %s" % len(colours_removed)


    #Raster Scan
    grid_locations =[]
    pixel_sample = 10
    for i in xrange(pixel_sample, x, pixel_sample):
        for j in xrange(pixel_sample, y, pixel_sample):
            grid_locations.append((i,j))

    if debug:
        print "Scanning Grid Locations: %s" % len(grid_locations)

    back_threshold = 2
    threshold = 2

    for gx, gy in grid_locations:
        removed = floodfill(trial, (gx,gy), mask_colour, backgrounds, back_threshold=back_threshold, threshold=threshold, validate_seed=False, test_seed_area=True)
        for colour in removed:
            colours_removed.add(colour)

    trial.save(new_file_name)

def process_file(file_name, debug=True):

    image = Image.open(file_name)
    if debug:
        print "Processing File: %s" % file_name
    
    mask_colour = (127,255,0)
    dails = {
        'corner_offset':30,
        'swab_radius':5,
        'background_colour_variance':8,
        'flood_colour_varinace':5
    }
    new_file_name = "new"+ file_name + '_.png'
    remove_background(image, mask_colour, new_file_name, meta=dails, debug=debug)


if __name__ == "__main__":
    process_file('sdryus_2234843_original.jpg')
    process_file('sdryus_2305083_original.jpg')
    process_file('sdryus_2353883_original.jpg')
    process_file('sdryus_2272669_original.jpg')
    process_file('sdryus_2215722_original.jpg')
    process_file('sdryus_2207404_original.jpg')
