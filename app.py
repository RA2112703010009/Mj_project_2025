from flask import Flask, request, render_template
import psutil
from helpers.scripts import *
from helpers.visualization  import *

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


# Integrate Dash app into Flask
create_dash_app(app)

#class initialization
log_viewer = LogViewer(LOGS)

def get_processes():
    """Fetch a list of running processes"""
    return [proc.info for proc in psutil.process_iter(attrs=['pid', 'name'])]



@app.route('/', methods=['GET','POST'])
def dashboard():
    search_term = request.form.get('SearchTerm', '').strip() if request.method == 'POST' else None
    selected_process = request.form.get('SelectedProcess', '').strip() if request.method == 'POST' else None
    processes = get_processes()
    # Filter processes based on search input
    if search_term:
        processes = [proc for proc in processes if search_term in proc['name'].lower()]

    return render_template('index.html', processes=processes, search_term=search_term, selected_process=selected_process)


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

