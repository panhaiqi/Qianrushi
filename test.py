from load import load
from image_process import image_process

model = load()
img = input()

data = image_process(img)
print(model.predict(data))
