# Criterios de Evaluación - Data Engineering

Este documento detalla los criterios y rubrica de evaluación para la prueba de ingeniería de datos.

## 📊 Distribución de Puntajes

### SQL (35 puntos total)
- **Ejercicio 1**: Consultas Básicas (12 puntos)
- **Ejercicio 2**: Window Functions (18 puntos) 
- **Ejercicio 3**: CTEs Avanzadas (22 puntos)
- **Bonus SQL**: (5 puntos adicionales)

### PySpark (35 puntos total)
- **Ejercicio 1**: DataFrames Básicos (15 puntos)
- **Ejercicio 2**: Agregaciones y JOINs (10 puntos)
- **Ejercicio 3**: Window Functions (10 puntos)
- **Bonus PySpark**: (10 puntos adicionales)

### Python (30 puntos total)
- **Ejercicio 1**: Pandas Básico (18 puntos)
- **Ejercicio 2**: ETL Pipeline (28 puntos)
- **Bonus Python**: (6 puntos adicionales)

**Total**: 100 puntos base + 21 puntos bonus

## 🎯 Criterios de Evaluación

### 1. Correctitud (40% del puntaje)
| Nivel | Descripción | Puntos |
|-------|-------------|--------|
| **Excelente** | Solución 100% correcta, maneja todos los casos | 100% |
| **Bueno** | Solución mayormente correcta, casos edge menores | 80% |
| **Regular** | Solución básica funciona, algunos errores | 60% |
| **Deficiente** | Solución parcial o con errores importantes | 30% |
| **Incorrecto** | No funciona o enfoque completamente erróneo | 0% |

### 2. Eficiencia/Performance (25% del puntaje)

#### SQL
- **Excelente**: Uso apropiado de índices, JOINs optimizados, evita subconsultas innecesarias
- **Bueno**: Consulta eficiente, minor optimization opportunities
- **Regular**: Funciona pero podría optimizarse
- **Deficiente**: Ineficiente, scans completos innecesarios

#### PySpark  
- **Excelente**: Uso de broadcast joins, caching apropiado, partitioning considerado
- **Bueno**: Buen uso de transformations/actions, minor optimizations
- **Regular**: Código funciona pero sin optimizaciones
- **Deficiente**: Uso ineficiente de Spark (collect() innecesario, etc.)

#### Python
- **Excelente**: Vectorización, memory-efficient, pandas optimizado
- **Bueno**: Buen uso de pandas APIs, minor inefficiencies  
- **Regular**: Funciona pero con loops o métodos subóptimos
- **Deficiente**: Loops innecesarios, memory leaks, muy lento

### 3. Legibilidad y Buenas Prácticas (20% del puntaje)

#### SQL
- Indentación consistente y clara
- Nombres de columnas y aliases descriptivos
- Comentarios para lógica compleja
- Uso apropiado de CTEs vs subconsultas

#### PySpark
- Código modular y reutilizable
- Manejo apropiado de SparkSession
- Lazy evaluation entendida
- Error handling básico

#### Python  
- PEP 8 compliance
- Funciones bien definidas y documentadas
- Manejo de errores robusto
- Type hints cuando apropiado

### 4. Completitud y Robustez (15% del puntaje)

- **Manejo de casos edge**: Valores nulos, datos vacíos, etc.
- **Validación de datos**: Checks básicos de sanidad
- **Error handling**: Try/catch apropiado
- **Logging**: Mensajes informativos de progreso/errores

## 📝 Evaluación por Sección

### SQL - Aspectos Específicos

#### Consultas Básicas (12 pts)
- [3 pts] Sintaxis correcta y queries ejecutables
- [3 pts] Filtros y JOINs apropiados
- [3 pts] Agregaciones correctas  
- [3 pts] Ordenamiento y formato de resultados

#### Window Functions (18 pts)
- [5 pts] ROW_NUMBER, RANK, DENSE_RANK usados correctamente
- [4 pts] LAG/LEAD para análisis temporal
- [5 pts] Partitioning apropiado
- [4 pts] Cálculos de porcentajes y running totals

#### CTEs Avanzadas (22 pts)
- [6 pts] Análisis de cohort correctamente implementado
- [8 pts] Análisis RFM completo con segmentación
- [5 pts] CTE recursiva para series temporales
- [3 pts] Market basket analysis básico

### PySpark - Aspectos Específicos

#### DataFrames Básicos (15 pts)
- [3 pts] Lectura y exploración de datos
- [4 pts] Transformaciones básicas (filter, select, withColumn)
- [4 pts] Agregaciones con groupBy
- [4 pts] Consideraciones de performance básicas

#### Optimización Avanzada (10 pts)
- [3 pts] Uso apropiado de cache()
- [3 pts] Broadcast joins cuando aplicable
- [2 pts] Partitioning strategies
- [2 pts] Explain plans entendidos

### Python - Aspectos Específicos

#### Pandas Básico (18 pts)
- [4 pts] Exploración y manipulación básica
- [4 pts] Filtrado e indexing avanzado
- [4 pts] Transformaciones de columnas
- [3 pts] Agregaciones complejas
- [3 pts] JOINs entre DataFrames

#### ETL Pipeline (28 pts)
- [4 pts] Extract: Lectura robusta de datos
- [6 pts] Validate: Validaciones comprensivas
- [6 pts] Transform: Transformaciones complejas
- [4 pts] Clean: Limpieza efectiva de datos
- [4 pts] Load: Persistencia de resultados
- [4 pts] Orquestación y error handling

## 🏆 Escalas de Calificación

### Puntaje Final
- **90-100 puntos**: Excelente - Senior Data Engineer level
- **80-89 puntos**: Bueno - Mid-level Data Engineer 
- **70-79 puntos**: Regular - Junior Data Engineer con potencial
- **60-69 puntos**: Básico - Necesita desarrollo adicional
- **< 60 puntos**: Insuficiente - No recomendado para rol

### Consideraciones Especiales

#### Bonus Points (+21 pts max)
- Creatividad en soluciones
- Optimizaciones no solicitadas pero valiosas  
- Documentación excepcional
- Consideraciones de escalabilidad

#### Penalizaciones
- **-5 pts**: Código no ejecutable sin modificaciones
- **-3 pts**: Sintaxis errors básicos
- **-2 pts**: Formato muy pobre o ilegible
- **-1 pt**: Minor style issues

## 📋 Checklist para Evaluadores

### Por cada ejercicio:
- [ ] ¿Ejecuta sin errores?
- [ ] ¿Produce el resultado esperado?
- [ ] ¿Está bien optimizado para el contexto?
- [ ] ¿Es código legible y mantenible?
- [ ] ¿Maneja casos edge básicos?

### Evaluación holística:
- [ ] ¿Demuestra entendimiento profundo de las tecnologías?
- [ ] ¿Sigue mejores prácticas de la industria?
- [ ] ¿Sería código production-ready con minor changes?
- [ ] ¿Muestra potencial para trabajar independientemente?

## 🔄 Proceso de Evaluación

1. **Revisión Inicial** (10 min): Verificar completitud y ejecutabilidad
2. **Evaluación Técnica** (30 min): Revisar cada ejercicio contra rubrica
3. **Evaluación Holística** (10 min): Impresión general y potencial
4. **Feedback** (10 min): Preparar comentarios constructivos
5. **Decisión Final** (5 min): Recomendación basada en puntaje y observaciones

**Tiempo total**: ~65 minutos por candidato

---

**Nota**: Esta evaluación busca identificar candidatos que no solo puedan resolver problemas técnicos, sino que también demuestren las habilidades necesarias para trabajar efectivamente en equipos de data engineering en producción.