# Ejercicios de Python para Data Engineering

Esta sección contiene ejercicios para evaluar habilidades en Python aplicadas a ingeniería de datos, con énfasis en Pandas, ETL pipelines y procesamiento de datos.

## 🎯 Objetivos de Evaluación

- **Pandas**: Manipulación y análisis de DataFrames
- **ETL Pipelines**: Extract, Transform, Load workflows
- **Data Cleaning**: Limpieza y validación de datos
- **File I/O**: Lectura/escritura de diferentes formatos
- **APIs**: Integración con servicios externos
- **Testing**: Unit tests para código de data engineering
- **Performance**: Optimización de código Python

## 📊 Datasets Utilizados

Los ejercicios utilizan los siguientes datasets (en `/data/`):
- `sample_data.csv` - Transacciones de e-commerce
- `users.csv` - Información de usuarios
- `products.csv` - Catálogo de productos

## 🔧 Librerías Principales

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json
import requests
import sqlite3
from sqlalchemy import create_engine
```

## 📝 Lista de Ejercicios

### Nivel Básico (1-3)
1. **Pandas Básico**: Lectura, filtros y manipulación básica
2. **Data Cleaning**: Limpieza y validación de datos
3. **Aggregations**: Agrupaciones y estadísticas descriptivas

### Nivel Intermedio (4-6)
4. **ETL Pipeline**: Pipeline completo de transformación
5. **Time Series**: Análisis de series temporales
6. **Data Validation**: Validación robusta de datos

### Nivel Avanzado (7-8)
7. **API Integration**: Integración con APIs y data enrichment
8. **Performance**: Optimización y testing

## 🚀 Cómo Usar

1. **Setup Python**: Asegúrate de tener Python 3.8+
2. **Instala dependencias**: `pip install -r requirements.txt`
3. **Ejecuta notebooks**: Usa Jupyter o ejecuta scripts directamente
4. **Valida resultados**: Compara outputs esperados

## 💡 Tips para la Evaluación

### Pandas Best Practices
- Usa vectorización en lugar de loops
- Aprovecha `groupby` para agregaciones
- Optimiza memory usage con tipos de datos apropiados
- Usa `query()` para filtros complejos

### ETL Best Practices  
- Separa Extract, Transform, Load en funciones
- Implementa logging y error handling
- Valida datos en cada etapa
- Usa configuration files para parámetros

### Performance Tips
- Profile tu código con `%timeit` 
- Usa `pd.read_csv()` con chunking para archivos grandes
- Considera `dask` para datasets que no caben en memoria
- Optimiza tipos de datos (int8 vs int64, category vs object)

## 📊 Estructura de Archivos

```
python/
├── README.md                       # Este archivo
├── exercises/
│   ├── 01_pandas_basico.py        # Manipulación básica con Pandas
│   ├── 02_data_cleaning.py        # Limpieza y validación
│   ├── 03_agregaciones.py         # Agrupaciones y estadísticas  
│   ├── 04_etl_pipeline.py         # Pipeline ETL completo
│   ├── 05_time_series.py          # Análisis temporal
│   ├── 06_data_validation.py      # Validación robusta
│   ├── 07_api_integration.py      # APIs y enriquecimiento
│   └── 08_performance.py          # Optimización y testing
├── notebooks/
│   └── exploratory_analysis.ipynb # Análisis exploratorio
└── utils/
    ├── data_utils.py              # Utilidades para datos
    ├── validation.py              # Funciones de validación
    └── config.py                  # Configuración
```

## 📈 Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Correctitud | 35% | ¿El código produce el resultado correcto? |
| Eficiencia | 25% | ¿Está optimizado para Python/Pandas? |
| Legibilidad | 25% | ¿El código es claro y está bien documentado? |
| Robustez | 15% | ¿Maneja errores y casos edge? |

## 🔍 Aspectos Clave a Evaluar

### Manipulación de Datos
- Indexing y slicing eficiente
- Merging y joining DataFrames
- Reshaping (pivot, melt, stack/unstack)
- Handling missing data

### ETL Design
- Modular design patterns
- Error handling y logging
- Data validation checkpoints
- Configuration management

### Performance
- Memory-efficient operations
- Vectorización vs loops
- Chunking para big datasets
- Profiling y bottleneck identification

### Testing
- Unit tests para funciones de transformación
- Data quality tests
- Integration tests para pipelines
- Mock external dependencies

---

**¡Comienza con el Ejercicio 1!** 🐍