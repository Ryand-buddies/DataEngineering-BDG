#!/usr/bin/env python3
"""
Script para generar datos de ejemplo para los ejercicios de Data Engineering
"""

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Configurar faker
fake = Faker(['es_ES', 'en_US'])
Faker.seed(42)
np.random.seed(42)
random.seed(42)

def generate_users(n_users=1000):
    """Generar datos de usuarios"""
    users = []
    for i in range(1, n_users + 1):
        user = {
            'user_id': i,
            'name': fake.name(),
            'email': fake.email(),
            'registration_date': fake.date_between(start_date='-2y', end_date='today'),
            'age': random.randint(18, 70),
            'country': fake.country()
        }
        users.append(user)
    return pd.DataFrame(users)

def generate_products(n_products=500):
    """Generar catálogo de productos"""
    categories = ['Electronics', 'Clothing', 'Books', 'Home & Garden', 'Sports', 'Beauty', 'Toys', 'Food']
    brands = ['BrandA', 'BrandB', 'BrandC', 'BrandD', 'BrandE', 'GenericBrand']
    
    products = []
    for i in range(1, n_products + 1):
        category = random.choice(categories)
        cost_price = round(random.uniform(5, 500), 2)
        margin = random.uniform(0.2, 0.8)  # 20-80% margin
        
        product = {
            'product_id': i,
            'product_name': fake.catch_phrase(),
            'category': category,
            'brand': random.choice(brands),
            'cost_price': cost_price,
            'selling_price': round(cost_price * (1 + margin), 2)
        }
        products.append(product)
    return pd.DataFrame(products)

def generate_transactions(users_df, products_df, n_transactions=10000):
    """Generar transacciones"""
    payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash']
    countries = ['Spain', 'Mexico', 'Argentina', 'Colombia', 'Chile', 'Peru']
    
    transactions = []
    start_date = datetime.now() - timedelta(days=365)
    
    for i in range(1, n_transactions + 1):
        user_id = random.choice(users_df['user_id'].tolist())
        product = products_df.sample(1).iloc[0]
        
        transaction = {
            'transaction_id': i,
            'user_id': user_id,
            'product_id': product['product_id'],
            'product_name': product['product_name'],
            'category': product['category'],
            'price': product['selling_price'],
            'quantity': random.randint(1, 5),
            'timestamp': fake.date_time_between(start_date=start_date, end_date='now'),
            'country': random.choice(countries),
            'payment_method': random.choice(payment_methods)
        }
        transactions.append(transaction)
    
    return pd.DataFrame(transactions)

def main():
    """Función principal para generar todos los datasets"""
    print("🚀 Generando datasets de ejemplo...")
    
    # Crear directorio de datos si no existe
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    # Generar usuarios
    print("👥 Generando usuarios...")
    users_df = generate_users(1000)
    users_df.to_csv(os.path.join(data_dir, 'users.csv'), index=False)
    print(f"   ✅ {len(users_df)} usuarios generados")
    
    # Generar productos
    print("📦 Generando productos...")
    products_df = generate_products(500)
    products_df.to_csv(os.path.join(data_dir, 'products.csv'), index=False)
    print(f"   ✅ {len(products_df)} productos generados")
    
    # Generar transacciones
    print("💳 Generando transacciones...")
    transactions_df = generate_transactions(users_df, products_df, 10000)
    transactions_df.to_csv(os.path.join(data_dir, 'sample_data.csv'), index=False)
    print(f"   ✅ {len(transactions_df)} transacciones generadas")
    
    # Mostrar estadísticas
    print("\n📊 Resumen de datos generados:")
    print(f"   • Usuarios: {len(users_df):,}")
    print(f"   • Productos: {len(products_df):,}")
    print(f"   • Transacciones: {len(transactions_df):,}")
    print(f"   • Periodo: {transactions_df['timestamp'].min()} - {transactions_df['timestamp'].max()}")
    print(f"   • Valor total: ${transactions_df['price'].sum():,.2f}")
    
    print("\n🎉 ¡Datasets generados exitosamente en la carpeta 'data/'!")

if __name__ == "__main__":
    main()