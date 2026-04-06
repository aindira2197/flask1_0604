from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/search')
def search_page():
    products = ["Noutbuk", "Telefon", "Planshet", "Televizor", "Sichqoncha", "Klaviatura"]
    query = request.args.get('q', '')

    # query bo'yicha filter (katta-kichik harf farq qilmaydi)
    results = [p for p in products if query.lower() in p.lower()]

    return render_template("search.html", results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
