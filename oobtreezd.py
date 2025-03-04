import csv
import timeit
from BTrees.OOBTree import OOBTree

def load_data(filename):
    """Завантаження даних з CSV-файлу."""
    items = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row['ID'] = int(row['ID'])
            row['Price'] = float(row['Price'])
            row['Category'] = str(row['Category'])
            row['Name'] = str(row['Name'])
            items.append(row)
    return items

def add_item_to_tree(tree, item):
    """Додавання товару в OOBTree."""
    tree[item['ID']] = item

def add_item_to_dict(dictionary, item):
    """Додавання товару в словник."""
    dictionary[item['ID']] = item

def range_query_tree(tree, min_price, max_price):
    """Діапазонний запит для OOBTree."""
    return [item for _, item in tree.items() if min_price <= item['Price'] <= max_price]

def range_query_dict(dictionary, min_price, max_price):
    """Діапазонний запит для словника."""
    return [item for item in dictionary.values() if min_price <= item['Price'] <= max_price]

def benchmark():
    """Вимірювання продуктивності."""
    filename = 'generated_items_data.csv'
    items = load_data(filename)
    
    tree = OOBTree()
    dictionary = {}
    
    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(dictionary, item)
    
    min_price, max_price = 50, 90
    
    time_dict = timeit.timeit(lambda: range_query_dict(dictionary, min_price, max_price), number=100)
    time_tree = timeit.timeit(lambda: range_query_tree(tree, min_price, max_price), number=100)    
    
    print(f"Total range_query time for OOBTree: {time_tree:.6f} seconds")
    print(f"Total range_query time for Dict: {time_dict:.6f} seconds")

if __name__ == "__main__":
    benchmark()
