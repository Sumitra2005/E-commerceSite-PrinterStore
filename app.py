from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock products
products = [
    {"id": "printer-a", "name": "Printer A", "price": 150},
    {"id": "printer-b", "name": "Printer B", "price": 200},
    {"id": "printer-c", "name": "Printer C", "price": 250},
]

cart = []


@app.route("/cart", methods=["GET"])
def index():
 return render_template("index.html", products=products, cart=cart)


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = request.form.get("product_id")
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        cart.append(product)
        return jsonify(
            {"status": "success", "cart_total": sum(p["price"] for p in cart)}
        )
    return jsonify({"status": "error"}), 400


@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_id = request.form.get("product_id")
    cart[:] = [p for p in cart if p["id"] != product_id]  # <-- in-place update
    return jsonify({"status": "success", "cart_total": sum(p["price"] for p in cart)})


if __name__ == "__main__":
    app.run(debug=True)
