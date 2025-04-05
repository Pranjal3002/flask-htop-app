from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Pranjal"  # Replace with your name
    try:
        username = os.getlogin()
    except:
        username = os.environ.get('USER') or os.environ.get('USERNAME') or 'Unknown'

    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    
    top_output = subprocess.getoutput('top -b -n 1 | head -20')  # limit output

    return f"""
    <pre>
    Name: {full_name}
    Username: {username}
    Server Time (IST): {ist_time}
    
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
