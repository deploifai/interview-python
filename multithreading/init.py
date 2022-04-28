def get_image_url(size):
    return "https://via.placeholder.com/{}".format(size)


def init(size):
    return [get_image_url(i * 10) for i in range(1, size + 1)]
