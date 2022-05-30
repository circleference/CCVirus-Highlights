import cv2, numpy, pygame

def sharp_compression(image, intensity=10):
    cv2.useOptimized()
    view = pygame.surfarray.pixels3d(image).transpose([1, 0, 2])
    image = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    

    scale_percent = 20

    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    dsize = (width, height)

    result = cv2.resize(image, dsize)

    kernel = numpy.array([[intensity, -1, 0],
                    [-1, 2 * intensity,-1],
                    [intensity, -1, intensity]])
    result = cv2.filter2D(src=result, ddepth=-1, kernel=kernel)

    return pygame.image.frombuffer(result.tostring(), result.shape[1::-1],"BGR")

def resolution_compression(image, intensity=13):
    cv2.useOptimized()
    view = pygame.surfarray.pixels3d(image).transpose([1, 0, 2])
    image = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    scale_percent = intensity

    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)

    dsize = (width, height)

    result = cv2.resize(image, dsize)

    return pygame.image.frombuffer(result.tostring(), result.shape[1::-1],"BGR")