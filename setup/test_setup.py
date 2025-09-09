#!/usr/bin/env python3
"""
Script de validación para verificar que la instalación sea correcta
"""

import sys
import os
from pathlib import Path

def test_python_version():
    """Verificar versión de Python"""
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor} - Requiere 3.8+")
        return False

def test_libraries():
    """Verificar librerías necesarias"""
    libraries = [
        'pandas',
        'numpy', 
        'pyspark',
        'sqlalchemy',
        'faker',
        'matplotlib'
    ]
    
    all_ok = True
    for lib in libraries:
        try:
            module = __import__(lib)
            if hasattr(module, '__version__'):
                version = module.__version__
            else:
                version = "instalada"
            print(f"✅ {lib} {version} - OK")
        except ImportError:
            print(f"❌ {lib} - NO ENCONTRADA")
            all_ok = False
    
    return all_ok

def test_data_files():
    """Verificar que los archivos de datos existan"""
    data_dir = Path("data")  # Changed from "../data" to "data"
    required_files = [
        "sample_data.csv",
        "users.csv", 
        "products.csv"
    ]
    
    all_ok = True
    if data_dir.exists():
        for file in required_files:
            file_path = data_dir / file
            if file_path.exists():
                print(f"✅ {file} - ENCONTRADO")
            else:
                print(f"❌ {file} - NO ENCONTRADO")
                all_ok = False
    else:
        print("❌ Carpeta data/ no encontrada")
        all_ok = False
    
    return all_ok

def test_pyspark():
    """Verificar que PySpark funcione"""
    try:
        from pyspark.sql import SparkSession
        
        spark = SparkSession.builder \
            .appName("TestSetup") \
            .config("spark.sql.adaptive.enabled", "true") \
            .getOrCreate()
        
        # Test simple
        df = spark.range(10)
        count = df.count()
        
        spark.stop()
        
        if count == 10:
            print("✅ PySpark - OK")
            return True
        else:
            print("❌ PySpark - Error en test básico")
            return False
            
    except Exception as e:
        print(f"❌ PySpark - Error: {e}")
        return False

def test_sqlite():
    """Verificar conectividad con SQLite"""
    try:
        import sqlite3
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        conn.close()
        
        if result[0] == 1:
            print("✅ SQLite - OK")
            return True
        else:
            print("❌ SQLite - Error en test")
            return False
            
    except Exception as e:
        print(f"❌ SQLite - Error: {e}")
        return False

def main():
    """Función principal de validación"""
    print("🔍 VALIDANDO INSTALACIÓN...")
    print("=" * 40)
    
    tests = [
        test_python_version,
        test_libraries,
        test_data_files,
        test_pyspark,
        test_sqlite
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Error en test: {e}")
            results.append(False)
        print()
    
    # Resumen
    print("=" * 40)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print("🎉 ¡Instalación completada exitosamente!")
        print("✅ Todos los tests pasaron")
        print("\n🚀 ¡Listo para comenzar la evaluación!")
    else:
        print(f"⚠️  {passed}/{total} tests pasaron")
        print("❌ Algunos componentes necesitan atención")
        print("\n📋 Revisa los errores arriba y ejecuta:")
        print("   pip install -r requirements.txt")
        print("   python setup/generate_data.py")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)