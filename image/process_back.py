from PIL import ImageDraw, Image
from collections import defaultdict

def find_simualr_colours(value, threshold):
    print value
    r,g,b = value
    new_colours=[value]

    for i in xrange(1, threshold+1):
        for j in xrange(1, threshold+1):
            for k in xrange(1, threshold+1):
                #new_colours.append((r+i, g+j, b+k))
                new_colours.append((r-i, g-j, b-k))

    print new_colours
    return new_colours

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


def floodfill(image, xy, value, backgrounds, border=None, back_threshold=None, threshold=None, debug=True):
    "Fill bounded region."
    # based on an implementation by Eric S. Raymond
    pixel = image.load()
    x, y = xy

    like_background = defaultdict(lambda:0)
    like_last = defaultdict(lambda:0)

    last = []

    try:
        background = pixel[x, y]
        pixel[x, y] = value
    except IndexError:
        return # seed point outside image

    edge = [(x, y)]
    if border is None:
        while edge:
            newedge = []
            for (x, y) in edge:
                for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    try:
                        p = pixel[s, t]
                    except IndexError:
                        pass
                    else:
                        if check_colour_against_set(p, backgrounds, back_threshold):
                            like_background[p]+=1
                            pixel[s, t] = value
                            newedge.append((s, t))
                            last.append(p)
                        elif check_colour_against_set(p, last[-20:], threshold):
                            like_last[p]+=1
                            pixel[s, t] = value
                            newedge.append((s, t))
                            last.append(p)
            edge = newedge
    else:
        while edge:
            newedge = []
            for (x, y) in edge:
                for (s, t) in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    try:
                        p = pixel[s, t]
                    except IndexError:
                        pass
                    else:
                        if p != value and p != border:
                            pixel[s, t] = value
                            newedge.append((s, t))
            edge = newedge
    
    if debug:
        print "Processing Image from Start Point %s,%s" % xy
        print "\t Like Last colours:%s, pixels:%s" % (len(like_last), sum([v for k, v in like_last.items()]))
        print "\t Like Background colours:%s, pixels:%s" % (len(like_background), sum([v for k, v in like_background.items()]))

def remove_background(image, mask_colour, new_file_name, meta={}):
    trial = image.copy()
    x, y = trial.size

    offset = meta.get('corner_offset', 20)
    swabr = meta.get('swab_radius', 15)
    back_threshold = meta.get('background_colour_variance', 8)
    threshold = meta.get('flood_colour_varinace', 5)

    seed_locations =[(offset,offset), (x-offset,offset), (offset,y-offset), (x-offset,y-offset)]
    backgrounds = get_backgounds(trial, seed_locations, swabr)

    for sx, sy in seed_locations:
        floodfill(trial2, (sx,sy), mask_colour, backgrounds, back_threshold=back_threshold, threshold=threshold)

    trail.save(new_file_name)

def process_file(file_name):
    image = Image.open(file_name)
    
    mask_colour = (127,255,0)

    dails = {
        'corner_offset':30,
        'swab_radius':5,
        'background_colour_variance':8,
        'flood_colour_varinace':5
    }
    new_file_name = "new"+ file_name
    remove_background(image, mask_colour, new_file_name, meta=dails)


if __name__ == "__main__":
    process_file('sdryus_2234843_original.jpg')
    process_file('sdryus_2305083_original.jpg')
    process_file('sdryus_2353883_original.jpg')
    process_file('sdryus_2272669_original.jpg')
    process_file('sdryus_2215722_original.jpg')
    process_file('sdryus_2207404_original.jpg')
