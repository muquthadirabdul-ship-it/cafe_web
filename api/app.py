from flask import Flask, render_template, request

# Important: template_folder and static_folder paths relative to api/
app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

menu = {
    "coffee": 2.50,
    "tea": 2.00,
    "sandwich": 5.00,
    "cake": 3.50
}

@app.route("/", methods=["GET", "POST"])
def index():
    bill = None
    order = {}
    customer = ""

    if request.method == "POST":
        customer = request.form.get("customer")

        for item in menu:
            qty = request.form.get(item)
            if qty and qty.isdigit() and int(qty) > 0:
                order[item] = int(qty)

        bill = sum(menu[item] * qty for item, qty in order.items())

    return render_template("index.html", menu=menu, bill=bill, order=order, customer=customer)
