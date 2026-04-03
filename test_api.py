from gradio_client import Client, handle_file

client = Client("123Sashank12/trufor-splicing-detecto")

img_path = r"C:\Users\Abhay Kalojia\Desktop\Splice\TruFor\sample5.jpeg"

score, anomaly_img, confidence_img = client.predict(
    handle_file(img_path), 
    api_name="/predict"
)

print("Score:", score)
print("Anomaly:", anomaly_img)
print("Confidence:", confidence_img)