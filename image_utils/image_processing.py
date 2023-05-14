import base64
import weaviate

client = weaviate.Client(
    url="http://localhost:8080",
)

def train_model():
  return

def search_similar_img(image_file):
  image_data = image_file.read()
  encoded_image = base64.b64encode(image_data).decode("utf-8")

  near_image = {"image": encoded_image}
  res_img = (
      client.query.get("Meme", "image")
      .with_near_image(near_image, encode=False)
      .with_limit(1)
      .do()
  )
  return res_img['data']['Get']['Meme'][0]['image']
