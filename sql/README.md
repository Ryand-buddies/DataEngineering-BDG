# Ejercicios de SQL

Esta sección contiene ejercicios para evaluar habilidades en SQL, desde consultas básicas hasta análisis complejos.

## 🎯 Objetivos de Evaluación

- **Consultas básicas**: SELECT, WHERE, ORDER BY, GROUP BY
- **JOINs**: INNER, LEFT, RIGHT, FULL OUTER JOIN
- **Funciones de ventana**: ROW_NUMBER, RANK, LAG, LEAD
- **CTEs**: Common Table Expressions para consultas complejas
- **Agregaciones**: COUNT, SUM, AVG, MIN, MAX con HAVING
- **Subconsultas**: Correlated y non-correlated subqueries
- **Optimización**: Índices, planes de ejecución

## 📊 Datasets Utilizados

Los ejercicios utilizan los siguientes datasets (en `/data/`):
- `sample_data.csv` - Transacciones de e-commerce
- `users.csv` - Información de usuarios
- `products.csv` - Catálogo de productos

## 📝 Lista de Ejercicios

### Nivel Básico (1-3)
1. **Consultas Básicas**: Filtros y ordenamiento
2. **Agregaciones Simples**: Group by y funciones de agregación
3. **JOINs Básicos**: Inner y left joins

### Nivel Intermedio (4-7)
4. **Funciones de Ventana**: Ranking y análisis temporal
5. **CTEs**: Consultas recursivas y jerárquicas
6. **Subconsultas**: Consultas correlacionadas
7. **Análisis Temporal**: Trends y patrones por fecha

### Nivel Avanzado (8-10)
8. **Optimización**: Mejora de performance en consultas complejas
9. **Análisis Cohort**: Análisis de retención de usuarios
10. **Métricas de Negocio**: KPIs complejos y dashboards

## 🚀 Cómo Usar

1. **Configura tu entorno SQL**: Usa SQLite, PostgreSQL, o MySQL
2. **Carga los datos**: Importa los CSVs a tu base de datos
3. **Ejecuta los ejercicios**: Sigue las instrucciones en cada archivo
4. **Valida resultados**: Compara con los outputs esperados

## 💡 Tips para la Evaluación

- **Legibilidad**: Usa indentación consistente y nombres descriptivos
- **Performance**: Considera el uso de índices y optimización
- **Buenas prácticas**: Evita SELECT *, usa alias claros
- **Documentación**: Comenta consultas complejas

## 🔧 Setup Rápido con SQLite

```sql
-- Crear tablas
CREATE TABLE transactions AS SELECT * FROM 'sample_data.csv';
CREATE TABLE users AS SELECT * FROM 'users.csv';  
CREATE TABLE products AS SELECT * FROM 'products.csv';

-- Verificar datos cargados
SELECT COUNT(*) FROM transactions;
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM products;
```

## 📈 Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Correctitud | 40% | ¿La consulta produce el resultado correcto? |
| Eficiencia | 25% | ¿La consulta está optimizada? |
| Legibilidad | 20% | ¿El código es claro y bien formateado? |
| Complejidad | 15% | ¿Maneja casos edge y validaciones? |

---

**¡Comienza con el Ejercicio 1!** 📚