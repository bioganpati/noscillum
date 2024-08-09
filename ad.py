def normalize_angle(angle):
    normalized_angle = angle % 360
    if normalized_angle < 0:
        normalized_angle += 360
    return normalized_angle
