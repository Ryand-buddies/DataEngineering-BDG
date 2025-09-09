# Datasets para Ejercicios de Data Engineering

Esta carpeta contiene los datasets utilizados en los ejercicios de evaluación.

## 📊 Datasets Disponibles

### 1. sample_data.csv
**Descripción**: Dataset principal con datos de e-commerce simulados
**Registros**: ~10,000 transacciones
**Campos**:
- `transaction_id`: ID único de la transacción
- `user_id`: ID del usuario
- `product_id`: ID del producto
- `product_name`: Nombre del producto
- `category`: Categoría del producto
- `price`: Precio del producto
- `quantity`: Cantidad comprada
- `timestamp`: Fecha y hora de la transacción
- `country`: País de la transacción
- `payment_method`: Método de pago utilizado

### 2. users.csv
**Descripción**: Información de usuarios
**Campos**:
- `user_id`: ID único del usuario
- `name`: Nombre completo
- `email`: Correo electrónico
- `registration_date`: Fecha de registro
- `age`: Edad del usuario
- `country`: País de residencia

### 3. products.csv
**Descripción**: Catálogo de productos
**Campos**:
- `product_id`: ID único del producto
- `product_name`: Nombre del producto
- `category`: Categoría
- `brand`: Marca
- `cost_price`: Precio de costo
- `selling_price`: Precio de venta

## 🔧 Generación de Datos

Los datos son generados sintéticamente para simular un entorno real de e-commerce.
Puedes regenerar los datos ejecutando:

```bash
python ../setup/generate_data.py
```

## 📈 Uso en Ejercicios

Estos datasets se utilizan en:
- **SQL**: Consultas complejas y análisis
- **PySpark**: Procesamiento distribuido
- **Python**: ETL y análisis con pandas

## 🚨 Nota Importante

Estos son datos sintéticos creados exclusivamente para fines educativos y de evaluación.
No representan datos reales de ninguna empresa o usuario.