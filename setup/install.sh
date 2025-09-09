#!/bin/bash

# ===============================================
# SCRIPT DE INSTALACIÓN - DATA ENGINEERING EVAL
# ===============================================
# 
# Este script configura el entorno completo para
# la evaluación de Data Engineering
#
# ===============================================

set -e  # Salir en caso de error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para logging
log_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

log_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

log_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

log_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Banner
echo "==============================================="
echo "🚀 DATA ENGINEERING EVALUATION SETUP"
echo "==============================================="
echo ""

# 1. Verificar prerequisitos
log_info "Verificando prerequisitos del sistema..."

# Verificar Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    log_success "Python $PYTHON_VERSION encontrado"
else
    log_error "Python 3 no está instalado. Por favor instala Python 3.8 o superior."
    exit 1
fi

# Verificar pip
if command -v pip3 &> /dev/null; then
    log_success "pip3 encontrado"
else
    log_error "pip3 no está instalado. Por favor instala pip."
    exit 1
fi

# Verificar Java (para PySpark)
if command -v java &> /dev/null; then
    JAVA_VERSION=$(java -version 2>&1 | head -n 1 | cut -d'"' -f2)
    log_success "Java $JAVA_VERSION encontrado"
else
    log_warning "Java no encontrado. PySpark puede fallar."
    log_info "Para instalar Java: sudo apt-get install default-jdk"
fi

# Verificar Git
if command -v git &> /dev/null; then
    log_success "Git encontrado"
else
    log_error "Git no está instalado."
    exit 1
fi

echo ""

# 2. Crear entorno virtual (opcional pero recomendado)
log_info "¿Deseas crear un entorno virtual? (recomendado) [y/N]"
read -r create_venv

if [[ $create_venv =~ ^[Yy]$ ]]; then
    log_info "Creando entorno virtual..."
    python3 -m venv data_eng_env
    source data_eng_env/bin/activate
    log_success "Entorno virtual creado y activado"
    
    # Actualizar pip en el venv
    pip install --upgrade pip
else
    log_warning "Continuando sin entorno virtual"
fi

echo ""

# 3. Instalar dependencias de Python
log_info "Instalando dependencias de Python..."

if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    log_success "Dependencias instaladas desde requirements.txt"
else
    log_error "requirements.txt no encontrado"
    exit 1
fi

echo ""

# 4. Configurar JAVA_HOME si es necesario
if [ -z "$JAVA_HOME" ]; then
    log_warning "JAVA_HOME no está configurado"
    
    # Intentar encontrar Java automáticamente
    if [ -d "/usr/lib/jvm/default-java" ]; then
        export JAVA_HOME="/usr/lib/jvm/default-java"
        echo "export JAVA_HOME=/usr/lib/jvm/default-java" >> ~/.bashrc
        log_success "JAVA_HOME configurado automáticamente"
    else
        log_warning "Por favor configura JAVA_HOME manualmente para PySpark"
    fi
fi

echo ""

# 5. Generar datos de ejemplo
log_info "Generando datos de ejemplo..."

if [ -f "setup/generate_data.py" ]; then
    python setup/generate_data.py
    log_success "Datos de ejemplo generados"
else
    log_error "Script generate_data.py no encontrado"
    exit 1
fi

echo ""

# 6. Configurar Jupyter (si está instalado)
if command -v jupyter &> /dev/null; then
    log_info "Configurando Jupyter Notebook..."
    
    # Instalar kernel de Python
    python -m ipykernel install --user --name=data_eng_env --display-name="Data Engineering"
    
    log_success "Jupyter configurado"
    log_info "Para iniciar Jupyter: jupyter notebook"
else
    log_info "Jupyter no encontrado (opcional)"
fi

echo ""

# 7. Validar instalación
log_info "Validando instalación..."

if [ -f "setup/test_setup.py" ]; then
    python setup/test_setup.py
else
    log_warning "Script de validación no encontrado"
fi

echo ""

# 8. Mostrar resumen
echo "==============================================="
echo "🎉 INSTALACIÓN COMPLETADA"
echo "==============================================="
echo ""

log_success "Entorno configurado correctamente"
echo ""

echo "📁 Estructura del proyecto:"
echo "   ├── data/          # Datasets generados"  
echo "   ├── sql/           # Ejercicios SQL"
echo "   ├── pyspark/       # Ejercicios PySpark"
echo "   ├── python/        # Ejercicios Python"
echo "   └── setup/         # Scripts de configuración"
echo ""

echo "🚀 Próximos pasos:"
echo "   1. Revisa el README.md principal"
echo "   2. Explora los datos: ls data/"
echo "   3. Comienza con SQL: cd sql/exercises/"
echo "   4. Prueba PySpark: python pyspark/exercises/01_dataframes_basicos.py"
echo "   5. Ejecuta Python: python python/exercises/01_pandas_basico.py"
echo ""

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "💡 Para activar el entorno virtual en futuras sesiones:"
    echo "   source data_eng_env/bin/activate"
    echo ""
fi

echo "📚 Documentación completa en cada carpeta/README.md"
echo ""
echo "¡Buena suerte con la evaluación! 🍀"