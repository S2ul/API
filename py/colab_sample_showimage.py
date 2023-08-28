import io
import requests
from PIL import Image

res = requests.get("https://www.zinnunkebi.com/wp-content/uploads/2020/06/64AAA653-7906-4A32-815F-E61C4F81BD75-320x240.jpeg")
Image.open(io.BytesIO(res.content))