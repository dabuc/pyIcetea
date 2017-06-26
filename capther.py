import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

r = requests.get('http://agent.formaxmarket.com/user/login')
soup = BeautifulSoup(r.text, 'lxml')
capther_url = 'http://agent.formaxmarket.com' + soup.img['src']
content = requests.get(capther_url).content
i = Image.open(BytesIO(content))
# i.show()
plt.title('capther')
plt.imshow(i)
plt.show()
