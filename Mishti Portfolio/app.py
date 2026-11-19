import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    message = request.form.get("message")
    
    print("New Contact Message:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Message: {message}")
    
    return f"""
    <div style="font-family: 'Poppins', sans-serif; text-align: center; padding: 60px; background: #fffaf5; height: 100vh;">
        <h2 style="color: #ea580c; font-size: 2.5rem;">Thank you, {name}!</h2>
        <p style="font-size: 1.2rem; color: #475569;">Your message and phone number have been successfully received.</p>
        <a href="/" style="display: inline-block; margin-top: 20px; background: linear-gradient(135deg, #e11d48 0%, #f97316 100%); color: white; padding: 0.8rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: 600;">Go back to portfolio</a>
    </div>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)