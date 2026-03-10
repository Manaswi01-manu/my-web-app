from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Deployment using CodePipeline successful!"

if __name__ == "__main__":
    app.run()