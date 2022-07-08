from PIL import Image
import requests, json
from skimage import io

URL = "https://api.url.com" # API Link 

response_api = requests.get(URL)
response_json = json.loads(response_api.text)


io.imshow(io.imread(response_json["url"])) # Json key to url 
io.show()
