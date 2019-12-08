from functools import reduce

wide, tall = 25, 6
grid = wide * tall
pixels = open("inputs/day08.txt").read().strip()
layers = [pixels[i:i + grid] for i in range(0, len(pixels), grid)]

min_zero = min(layers, key=lambda x: x.count("0"))
print("answer 1:", min_zero.count("1") * min_zero.count("2"))


def merge_image(image_a, image_b):
    new_image = ""
    for a, b in zip(image_a, image_b):
        new_image += a if a != "2" else b
    return new_image


password = reduce(merge_image, layers)
print("answer 2:")
for i in range(0, len(password), wide):
    print(password[i:i + wide].replace("0", " ").replace("1", "█"))
