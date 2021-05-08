def has_collision(a, b):
    x_overlap = (a.left < b.right) and (a.right > b.left)
    y_overlap = (a.top < b.bottom) and (a.bottom > b.top)
    return x_overlap and y_overlap
