#!/usr/bin/env python3
"""
===============================================
EJERCICIO 2: OPTIMIZACIÓN EN PYSPARK
===============================================

Objetivo: Evaluar conocimientos de optimización y performance tuning
Tiempo estimado: 30 minutos
Dificultad: ⭐⭐⭐ Avanzado

===============================================
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.broadcast import Broadcast
import time
import os

def create_optimized_spark_session():
    """Crear SparkSession con configuraciones optimizadas"""
    return SparkSession.builder \
        .appName("Optimizacion-PySpark") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.sql.adaptive.advisoryPartitionSizeInBytes", "128MB") \
        .config("spark.sql.join.preferSortMergeJoin", "true") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .getOrCreate()

def ejercicio_1_broadcast_joins(spark):
    """
    EJERCICIO 1 (4 puntos): Optimización con Broadcast Joins
    
    Tareas:
    1. Identifique qué tabla es candidata para broadcast
    2. Implemente broadcast join manual
    3. Compare performance con join normal  
    4. Analice los execution plans
    
    Args:
        spark: SparkSession
    """
    
    print("=== EJERCICIO 1: BROADCAST JOINS ===")
    
    # Cargar datos
    transactions_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("../../data/sample_data.csv")
    
    products_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("../../data/products.csv")
    
    # TODO: Implementar comparación de performance
    # 1. Join normal
    # 2. Broadcast join manual usando broadcast()
    # 3. Medir tiempos de ejecución
    # 4. Comparar execution plans con .explain()
    
    print("💡 Pista: Usa broadcast(small_df) y time.time() para medir")
    
    pass

def ejercicio_2_caching_strategies(spark):
    """
    EJERCICIO 2 (4 puntos): Estrategias de Caching
    
    Tareas:
    1. Identifique DataFrames que se reutilizan
    2. Aplique diferentes niveles de storage (MEMORY_ONLY, MEMORY_AND_DISK, etc.)
    3. Compare performance con y sin cache
    4. Monitoreé el uso de memoria
    
    Args:
        spark: SparkSession
    """
    
    print("\n=== EJERCICIO 2: CACHING STRATEGIES ===")
    
    transactions_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("../../data/sample_data.csv")
    
    # TODO: Implementar estrategias de caching
    # 1. Crear transformaciones complejas que se reutilicen
    # 2. Aplicar cache() con diferentes storage levels
    # 3. Medir impacto en performance
    # 4. Usar spark.catalog.cacheTable() para SQL caching
    
    print("💡 Pista: StorageLevel.MEMORY_AND_DISK, unpersist()")
    
    pass

def ejercicio_3_partitioning_optimization(spark):
    """
    EJERCICIO 3 (5 puntos): Optimización de Particionado
    
    Tareas:
    1. Analice la distribución actual de particiones
    2. Implemente particionado por columna relevante
    3. Compare performance de queries con diferentes estrategias
    4. Optimize el número de particiones
    
    Args:
        spark: SparkSession
    """
    
    print("\n=== EJERCICIO 3: PARTITIONING OPTIMIZATION ===")
    
    transactions_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("../../data/sample_data.csv")
    
    # TODO: Implementar optimización de particionado
    # 1. Analizar .rdd.getNumPartitions()  
    # 2. .repartition() vs .coalesce()
    # 3. Partitioning por columna (country, category)
    # 4. Medir impacto en agregaciones filtradas
    
    print("💡 Pista: repartition(col('country')), coalesce()")
    
    pass

def ejercicio_4_columnar_optimization(spark):
    """
    EJERCICIO 4 (4 puntos): Optimización Columnar
    
    Tareas:
    1. Optimice la selección de columnas (projection pushdown)
    2. Implemente predicate pushdown en filters
    3. Use formatos columnares eficientes (Parquet)
    4. Compare performance vs CSV
    
    Args:
        spark: SparkSession
    """
    
    print("\n=== EJERCICIO 4: COLUMNAR OPTIMIZATION ===")
    
    # TODO: Implementar optimizaciones columnares
    # 1. Leer solo columnas necesarias
    # 2. Aplicar filtros temprano
    # 3. Guardar como Parquet y comparar
    # 4. Usar .explain(True) para ver optimizaciones aplicadas
    
    print("💡 Pista: .select(), .filter(), .write.parquet()")
    
    pass

def ejercicio_5_window_optimization(spark):
    """
    EJERCICIO 5 (5 puntos): Optimización de Window Functions
    
    Tareas:
    1. Implemente window functions eficientemente
    2. Optimize el partitioning de windows
    3. Reutilice window specifications
    4. Compare diferentes approaches para el mismo resultado
    
    Args:
        spark: SparkSession
    """
    
    print("\n=== EJERCICIO 5: WINDOW OPTIMIZATION ===")
    
    transactions_df = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("../../data/sample_data.csv")
    
    # TODO: Implementar window functions optimizadas
    # 1. Crear window specs reutilizables
    # 2. Optimizar partitioning y ordering
    # 3. Comparar con approaches alternativos (groupBy + join)
    # 4. Medir performance de diferentes strategies
    
    print("💡 Pista: Window.partitionBy(), rangeBetween()")
    
    pass

def ejercicio_bonus_adaptive_query(spark):
    """
    EJERCICIO BONUS (3 puntos): Adaptive Query Execution
    
    Tareas:
    1. Analice el impacto de AQE en queries complejas
    2. Configure parámetros de AQE optimalmente
    3. Compare execution plans con y sin AQE
    4. Identifique casos donde AQE ayuda más
    
    Args:
        spark: SparkSession
    """
    
    print("\n=== EJERCICIO BONUS: ADAPTIVE QUERY EXECUTION ===")
    
    # TODO: Implementar análisis de AQE
    # 1. Disable/enable AQE y comparar
    # 2. Analizar join strategy changes
    # 3. Observar partition coalescing
    # 4. Medir impacto en queries con skew
    
    print("💡 Pista: spark.sql.adaptive.enabled, .explain('cost')")
    
    pass

def benchmark_query(spark, query_func, description, iterations=3):
    """Función utilitaria para benchmark de queries"""
    print(f"\n⏱️ Benchmarking: {description}")
    
    times = []
    for i in range(iterations):
        start = time.time()
        query_func()
        end = time.time()
        times.append(end - start)
        print(f"  Iteración {i+1}: {end-start:.2f}s")
    
    avg_time = sum(times) / len(times)
    print(f"  ⏱️ Tiempo promedio: {avg_time:.2f}s")
    
    return avg_time

def analyze_execution_plan(df, description):
    """Función utilitaria para analizar execution plans"""
    print(f"\n📊 Execution Plan - {description}")
    print("=" * 50)
    df.explain(True)
    print("=" * 50)

def main():
    """Función principal"""
    
    # Crear SparkSession optimizada
    spark = create_optimized_spark_session()
    spark.sparkContext.setLogLevel("WARN")
    
    try:
        print("🚀 Iniciando ejercicios de optimización PySpark...")
        
        # Ejecutar ejercicios
        ejercicio_1_broadcast_joins(spark)
        ejercicio_2_caching_strategies(spark) 
        ejercicio_3_partitioning_optimization(spark)
        ejercicio_4_columnar_optimization(spark)
        ejercicio_5_window_optimization(spark)
        ejercicio_bonus_adaptive_query(spark)
        
        print("\n✅ ¡Ejercicios de optimización completados!")
        
        # Mostrar estadísticas finales del SparkContext
        sc = spark.sparkContext
        print(f"\n📊 Estadísticas de SparkContext:")
        print(f"   • Aplicación: {sc.appName}")  
        print(f"   • Master: {sc.master}")
        print(f"   • Versión Spark: {sc.version}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Limpiar recursos
        spark.stop()

if __name__ == "__main__":
    main()

# ===============================================
# RESULTADOS ESPERADOS
# ===============================================
"""
Ejercicio 1: Comparación de performance entre join normal y broadcast join
Ejercicio 2: Impacto del caching en queries repetitivas  
Ejercicio 3: Mejora de performance con particionado optimizado
Ejercicio 4: Ventajas del formato Parquet vs CSV
Ejercicio 5: Window functions optimizadas para grandes datasets
Bonus: Beneficios de Adaptive Query Execution en joins complejos

📈 Performance Improvements Esperados:
• Broadcast joins: 2-5x más rápido para joins con tablas pequeñas
• Caching: 3-10x más rápido en queries repetitivas
• Partitioning: 2-4x más rápido en queries filtradas
• Parquet: 5-20x más rápido que CSV para analytics
• AQE: 10-30% mejora en queries complejas
"""