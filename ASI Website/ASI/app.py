from flask import Flask

def create_app():
    app = Flask(__name__)
    from routes import main
    app.register_blueprint(main)

    return app

def main():
    print()

if __name__ == "__main__":
    main()