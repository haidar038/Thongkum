import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from web import create_app

app = create_app()

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    app.run()