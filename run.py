from app import app
from app.views.items_views import item_bp

app.register_blueprint(item_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
