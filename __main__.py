
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
    html_img = f'<img src="data:image/png;base64,{image_base64}" alt="Sine Wave Plot" width="100%"/>'

    return {
          "headers": { 'Content-Type': 'text/html; charset=utf-8' },
          "body": html_img
       }
"""

def main(args):

    html = '
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h2>Click the button below:</h2>
        <button type="button" onclick="youclicked()">Click Me</button>
        <script>  
            function youclicked(){  
            alert("You Clicked!");  
            }  
        </script>
        <canvas id="myChart" style="width:100%;max-width:700px"></canvas>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js"></script>
        <script>
            var xyValues = [{x:50, y:7}, {x:60, y:8}, {x:70, y:8}, {x:80, y:9}, {x:90, y:9}];

            new Chart("myChart", {
                type: "scatter",
                data: {
                datasets: [{
                    pointRadius: 4,
                    pointBackgroundColor: "rgb(0,0,255)",
                    data: xyValues
                }]
                },
                options: {
                legend: {display: false},
                scales: {
                    xAxes: [{ticks: {min: 40, max:100}}],
                    yAxes: [{ticks: {min: 6, max:10}}],
                }
                }
            });
        </script>
    </body>
    </html>
    '
    
    return {
          "headers": { 'Content-Type': 'text/html; charset=utf-8' },
          "body": html
       }
"""