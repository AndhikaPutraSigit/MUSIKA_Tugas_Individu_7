from flask import Flask, render_template, request, redirect, url_for, abort, flash
from flask_wtf.csrf import CSRFProtect
from forms import ContactForm, ProductForm
import re

app = Flask(__name__)
app.config["SECRET_KEY"] = "musika-legacy-demo-secret-change-for-production"
csrf = CSRFProtect(app)

CATEGORIES = [
    {"id": 1, "slug": "electric-guitar", "name": "Electric Guitar", "short": "Guitars with a voice of their own", "image": "https://images.unsplash.com/photo-1550291652-6ea9114a47b1?auto=format&fit=crop&w=1200&q=85"},
    {"id": 2, "slug": "acoustic-guitar", "name": "Acoustic Guitar", "short": "Wood, strings, and honest sound", "image": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=1200&q=85"},
    {"id": 3, "slug": "bass", "name": "Bass Guitar", "short": "The heartbeat beneath every song", "image": "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?auto=format&fit=crop&w=1200&q=85"},
    {"id": 4, "slug": "drums", "name": "Drum Set", "short": "Where rhythm finds its pulse", "image": "https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?auto=format&fit=crop&w=1200&q=85"},
    {"id": 5, "slug": "keyboard", "name": "Keyboard", "short": "A thousand worlds under your hands", "image": "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?auto=format&fit=crop&w=1200&q=85"},
    {"id": 6, "slug": "amplifiers", "name": "Amplifiers", "short": "Make every note matter", "image": "https://images.unsplash.com/photo-1589903308904-1010c2294e8?auto=format&fit=crop&w=1200&q=85"},
]

PRODUCTS = [
    {"id": 101, "category": 1, "name": "Fender Player Stratocaster", "tag": "ELECTRIC GUITAR", "price": "Rp 12.450.000", "desc": "A versatile electric guitar with a familiar silhouette and expressive tone.", "image": "https://images.unsplash.com/photo-1550291652-6ea9114a47b1?auto=format&fit=crop&w=1000&q=85"},
    {"id": 102, "category": 1, "name": "Yamaha Pacifica 112V", "tag": "ELECTRIC GUITAR", "price": "Rp 4.250.000", "desc": "A dependable companion for practice, recording, and the stage.", "image": "https://images.unsplash.com/photo-1550291652-6ea9114a47b1?auto=format&fit=crop&w=1000&q=85"},
    {"id": 201, "category": 2, "name": "Martin D-10E", "tag": "ACOUSTIC GUITAR", "price": "Rp 15.900.000", "desc": "Warm projection and a balanced voice for intimate rooms or open stages.", "image": "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?auto=format&fit=crop&w=1000&q=85"},
    {"id": 202, "category": 2, "name": "Yamaha F310", "tag": "ACOUSTIC GUITAR", "price": "Rp 2.150.000", "desc": "An approachable acoustic classic for the first song and the thousandth.", "image": "https://images.unsplash.com/photo-1478737270239-2f02b77fc618?auto=format&fit=crop&w=1000&q=85"},
    {"id": 301, "category": 3, "name": "Ibanez SR300E", "tag": "BASS GUITAR", "price": "Rp 5.850.000", "desc": "Comfortable playability with a focused, articulate low end.", "image": "https://images.unsplash.com/photo-1498038432885-c6f3f1b912ee?auto=format&fit=crop&w=1000&q=85"},
    {"id": 401, "category": 4, "name": "Pearl Roadshow 5-Piece", "tag": "DRUM SET", "price": "Rp 9.750.000", "desc": "A complete acoustic drum setup ready to lay down the foundation.", "image": "https://images.unsplash.com/photo-1519892300165-cb5542fb47c7?auto=format&fit=crop&w=1000&q=85"},
    {"id": 501, "category": 5, "name": "Roland FP-30X", "tag": "KEYBOARD", "price": "Rp 11.200.000", "desc": "Expressive piano feel in a refined instrument for home and studio.", "image": "https://images.unsplash.com/photo-1520523839897-bd0b52f945a0?auto=format&fit=crop&w=1000&q=85"},
    {"id": 601, "category": 6, "name": "Boss Katana-50 MkII", "tag": "AMPLIFIER", "price": "Rp 4.100.000", "desc": "A flexible amplifier for shaping tones from clean to powerful.", "image": "https://images.unsplash.com/photo-1589903308904-1010c2294e8?auto=format&fit=crop&w=1000&q=85"},
]
REGISTERED = {"andhika", "admin", "musika"}

@app.route("/")
def home():
    featured = PRODUCTS[:4]
    return render_template("home.html", categories=CATEGORIES, featured=featured)

@app.route("/tentang")
def about():
    return render_template("about.html")

@app.route("/produk")
def products():
    return render_template("products.html", categories=CATEGORIES, products=PRODUCTS)

CONTACT_MESSAGES = []

@app.route("/kontak", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        CONTACT_MESSAGES.append({"name": form.name.data, "email": form.email.data,
                                 "subject": form.subject.data or "-", "message": form.message.data})
        flash("Terima kasih! Pesan kamu berhasil dikirim.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html", form=form)

@app.route("/kategori/<slug>")
def category_slug(slug):
    category = next((c for c in CATEGORIES if c["slug"] == slug), None)
    if not category:
        abort(404)
    items = [p for p in PRODUCTS if p["category"] == category["id"]]
    return render_template("category.html", category=category, products=items)

@app.route("/produk/<int:id>")
def category_number(id):
    if id < 1 or id > len(CATEGORIES):
        abort(404)
    category = CATEGORIES[id - 1]
    items = [p for p in PRODUCTS if p["category"] == id]
    return render_template("category.html", category=category, products=items)

@app.route("/item/<int:id>")
def product_detail(id):
    product = next((p for p in PRODUCTS if p["id"] == id), None)
    if not product:
        abort(404)
    category = CATEGORIES[product["category"] - 1]
    return render_template("detail.html", product=product, category=category)

@app.route("/cek/<username>")
def check_username(username):
    valid = bool(re.fullmatch(r"[A-Za-z0-9_]{3,20}", username))
    registered = username.lower() in REGISTERED
    return render_template("check_result.html", username=username, valid=valid, registered=registered)

@app.route("/user/<username>")
def user_profile(username):
    valid = bool(re.fullmatch(r"[A-Za-z0-9_]{3,20}", username))
    if not valid:
        abort(404)
    return render_template("user.html", username=username, registered=username.lower() in REGISTERED)

@app.route("/member", methods=["GET", "POST"])
def member():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
            return render_template("member.html", error="Gunakan 3–20 karakter: huruf, angka, atau underscore.")
        return redirect(url_for("user_profile", username=username))
    return render_template("member.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin/dashboard.html", products=PRODUCTS, messages=CONTACT_MESSAGES)

@app.route("/admin/produk/tambah", methods=["GET", "POST"])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        category_id = int(form.category.data)
        category = CATEGORIES[category_id - 1]
        new_id = max((item["id"] for item in PRODUCTS), default=100) + 1
        PRODUCTS.append({
            "id": new_id,
            "category": category_id,
            "name": form.name.data.strip(),
            "tag": category["name"].upper(),
            "price": "Rp " + f"{form.price.data:,}".replace(",", "."),
            "desc": form.description.data.strip(),
            "image": category["image"],
            "stock": form.stock.data,
        })
        flash("Produk berhasil ditambahkan ke katalog!", "success")
        return redirect(url_for("admin_dashboard"))
    return render_template("admin/add_product.html", form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
