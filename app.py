import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize the application
app = Flask(__name__)

# SECURITY WARNING: This key is for development only.
app.secret_key = 'dev-secret-key-for-session-management'

# --- Routes ---

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Mock Authentication Logic
        if username == "admin" and password == "password":
            flash(f'Welcome back, {username}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials. Try admin/password', 'danger')
            
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Handle user registration."""
    if request.method == 'POST':
        email = request.form.get('email')
        # Here you would typically save the user to a database
        flash(f'Account created for {email}! Please log in.', 'success')
        return redirect(url_for('login'))
        
    return render_template('signup.html')

if __name__ == "__main__":
    # CRITICAL: Host 0.0.0.0 is required for container/agent access
    # Debug mode allows live reloading of changes
    print("🚀 Starting Flask Server on port 5000...")
    app.run(host='0.0.0.0', port=5000, debug=True)
