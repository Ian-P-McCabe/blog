from colorsys import rgb_to_hsv
from colormath import color_diff

def hex_to_hsv(hex_color):
    """Convert hex color to HSV tuple (hue, saturation, value)"""
    hex_color = hex_color.lstrip('#')
    r, g, b = [int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4)]
    h, s, v = rgb_to_hsv(r, g, b)
    return (h, s, v)

def adjust_hue_for_rainbow(hex_color):
    """Adjust hue so red starts at beginning (red -> yellow -> green -> blue -> magenta -> red)"""
    h, s, v = hex_to_hsv(hex_color)
    # Rotate hue by -0.1 so red (which is ~0) starts first
    h = (h + 0.15) % 1.0
    return (h, s, v)   


def build_distance_matrix(lab_colors):
  distance_matrix = {}
  for i, color1 in enumerate(lab_colors):
      for j, color2 in enumerate(lab_colors):
          if i != j:
            distance_matrix[(i, j)] = round( #Want integer values
              color_diff.delta_e_cie2000(color1=color1, color2=color2)
              )
  
  return distance_matrix