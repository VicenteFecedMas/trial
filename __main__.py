import os
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def generate_dummy_image():
    # Create a simple dummy image using matplotlib
    plt.figure(figsize=(5, 5))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title('Dummy Image')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    
    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)  # Rewind the buffer to the beginning
    return buf.getvalue()

def main(args):
    # Generate a dummy image
    image_data = np.random.rand()
    
    # Encode the image data in Base64
    #encoded_image = base64.b64encode(image_data).decode('utf-8')
    
    return {
        "headers": {
            "Content-Type": "text/plain",  # Specify the content type for an image
        },
        "statusCode": 200,
        "body": str(image_data),  # Base64 encoded image data
    }
