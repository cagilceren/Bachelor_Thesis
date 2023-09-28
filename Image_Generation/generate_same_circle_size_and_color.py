import os
import random
from PIL import Image, ImageDraw


def generate_same_size():
    # Configuration
    num_images = 2000          # Number of images to generate
    image_size = (500, 500)  # Size of each image in pixels
    circle_radius_max = 100       # Radius of each circle in pixels
    # circle_color = (255, 0, 0)  # Color of the circles (in RGB format)
    max_color = 255
    os.makedirs(f'data/same_size_and_color', exist_ok=True)
        
    # Generate multiple images
    for image_num in range(num_images):

        circle_radius = random.randint(25, circle_radius_max)
        
        circle_color = (random.randint(0, max_color), random.randint(0, max_color), random.randint(0, max_color))
        
        # Create a new image with a white background
        image = Image.new("RGB", image_size, (255, 255, 255))
        draw = ImageDraw.Draw(image)

        # Calculate the number of circles that can fit in the image
        num_circles_horizontal = image_size[0] // (2 * circle_radius)
        num_circles_vertical = image_size[1] // (2 * circle_radius)

        # Calculate the spacing between circles
        horizontal_spacing = (image_size[0] - (2 * circle_radius * num_circles_horizontal)) // (num_circles_horizontal + 1)
        vertical_spacing = (image_size[1] - (2 * circle_radius * num_circles_vertical)) // (num_circles_vertical + 1)

        # Draw circles on the image
        for i in range(num_circles_horizontal):
            for j in range(num_circles_vertical):
                # Calculate the center coordinates of the circle
                center_x = (2 * i + 1) * circle_radius + (i + 1) * horizontal_spacing
                center_y = (2 * j + 1) * circle_radius + (j + 1) * vertical_spacing

                # Draw the circle if it does not overlap with existing circles
                if (
                    center_x - circle_radius >= 0
                    and center_x + circle_radius <= image_size[0]
                    and center_y - circle_radius >= 0
                    and center_y + circle_radius <= image_size[1]
                ):
                    draw.ellipse(
                        [
                            (center_x - circle_radius, center_y - circle_radius),
                            (center_x + circle_radius, center_y + circle_radius),
                        ],
                        fill=circle_color,
                        outline=circle_color,
                    )

        num_circles = num_circles_horizontal * num_circles_vertical
        # Save the image with a unique filename
        image_filename = f"data/same_size_and_color/class_{num_circles}_circles_{image_num + 1}.png"
        image.save(image_filename)

        print(f"Image {image_num + 1} generated: {image_filename}")

generate_same_size()
