#!/usr/bin/env python3
"""
===============================================
EJERCICIO 1: DATAFRAMES BÁSICOS EN PYSPARK
===============================================

Objetivo: Evaluar habilidades básicas con DataFrames de Spark
Tiempo estimado: 20 minutos
Dificultad: ⭐ Básico

===============================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as spark_sum, avg, max as spark_max, min as spark_min
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, TimestampType
import os

# ===============================================
# CONFIGURACIÓN INICIAL
# ===============================================

def create_spark_session():
    """Crear SparkSession para los ejercicios"""
    return SparkSession.builder \
        .appName("DataFrames-Basicos") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

def load_data(spark):
    """Cargar los datasets necesarios"""
    # Get the path relative to the project root
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_path = os.path.join(project_root, "data")
    
    # Cargar transacciones
    transactions_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv(os.path.join(data_path, "sample_data.csv"))
    
    # Cargar usuarios  
    users_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv(os.path.join(data_path, "users.csv"))
        
    # Cargar productos
    products_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv(os.path.join(data_path, "products.csv"))
    
    return transactions_df, users_df, products_df

# ===============================================
# EJERCICIOS
# ===============================================

def ejercicio_1_exploracion(transactions_df):
    """
    EJERCICIO 1 (2 puntos): Exploración básica del DataFrame
    
    Tareas:
    1. Muestra el schema del DataFrame de transacciones
    2. Cuenta el número total de registros
    3. Muestra las primeras 10 filas
    4. Obtén estadísticas descriptivas de las columnas numéricas
    """
    
    print("=== EJERCICIO 1: EXPLORACIÓN BÁSICA ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .printSchema(), .count(), .show(), .describe()
    
    pass

def ejercicio_2_filtros(transactions_df):
    """
    EJERCICIO 2 (3 puntos): Filtros y selección
    
    Tareas:
    1. Filtra transacciones de 'Electronics' con precio > 100
    2. Selecciona solo las columnas: transaction_id, product_name, price, country
    3. Ordena por precio descendente
    4. Muestra los resultados
    """
    
    print("\n=== EJERCICIO 2: FILTROS Y SELECCIÓN ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .filter(), .select(), .orderBy()
    
    pass

def ejercicio_3_agregaciones_simples(transactions_df):
    """
    EJERCICIO 3 (4 puntos): Agregaciones básicas
    
    Tareas:
    1. Calcula el revenue total por país
    2. Encuentra el precio promedio por categoría  
    3. Cuenta transacciones por método de pago
    4. Muestra los resultados ordenados apropiadamente
    """
    
    print("\n=== EJERCICIO 3: AGREGACIONES BÁSICAS ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .groupBy(), .agg(), .sum(), .avg(), .count()
    
    pass

def ejercicio_4_transformaciones(transactions_df):
    """
    EJERCICIO 4 (4 puntos): Transformaciones de columnas
    
    Tareas:
    1. Crea una columna 'total_amount' = price * quantity
    2. Crea una columna 'price_category' que clasifique:
       - 'Low': < 50
       - 'Medium': 50-150  
       - 'High': > 150
    3. Extrae el año de la columna timestamp como 'year'
    4. Muestra el DataFrame transformado
    """
    
    print("\n=== EJERCICIO 4: TRANSFORMACIONES ===")
    
    # TODO: Implementa aquí tu código  
    # Pista: usa .withColumn(), .when(), .otherwise(), year()
    
    pass

def ejercicio_bonus_performance(transactions_df):
    """
    EJERCICIO BONUS (2 puntos): Consideraciones de performance
    
    Tareas:
    1. Cachea el DataFrame de transacciones
    2. Cuenta las particiones del DataFrame
    3. Reparticiona por país (4 particiones)
    4. Compara el plan de ejecución antes y después
    """
    
    print("\n=== EJERCICIO BONUS: PERFORMANCE ===")
    
    # TODO: Implementa aquí tu código
    # Pista: usa .cache(), .rdd.getNumPartitions(), .repartition(), .explain()
    
    pass

# ===============================================
# FUNCIÓN PRINCIPAL
# ===============================================

def main():
    """Función principal que ejecuta todos los ejercicios"""
    
    # Crear SparkSession
    spark = create_spark_session()
    spark.sparkContext.setLogLevel("WARN")
    
    try:
        # Cargar datos
        print("🚀 Cargando datos...")
        transactions_df, users_df, products_df = load_data(spark)
        
        # Ejecutar ejercicios
        ejercicio_1_exploracion(transactions_df)
        ejercicio_2_filtros(transactions_df) 
        ejercicio_3_agregaciones_simples(transactions_df)
        ejercicio_4_transformaciones(transactions_df)
        ejercicio_bonus_performance(transactions_df)
        
        print("\n✅ ¡Ejercicios completados!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    finally:
        # Cerrar SparkSession
        spark.stop()

if __name__ == "__main__":
    main()

# ===============================================
# RESULTADOS ESPERADOS
# ===============================================
"""
Ejercicio 1: Schema, count, primeras filas, estadísticas
Ejercicio 2: Transacciones de Electronics > $100 ordenadas por precio
Ejercicio 3: Revenue por país, precio avg por categoría, transacciones por payment method
Ejercicio 4: DataFrame con total_amount, price_category, year
Bonus: DataFrame cacheado y reparticionado con planes de ejecución
"""