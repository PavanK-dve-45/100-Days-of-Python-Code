import colorgram

# colors = [
#     "red", "blue", "green", "yellow", "purple", "orange", "pink", "black",
#     "white", "brown", "gray", "cyan", "magenta", "light blue", "light green",
#     "dark blue", "dark green", "gold", "silver", "beige", "coral", "indigo",
#     "violet", "maroon", "olive", "navy", "teal", "lime", "khaki", "turquoise"
# ]
colors = colorgram.extract('Image1.jpg',50)
rgb_colors =[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))