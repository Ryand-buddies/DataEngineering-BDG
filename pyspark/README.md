# Ejercicios de PySpark

Esta sección contiene ejercicios para evaluar habilidades en Apache Spark con Python, enfocándose en procesamiento distribuido de big data.

## 🎯 Objetivos de Evaluación

- **DataFrames**: Creación, transformación y acciones básicas
- **RDDs**: Operaciones de bajo nivel cuando sea necesario  
- **Transformaciones**: map, filter, groupBy, join, window functions
- **Acciones**: collect, count, reduce, save
- **Optimización**: Broadcast variables, caching, partitioning
- **Streaming**: Structured Streaming (básico)
- **SQL**: Spark SQL y Catalyst optimizer

## 📊 Datasets Utilizados

Los ejercicios utilizan los siguientes datasets (en `/data/`):
- `sample_data.csv` - Transacciones (para simular big data)
- `users.csv` - Usuarios 
- `products.csv` - Productos

## 🔧 Setup de PySpark

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Crear SparkSession
spark = SparkSession.builder \
    .appName("DataEngineering-Evaluation") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

# Configurar nivel de log
spark.sparkContext.setLogLevel("WARN")
```

## 📝 Lista de Ejercicios

### Nivel Básico (1-3)
1. **DataFrames Básicos**: Lectura, filtros y transformaciones
2. **Agregaciones**: GroupBy y funciones de agregación 
3. **JOINs**: Diferentes tipos de joins entre DataFrames

### Nivel Intermedio (4-6) 
4. **Window Functions**: Análisis temporal y rankings
5. **UDFs**: User Defined Functions personalizadas
6. **Optimización**: Caching y broadcast joins

### Nivel Avanzado (7-8)
7. **Streaming**: Procesamiento en tiempo real básico
8. **Performance**: Optimización avanzada y tuning

## 🚀 Cómo Usar

1. **Inicia PySpark**: `pyspark` o Jupyter notebook
2. **Carga los datos**: Lee los CSVs como DataFrames
3. **Ejecuta ejercicios**: Sigue las instrucciones en cada notebook
4. **Valida resultados**: Compara outputs y performance

## 💡 Tips para la Evaluación

- **Lazy Evaluation**: Entiende cuándo se ejecutan las transformaciones
- **Partitioning**: Considera el particionado para mejor performance  
- **Caching**: Usa cache() para DataFrames reutilizados
- **Broadcast**: Para joins con tablas pequeñas
- **Columnar**: Aprovecha el formato columnar de Spark

## 📊 Estructura de Archivos

```
pyspark/
├── README.md                    # Este archivo
├── exercises/
│   ├── 01_dataframes_basicos.py # DataFrames y operaciones básicas  
│   ├── 02_agregaciones.py       # GroupBy y agregaciones
│   ├── 03_joins.py              # Diferentes tipos de JOINs
│   ├── 04_window_functions.py   # Funciones de ventana
│   ├── 05_udfs.py              # User Defined Functions
│   ├── 06_optimizacion.py      # Caching y broadcast
│   ├── 07_streaming.py         # Structured Streaming básico
│   └── 08_performance.py       # Tuning y optimización avanzada
└── utils/
    └── spark_utils.py          # Utilidades comunes
```

## 📈 Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Correctitud | 35% | ¿El código produce el resultado esperado? |
| Performance | 30% | ¿Está optimizado para Spark? |
| Uso de APIs | 20% | ¿Usa las APIs de Spark correctamente? |
| Buenas Prácticas | 15% | ¿Sigue mejores prácticas de Spark? |

## 🔍 Aspectos Clave a Evaluar

### DataFrames vs RDDs
- Cuándo usar cada uno
- Ventajas del Catalyst optimizer
- Type safety con Datasets

### Optimización
- Partitioning strategies
- Join strategies (broadcast, sort-merge)  
- Caching strategies
- Columnar storage benefits

### Configuración
- Memory management
- Executor configuration
- Dynamic allocation

---

**¡Comienza con el Ejercicio 1!** ⚡