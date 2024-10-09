
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def main(args):
    # Step 1: Generate a plot
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure()
    plt.plot(x, y)
    plt.title('Sine Wave')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')

    # Step 2: Save the plot to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Step 3: Encode the image in base64
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    # Create an HTML image tag
    html_img = f'<img src="data:image/png;base64,{image_base64}" alt="Sine Wave Plot" width="300"/>'

    return {
          "headers": { 'Content-Type': 'text/html; charset=utf-8' },
          "body": html_img
       }
