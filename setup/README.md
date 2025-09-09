# Setup y Configuración

Esta carpeta contiene scripts y archivos de configuración para preparar el entorno de desarrollo y generar los datos de prueba.

## 🔧 Archivos Incluidos

### `install.sh`
Script de instalación que configura todo el entorno:
- Verifica prerequisitos (Python, Java)
- Instala dependencias de Python
- Genera datos de muestra
- Configura Jupyter notebooks
- Valida la instalación

### `generate_data.py`  
Script para generar los datasets sintéticos:
- Crea `users.csv` con información de usuarios
- Genera `products.csv` con catálogo de productos  
- Produce `sample_data.csv` con transacciones
- Utiliza Faker para datos realistas

### `test_setup.py`
Script de validación que verifica:
- Correcta instalación de librerías
- Disponibilidad de datasets
- Funcionamiento básico de PySpark
- Conectividad de base de datos

## 🚀 Instalación Rápida

### Opción 1: Script Automático
```bash
chmod +x setup/install.sh
./setup/install.sh
```

### Opción 2: Manual
```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Generar datos
python setup/generate_data.py

# 3. Validar instalación  
python setup/test_setup.py
```

## 📋 Prerequisitos

### Sistema Operativo
- Linux, macOS, o Windows con WSL
- Git instalado

### Python
- Python 3.8 o superior
- pip package manager
- virtualenv (recomendado)

### Java (para PySpark)
- Java 8 o superior
- Variable JAVA_HOME configurada

### Opcional
- Docker (para entorno consistente)
- Jupyter Notebook
- Base de datos (SQLite incluido, PostgreSQL/MySQL opcional)

## 🐳 Docker Setup (Opcional)

Si prefieres usar Docker para un entorno aislado:

```bash
# Crear imagen
docker build -t data-engineering-eval .

# Ejecutar contenedor
docker run -it --rm -p 8888:8888 data-engineering-eval

# Acceder a Jupyter
# http://localhost:8888
```

## 🔍 Verificación de Instalación

El script `test_setup.py` verifica:

1. **Python Libraries**: pandas, pyspark, numpy, etc.
2. **Data Files**: Existencia y formato correcto de CSVs  
3. **PySpark**: Creación de SparkSession
4. **SQL**: Conectividad con SQLite
5. **Notebooks**: Jupyter kernel disponible

### Salida Esperada
```
✅ Python 3.8.10 - OK
✅ Pandas 1.5.2 - OK  
✅ PySpark 3.3.0 - OK
✅ Datasets encontrados - OK
✅ SparkSession creada - OK
✅ SQLite conexión - OK
🎉 ¡Instalación completada exitosamente!
```

## 🚨 Solución de Problemas

### Error: "Java not found"
```bash
# Instalar Java 8+
sudo apt-get install default-jdk

# Configurar JAVA_HOME
export JAVA_HOME=/usr/lib/jvm/default-java
echo 'export JAVA_HOME=/usr/lib/jvm/default-java' >> ~/.bashrc
```

### Error: "PySpark initialization failed"
```bash
# Verificar Java
java -version

# Verificar JAVA_HOME
echo $JAVA_HOME

# Reinstalar PySpark
pip uninstall pyspark
pip install pyspark==3.3.0
```

### Error: "Permission denied"
```bash
# Dar permisos de ejecución
chmod +x setup/install.sh

# O ejecutar con Python
python setup/generate_data.py
```

### Error: "Module not found"
```bash
# Activar entorno virtual
source venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

## 🎯 Próximos Pasos

Después de completar la instalación:

1. **Explora los datos**: `ls data/`
2. **Ejecuta ejercicios SQL**: `cd sql/exercises/`
3. **Prueba PySpark**: `python pyspark/exercises/01_dataframes_basicos.py`  
4. **Inicia con Python**: `python python/exercises/01_pandas_basico.py`
5. **Jupyter Notebooks**: `jupyter notebook`

## 📞 Soporte

Si encuentras problemas:

1. Revisa los logs de error completos
2. Verifica prerequisitos del sistema
3. Consulta la documentación oficial de las librerías
4. Abre un issue en el repositorio con detalles del error

---

**¡Listo para comenzar la evaluación!** 🚀