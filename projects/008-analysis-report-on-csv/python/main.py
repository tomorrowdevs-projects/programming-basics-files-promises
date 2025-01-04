import csv

def read_csv(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print("Errore: File non trovato.")
        return []

def clean_data(data):
    return [dict(t) for t in {tuple(row.items()) for row in data}]

def analyze_order_ids(data):
    return len(set(row['OrderID'] for row in data))

def analyze_products(data):
    product_count = {}
    total_price = 0
    for row in data:
        product = row['Product']
        product_count[product] = product_count.get(product, 0) + int(row['Quantity'])
        total_price += float(row['Price'])
    avg_price = total_price / len(data) if data else 0
    return product_count, avg_price

def analyze_categories(data):
    category_count = {}
    category_revenue = {}
    for row in data:
        category = row['Category']
        quantity = int(row['Quantity'])
        revenue = float(row['Price']) * quantity
        category_count[category] = category_count.get(category, 0) + quantity
        category_revenue[category] = category_revenue.get(category, 0) + revenue
    return category_count, category_revenue

def analyze_customers(data):
    customer_orders = {}
    customer_spending = {}
    for row in data:
        customer = row['Customer']
        price = float(row['Price']) * int(row['Quantity'])
        customer_orders[customer] = customer_orders.get(customer, 0) + 1
        customer_spending[customer] = customer_spending.get(customer, 0) + price
    return customer_orders, customer_spending

def generate_report(order_count, product_stats, category_stats, customer_stats):
    print("\n=== Report ===")
    print(f"Totale ordini unici: {order_count}")
    print("\nProdotti:")
    for product, count in product_stats[0].items():
        print(f"  {product}: {count}")
    print(f"Prezzo medio: {product_stats[1]:.2f}")
    print("\nCategorie:")
    for category, count in category_stats[0].items():
        print(f"  {category}: {count}")
    for category, revenue in category_stats[1].items():
        print(f"  {category} ricavi: {revenue:.2f}")
    print("\nClienti:")
    for customer, orders in customer_stats[0].items():
        print(f"  {customer}: {orders} ordini")
    for customer, spending in customer_stats[1].items():
        print(f"  {customer} spesa totale: {spending:.2f}")

def main():
    data = read_csv("projects/008-analysis-report-on-csv/python/data.csv")
    data = clean_data(data)
    order_count = analyze_order_ids(data)
    product_stats = analyze_products(data)
    category_stats = analyze_categories(data)
    customer_stats = analyze_customers(data)
    generate_report(order_count, product_stats, category_stats, customer_stats)

if __name__ == "__main__":
    main()
