import numpy as np

"""
import os
import matplotlib.pyplot as plt
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
"""

import os
import base64

def main(args):
    responseBody=str(np.random.rand())
    encodedResponse=base64.encodebytes(responseBody.encode()).decode("utf-8").strip()
    return {
        "headers": {
            "Content-Type": "text/plain",
        },

        "statusCode": 200,
        "body": encodedResponse,
    }