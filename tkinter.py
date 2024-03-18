
```
master = tk.Tk()

```
from PIL import Image, ImageTk
transperty_images = [] # for memory
def create_transperty_rect(x1, y1, x2, y2, **kwargs):
      alpha = int(kwargs.pop("alpha") * 255)
      fill = kwargs.pop("fill")
      fill = master.winfo_rgb(fill) + (alpha,)
      image = Image.new('RGBA', (x2 - x1, y2 - y1) , fill)
      return image

## poc
transperty_images.append(ImageTk.PhotoImage(
    create_transperty_rect( 
        0,0,200,200,
        fill="#000000",
        alpha=0.4
)))
