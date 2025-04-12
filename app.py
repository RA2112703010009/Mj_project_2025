from flask import Flask, request, render_template
from helpers.scripts import *

app = Flask(__name__)
    
LOGS = """2025-04-01 10:00 AM - System initialized
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected
2025-04-01 10:05 AM - User login detected
2025-04-01 10:10 AM - SQL Checker started
2025-04-01 10:15 AM - User logout detected"""


#class initialization
log_viewer = LogViewer(LOGS)

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/logs', methods=['GET','POST'])
def logs():
    #search_button for log viewer
    if request.method == 'POST':
        search_term = request.form.get('SearchTerm', '').strip()
        highlight_log, message = log_viewer.search_logs(search_term)
        return render_template('logs.html', logs=highlight_log, message=message)
    
    return render_template('logs.html', logs=log_viewer.logs, message=" ")

@app.route('/settings')
def settings():
    return render_template('settings.html')


if __name__ == "__main__":
    app.run(ssl_context=('certs/cert.pem','certs/key.pem'), host="127.0.0.1", debug=True )

