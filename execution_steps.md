✅ Step-by-Step for Docker

🚀 Build & Run Docker Container

# Build the image
docker build -t cidr-calculator .

# Run the container
docker run -p 5000:5000 cidr-calculator
Then open your browser to http://localhost:5000


✅ Step-by-Step for macOS
1. Open Terminal
2. Create a Virtual Environment (recommended)

cd ~/Desktop/VS-Code/CIDR\ Web\ application/
python3 -m venv venv
source venv/bin/activate
You should now see your prompt change to indicate the virtual environment is active (e.g., (venv)).

3. Install Flask

pip install flask
(Optional: Save dependencies to requirements.txt)

pip freeze > requirements.txt

4. Open the App
In your browser, go to:

http://localhost:5001
✅ Done! You're now running a Flask web app on your Mac.

