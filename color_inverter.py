from PIL import ImageColor
import matplotlib.colors as mcolors

def invert_color(colors):
    updated = []
    for color in colors[:-1]:  
        if isinstance(color, str):
            if color.startswith("#"):  
                rgb = ImageColor.getrgb(color)
            elif color in mcolors.CSS4_COLORS:  
                rgb = ImageColor.getrgb(mcolors.CSS4_COLORS[color])
            else:
                raise ValueError(f"Invalid color name or HEX format: {color}")
            inverted = tuple(255 - c for c in rgb)
            updated.append("#{:02X}{:02X}{:02X}".format(*inverted))
        
        elif isinstance(color, tuple) and len(color) == 3:
            if all(0 <= c <= 255 for c in color):  
                updated.append(tuple(255 - c for c in color))
            elif all(0 <= c <= 1 for c in color):  
                h, s, l = color
                inverted_h = (h + 0.5) % 1.0  
                updated.append((inverted_h, s, 1 - l))
            else:
                raise ValueError(f"Invalid RGB or HSL color format: {color}")
        else:
            raise ValueError(f"Unsupported color format: {color}")
    
    updated.append(colors[-1])  
    return updated

if __name__ == "__main__":
    color_list = ['#FF7FFF', '#00FFFF', '#FF00FF', '#00FFFF', '#FF7FFF', '#00FFFF', '#6C7449', '#00FFFF', '#000000', '#FFFFFF', '#7F7F7F', 'Solid line']
    print(invert_color(color_list))
