import numpy as np
import sys

WIDTH = 25;
HEIGHT = 6;

def part1(image):
    image_len = len(image)
    layers = np.zeros(int(image_len/(WIDTH * HEIGHT)), str).tolist()
    i, j = (0, 0)
    for color_val in image:
        if i == 0 or i % WIDTH*HEIGHT != 0:
            layers[j] += color_val
        elif i % 150 == 0:
            j += 1
            layers[j] += color_val
        i += 1

    # print(layers)
    initVal = sys.maxsize
    min_zero = [-1, initVal, ""]
    for i, l in enumerate(layers):
        num_zeros = l.count('0')
        if int(num_zeros) < min_zero[1]:
            min_zero[0] = i
            min_zero[1] = num_zeros
            min_zero[2] = l

    ones = 0
    twos = 0
    for num in min_zero[2]:
        if num == '1':
            ones += 1
        if num == '2':
            twos += 1

    print("PART 1")
    print(ones * twos)

    return layers

def part2(layers):
    final_img = []
    j = 0
    while j < len(layers[0]):
        for l in layers:
            pixel_color = l[j]
            if pixel_color == "0" or pixel_color == "1":
                final_img.append(pixel_color)
                break
        j += 1
    
    print("PART 2")
    for i in range(len(final_img)):
        if i == 0 or i % WIDTH != 0:
            print(final_img[i], end='')
        else:
            print()
            print(final_img[i], end='')


if __name__ == '__main__':
    image = "";
    with open('input.txt') as f:
        image = f.read();
    
    layers = part1(image)
    part2(layers)
    


    