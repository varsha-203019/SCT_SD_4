import csv

products = []
lines = html.split("\n")
for line in lines:
    if "<h2>" in line:
        name = line.replace("<h2>", "").replace("</h2>", "").strip()
    if "Price:" in line:
        price = line.replace("<p>Price:", "").replace("</p>", "").strip()
        products.append([name, price])

# Save to CSV
with open('products.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price"])
    writer.writerows(products)
