from ctypes.wintypes import RGB
import random
import os

from PIL import Image, ImageDraw
def generate_circles(max):
    # set the seed for the random number generator
    random.seed()

    # set the size of the image
    width = 800
    height = 800

    # set the maximum number of shapes
    max_shapes = max + 1

    # set the maximum size of a shape
    max_size = 100

    # set the maximum color value
    max_color = 255


    #create folder
    os.makedirs(f'data/test', exist_ok=True)

    def generate_image():
        # create a new image
        image = Image.new("RGB", (width, height), color='white')

        # create a draw object
        draw = ImageDraw.Draw(image)

        # create a list to store the shapes
        shapes = []

        num_circle = 0
    
        # draw the shapes
        for i in range(1, max_shapes):
            # generate a random size
            size = random.randint(10, max_size)

            # generate a random position for the shape
            x = random.randint(size, width - size)
            y = random.randint(size, height - size)

            # generate a random color for the shape
            color = (random.randint(0, max_color), random.randint(0, max_color), random.randint(0, max_color))

            # generate a random shape (circle or rectangle)
            if random.random() < 0.5: # circle
                # check if the circle overlaps with any existing shapes
                overlapping = False
                for shape in shapes:
                    distance = ((x - shape[0]) ** 2 + (y - shape[1]) ** 2) ** 0.5
                    if distance < size + shape[2]:
                        overlapping = True
                        break

                # draw the circle if it does not overlap
                if not overlapping:
                    draw.ellipse((x - size, y - size, x + size, y + size), fill=color)
                    num_circle += 1
                    shapes.append((x, y, size))
        return image, num_circle
    
    #saves n images with the max number of counts
    k =0
    while k < 20:
        image_info = generate_image()
        if image_info[1] == max:
            k += 1
            filename = f"data/test/class_{image_info[1]}_circle_{k}.png"
            image_info[0].save(filename)

for i in range(1, 11):
    generate_circles(i)