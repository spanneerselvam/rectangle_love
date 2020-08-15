"""
Considering rectangles overlapping if they share one edge.
"""
def overlap_rectangles(r1, r2):
    
    right_x1 = r1['left_x'] + r1['width']
    top_y1 = r1['bottom_y'] + r1['height']
    right_x2 = r2['left_x'] + r2['width']
    top_y2 = r2['bottom_y'] + r2['height']
    x1 = (r1['left_x'], right_x1)
    y1 = (r1['bottom_y'], top_y1)
    x2 = (r2['left_x'], right_x2)
    y2 = (r2['bottom_y'], top_y2) 
    print("R1 Coordinates:", x1, y1)
    print("R2 Coordinates:", x2, y2)
    
    if min(right_x1, r1['left_x']) <= min(right_x2, r2['left_x']) and min(right_x2, r2['left_x']) <= max(right_x1, r1['left_x']):
        if min(top_y1, r1['bottom_y']) <= min(top_y2, r2['bottom_y']) and min(top_y2, r2['bottom_y']) <= max(top_y1, r1['bottom_y']):
            print("R1 and R2 overlap")
            return True
        else:
            print("R1 and R2 do not overlap")
            return False
r1 = {

# Coordinates of bottom-left corner
'left_x'   : 1,
'bottom_y' : 1,

# Width and height
'width'    : 6,
'height'   : 3,

}
r2 = {
'left_x'   : 3,
'bottom_y' : 4,

# Width and height
'width'    : 6,
'height'   : 3,
 
}
r2 = {

# Coordinates of bottom-left corner
'left_x'   : 1,
'bottom_y' : 1,

# Width and height
'width'    : 6,
'height'   : 3,

}

print(overlap_rectangles(r1, r2))

