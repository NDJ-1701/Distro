from flask import Flask, render_template, jsonify

app = Flask(__name__)

INVENTORY_HEADERS = [
    'SKU', 'Strain', 'Supplier', 'Date Received', 'Quantity Received',
    'Quantity Remaining', 'Cost to House', 'Shelf Price'
]
INVENTORY = [
    {
        'SKU': 10001,
        'Strain': 'GMO',
        'Supplier': 'Gary',
        'Date Received': 'Mar 13',
        'Quantity Received': 18,
        'Quantity Remaining': 15,
        'Cost to House': 550,
        'Shelf Price': 650
    },
    {
        'SKU': 10002,
        'Strain': 'LCG',
        'Supplier': 'Noah',
        'Date Received': 'Mar 15',
        'Quantity Received': 22,
        'Quantity Remaining': 9,
        'Cost to House': 1250,
        'Shelf Price': 1350
    },
]


@app.route("/")
def page_home():
    return render_template('login.html')


@app.route("/api/inventorydata")
def page_inventorydata():
    return jsonify(INVENTORY)


@app.route("/inventory")
def page_inventory():
    return render_template('inventory.html',
                           inventory=INVENTORY,
                           iheaders=INVENTORY_HEADERS)


@app.route("/inventoryModify")
def page_inventoryModify():
    return render_template('inventoryModify.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
