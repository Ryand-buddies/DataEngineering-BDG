#!/usr/bin/env python3
"""
===============================================
EJERCICIO 2: ETL PIPELINE
===============================================

Objetivo: Crear un pipeline ETL completo y robusto
Tiempo estimado: 35 minutos
Dificultad: ⭐⭐ Intermedio

===============================================
"""

import pandas as pd
import numpy as np
from datetime import datetime
import logging
from pathlib import Path
import json
from typing import Dict, List, Any

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ETLPipeline:
    """
    Pipeline ETL para procesar datos de e-commerce
    """
    
    def __init__(self, config: Dict[str, Any]):
        """Inicializar pipeline con configuración"""
        self.config = config
        self.data = {}
        self.transformed_data = {}
        
    def extract(self) -> Dict[str, pd.DataFrame]:
        """
        EJERCICIO 2.1 (3 puntos): Implementar extracción de datos
        
        Tareas:
        1. Leer archivos CSV desde la ruta configurada
        2. Validar que los archivos existen
        3. Manejar errores de lectura gracefulmente
        4. Log del progreso
        
        Returns:
            Dict con DataFrames cargados
        """
        
        logger.info("🔄 Iniciando extracción de datos...")
        
        # TODO: Implementar extracción
        # Pista: usar Path, pd.read_csv, try/except, logging
        
        extracted_data = {}
        
        return extracted_data
    
    def validate_data(self, df: pd.DataFrame, table_name: str) -> bool:
        """
        EJERCICIO 2.2 (4 puntos): Implementar validación de datos
        
        Tareas:
        1. Verificar que no esté vacío
        2. Verificar columnas requeridas
        3. Detectar duplicados
        4. Validar tipos de datos
        5. Detectar outliers en campos numéricos
        
        Args:
            df: DataFrame a validar
            table_name: Nombre de la tabla
            
        Returns:
            True si pasa todas las validaciones
        """
        
        logger.info(f"🔍 Validando datos de {table_name}...")
        
        # TODO: Implementar validaciones
        # Pista: usar .empty, .duplicated(), .dtypes, .isnull()
        
        validation_passed = True
        
        return validation_passed
    
    def clean_data(self, df: pd.DataFrame, table_name: str) -> pd.DataFrame:
        """
        EJERCICIO 2.3 (5 puntos): Implementar limpieza de datos
        
        Tareas:
        1. Remover duplicados
        2. Manejar valores nulos (estrategias diferentes por columna)
        3. Standardizar formatos de texto (trim, lowercase)
        4. Corregir tipos de datos
        5. Filtrar outliers extremos
        
        Args:
            df: DataFrame a limpiar
            table_name: Nombre de la tabla
            
        Returns:
            DataFrame limpio
        """
        
        logger.info(f"🧹 Limpiando datos de {table_name}...")
        
        # TODO: Implementar limpieza
        # Pista: .drop_duplicates(), .fillna(), .str.strip(), .astype()
        
        cleaned_df = df.copy()
        
        return cleaned_df
    
    def transform_transactions(self, transactions_df: pd.DataFrame) -> pd.DataFrame:
        """
        EJERCICIO 2.4 (6 puntos): Transformaciones específicas para transacciones
        
        Tareas:
        1. Crear columna total_amount = price * quantity
        2. Categorizar transacciones por valor (Low/Medium/High/Premium)
        3. Extraer componentes de fecha (year, month, day, weekday)
        4. Crear flag de weekend
        5. Calcular días desde primera transacción del usuario
        6. Agregar columna de season basada en el mes
        
        Args:
            transactions_df: DataFrame de transacciones
            
        Returns:
            DataFrame transformado
        """
        
        logger.info("⚙️ Aplicando transformaciones específicas...")
        
        # TODO: Implementar transformaciones
        # Pista: .assign(), pd.cut(), pd.to_datetime(), .dt accessor
        
        transformed_df = transactions_df.copy()
        
        return transformed_df
    
    def create_aggregations(self) -> Dict[str, pd.DataFrame]:
        """
        EJERCICIO 2.5 (4 puntos): Crear tablas agregadas para analytics
        
        Tareas:
        1. User summary: métricas por usuario
        2. Product summary: métricas por producto  
        3. Daily summary: métricas diarias
        4. Country summary: métricas por país
        
        Returns:
            Dict con DataFrames agregados
        """
        
        logger.info("📊 Creando agregaciones...")
        
        # TODO: Implementar agregaciones
        # Pista: .groupby(), .agg(), múltiples métricas por grupo
        
        aggregations = {}
        
        return aggregations
    
    def load_data(self, output_path: str) -> None:
        """
        EJERCICIO 2.6 (3 puntos): Cargar datos transformados
        
        Tareas:
        1. Guardar DataFrames transformados como CSV
        2. Crear metadatos del proceso (timestamp, counts, etc.)
        3. Guardar resumen en JSON
        4. Crear estructura de directorios si no existe
        
        Args:
            output_path: Ruta donde guardar los archivos
        """
        
        logger.info(f"💾 Cargando datos a {output_path}...")
        
        # TODO: Implementar carga
        # Pista: Path.mkdir(), .to_csv(), json.dump()
        
        pass
    
    def run_pipeline(self) -> Dict[str, Any]:
        """
        EJERCICIO 2.7 (3 puntos): Ejecutar pipeline completo
        
        Orquesta todo el proceso ETL con manejo de errores
        
        Returns:
            Resumen de la ejecución
        """
        
        start_time = datetime.now()
        logger.info("🚀 Iniciando pipeline ETL...")
        
        try:
            # TODO: Implementar orquestación completa
            # 1. Extract
            # 2. Validate
            # 3. Clean  
            # 4. Transform
            # 5. Aggregate
            # 6. Load
            
            execution_summary = {
                'status': 'success',
                'start_time': start_time,
                'end_time': datetime.now(),
                'records_processed': 0,
                'errors': []
            }
            
            return execution_summary
            
        except Exception as e:
            logger.error(f"❌ Error en pipeline: {e}")
            raise

def load_config() -> Dict[str, Any]:
    """Cargar configuración del pipeline"""
    return {
        'input_path': '../../data',
        'output_path': '/tmp/etl_output',
        'files': {
            'transactions': 'sample_data.csv',
            'users': 'users.csv',
            'products': 'products.csv'
        },
        'validation_rules': {
            'max_nulls_percent': 0.1,
            'required_columns': {
                'transactions': ['transaction_id', 'user_id', 'product_id', 'price'],
                'users': ['user_id', 'name', 'email'],
                'products': ['product_id', 'product_name', 'category']
            }
        }
    }

def main():
    """Función principal"""
    
    # Cargar configuración
    config = load_config()
    
    # Crear y ejecutar pipeline
    pipeline = ETLPipeline(config)
    
    try:
        result = pipeline.run_pipeline()
        
        # Mostrar resumen
        duration = result['end_time'] - result['start_time']
        logger.info(f"✅ Pipeline completado en {duration}")
        logger.info(f"📊 Registros procesados: {result['records_processed']:,}")
        
        if result['errors']:
            logger.warning(f"⚠️ {len(result['errors'])} errores encontrados")
    
    except Exception as e:
        logger.error(f"💥 Pipeline falló: {e}")
        raise

if __name__ == "__main__":
    main()

# ===============================================
# RESULTADOS ESPERADOS
# ===============================================
"""
✅ Pipeline ejecutado completamente
📁 Archivos generados en /tmp/etl_output/:
   ├── transactions_clean.csv
   ├── user_summary.csv  
   ├── product_summary.csv
   ├── daily_summary.csv
   ├── country_summary.csv
   └── pipeline_metadata.json

📊 Métricas esperadas:
   • ~10K transacciones procesadas
   • ~1K usuarios únicos
   • ~500 productos únicos
   • 0 duplicados después de limpieza
   • <5% valores nulos manejados
"""