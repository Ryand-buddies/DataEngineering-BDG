#!/usr/bin/env python3
"""
===============================================
EJERCICIO 1: PANDAS BÁSICO
===============================================

Objetivo: Evaluar habilidades fundamentales con Pandas
Tiempo estimado: 25 minutos
Dificultad: ⭐ Básico

===============================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

# ===============================================
# CONFIGURACIÓN INICIAL  
# ===============================================

def load_data():
    """Cargar los datasets necesarios"""
    # Get the path relative to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(project_root, "data")
    
    # Cargar datasets
    transactions = pd.read_csv(os.path.join(data_path, "sample_data.csv"))
    users = pd.read_csv(os.path.join(data_path, "users.csv"))
    products = pd.read_csv(os.path.join(data_path, "products.csv"))
    
    return transactions, users, products

# ===============================================
# EJERCICIOS
# ===============================================

def ejercicio_1_exploracion(df):
    """
    EJERCICIO 1 (2 puntos): Exploración inicial del DataFrame
    
    Tareas:
    1. Muestra información básica del DataFrame (shape, dtypes, info)
    2. Obtén estadísticas descriptivas de columnas numéricas
    3. Identifica valores nulos por columna
    4. Muestra las primeras y últimas 5 filas
    
    Args:
        df (pd.DataFrame): DataFrame de transacciones
        
    Returns:
        dict: Diccionario con las estadísticas básicas
    """
    
    print("=== EJERCICIO 1: EXPLORACIÓN INICIAL ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .shape, .dtypes, .info(), .describe(), .isnull().sum()
    
    stats = {
        'shape': None,
        'columns': None,
        'dtypes': None,
        'null_counts': None,
        'numeric_stats': None
    }
    
    return stats

def ejercicio_2_filtrado_indexing(df):
    """
    EJERCICIO 2 (3 puntos): Filtrado e indexing avanzado
    
    Tareas:
    1. Filtra transacciones de 'Electronics' con precio > 100
    2. Obtén las 10 transacciones más caras por país
    3. Selecciona transacciones de los últimos 90 días
    4. Crea un subset con columnas específicas
    
    Args:
        df (pd.DataFrame): DataFrame de transacciones
        
    Returns:
        tuple: (electronics_expensive, top_by_country, recent_transactions)
    """
    
    print("\n=== EJERCICIO 2: FILTRADO E INDEXING ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .loc[], .query(), .nlargest(), .tail()
    
    electronics_expensive = None
    top_by_country = None
    recent_transactions = None
    
    return electronics_expensive, top_by_country, recent_transactions

def ejercicio_3_transformaciones(df):
    """
    EJERCICIO 3 (4 puntos): Transformaciones de datos
    
    Tareas:
    1. Crea columna 'total_amount' = price * quantity
    2. Categoriza precios en 'Low' (<50), 'Medium' (50-150), 'High' (>150)
    3. Extrae año, mes y día de la columna timestamp
    4. Convierte 'country' a categorical para optimizar memoria
    
    Args:
        df (pd.DataFrame): DataFrame de transacciones
        
    Returns:
        pd.DataFrame: DataFrame transformado
    """
    
    print("\n=== EJERCICIO 3: TRANSFORMACIONES ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .assign(), pd.cut(), pd.to_datetime(), .astype('category')
    
    df_transformed = df.copy()
    
    return df_transformed

def ejercicio_4_agregaciones(df):
    """
    EJERCICIO 4 (4 puntos): Agregaciones y groupby
    
    Tareas:
    1. Revenue total por país y categoría
    2. Transacciones promedio por usuario 
    3. Top 5 productos más vendidos (por quantity)
    4. Estadísticas de precio por método de pago
    
    Args:
        df (pd.DataFrame): DataFrame de transacciones
        
    Returns:
        tuple: (revenue_by_country_cat, avg_trans_user, top_products, price_by_payment)
    """
    
    print("\n=== EJERCICIO 4: AGREGACIONES ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .groupby(), .agg(), .sum(), .mean(), .nlargest()
    
    revenue_by_country_cat = None
    avg_trans_user = None
    top_products = None
    price_by_payment = None
    
    return revenue_by_country_cat, avg_trans_user, top_products, price_by_payment

def ejercicio_5_joins_merges(transactions_df, users_df, products_df):
    """
    EJERCICIO 5 (5 puntos): Joins y merges entre DataFrames
    
    Tareas:
    1. Join transactions con users para obtener información demográfica
    2. Merge con products para obtener cost_price y calcular profit
    3. Calcula profit margin por transacción
    4. Identifica usuarios con mayor profit generado
    
    Args:
        transactions_df (pd.DataFrame): Transacciones
        users_df (pd.DataFrame): Usuarios  
        products_df (pd.DataFrame): Productos
        
    Returns:
        pd.DataFrame: DataFrame enriquecido con profit analysis
    """
    
    print("\n=== EJERCICIO 5: JOINS Y MERGES ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .merge(), .join(), calcular profit = selling_price - cost_price
    
    enriched_df = None
    
    return enriched_df

def ejercicio_bonus_pivot_reshape(df):
    """
    EJERCICIO BONUS (3 puntos): Pivot tables y reshaping
    
    Tareas:
    1. Crea pivot table: países vs categorías con revenue total
    2. Reshaping: melt el pivot para formato largo
    3. Crosstab: método de pago vs categoría con count
    
    Args:
        df (pd.DataFrame): DataFrame de transacciones
        
    Returns:
        tuple: (pivot_revenue, melted_df, payment_category_crosstab)
    """
    
    print("\n=== EJERCICIO BONUS: PIVOT Y RESHAPE ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .pivot_table(), .melt(), pd.crosstab()
    
    pivot_revenue = None
    melted_df = None
    payment_category_crosstab = None
    
    return pivot_revenue, melted_df, payment_category_crosstab

# ===============================================
# FUNCIÓN PRINCIPAL
# ===============================================

def main():
    """Función principal que ejecuta todos los ejercicios"""
    
    try:
        # Cargar datos
        print("🚀 Cargando datos...")
        transactions_df, users_df, products_df = load_data()
        
        # Ejecutar ejercicios
        stats = ejercicio_1_exploracion(transactions_df)
        filtered_data = ejercicio_2_filtrado_indexing(transactions_df)
        transformed_df = ejercicio_3_transformaciones(transactions_df)
        aggregations = ejercicio_4_agregaciones(transactions_df)
        enriched_df = ejercicio_5_joins_merges(transactions_df, users_df, products_df)
        pivot_data = ejercicio_bonus_pivot_reshape(transactions_df)
        
        print("\n✅ ¡Ejercicios completados!")
        
        # Mostrar resumen
        print(f"\n📊 Resumen:")
        print(f"   • Transacciones procesadas: {len(transactions_df):,}")
        print(f"   • Usuarios únicos: {transactions_df['user_id'].nunique():,}")
        print(f"   • Productos únicos: {transactions_df['product_id'].nunique():,}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

# ===============================================
# RESULTADOS ESPERADOS
# ===============================================
"""
Ejercicio 1: Estadísticas básicas del dataset (10K transacciones aprox)
Ejercicio 2: Transacciones filtradas por criterios específicos
Ejercicio 3: DataFrame con columnas adicionales calculadas
Ejercicio 4: Agregaciones por diferentes dimensiones
Ejercicio 5: DataFrame enriquecido con datos de users y products
Bonus: Pivot tables y reshaping para análisis dimensional
"""