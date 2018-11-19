from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    #creating a pandas DataFrame
    df = pd.read_excel("C:\\Python\\Scripts\\Templates\\load_status_1.xls")
    return df.to_html()

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(debug=True, host = '10.65.249.1')
    #app.run(host='0.0.0.0') # local server
    #app.run(host="0.0.0.0",port=8000) #static IP
    #http://10.65.252.229:8000/external_data_frame_analysis3
	