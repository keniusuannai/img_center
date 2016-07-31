from django.http import HttpResponse
from PIL import Image, ImageFont, ImageDraw


def index(request, width=0, height=0, bg_color='ccc', fn_color='969696'):
    _width = int(width)
    _height = int(height)
    txt = request.GET.get('text', str(width) + '×' + str(height)).replace('+', ' ')
    txtsize = request.GET.get('txtsize', int(_width / 10))
    image = Image.new('RGB', (_width, _height), '#' + bg_color)
    font = ImageFont.truetype('/static/msyh.ttc', int(txtsize))
    draw = ImageDraw.Draw(image)

    draw.text(((_width - font.getsize(txt)[0]) / 2, (_height - font.getsize(txt)[1] - _width / 10) / 2), txt,
              font=font,
              fill='#' + fn_color)

    response = HttpResponse(content_type="image/jpeg")
    image.save(response, "JPEG", quality=100)
    return response
