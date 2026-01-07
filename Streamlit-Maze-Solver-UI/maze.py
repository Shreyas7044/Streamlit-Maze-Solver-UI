def find_shortest_path(image, start, end):
    # Placeholder path logic
    return [start, end]

def drawPath(image, path, thickness):
    import cv2
    for i in range(len(path) - 1):
        cv2.line(image, path[i], path[i + 1], (0, 0, 255), thickness)