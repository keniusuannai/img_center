from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw


def index(request, width=0, height=0, bg_color='#ccc', fn_color='#969696'):
    _width = int(width)
    _height = int(height)
    image = Image.new('RGB', (_width, _height), bg_color)

    text = request.GET.get('text', str(width) + '×' + str(height))
    font = ImageFont.truetype('/static/msyh.ttc', int(_width / 10))
    draw = ImageDraw.Draw(image)

    draw.text(((_width - font.getsize(text)[0]) / 2, (_height - font.getsize(text)[1] - _width / 10) / 2), text,
              font=font,
              fill=fn_color)

    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG", quality=100)
    return response
