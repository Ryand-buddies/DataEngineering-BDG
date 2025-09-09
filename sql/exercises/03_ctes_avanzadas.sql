-- ===============================================
-- EJERCICIO 3: CTEs AVANZADAS Y ANÁLISIS COMPLEJO
-- ===============================================
-- 
-- Objetivo: Evaluar dominio de CTEs recursivas y análisis complejos
-- Tiempo estimado: 30 minutos
-- Dificultad: ⭐⭐⭐ Avanzado
--
-- ===============================================

-- PREGUNTA 1 (4 puntos)
-- Análisis de Cohort: Calcula la retención mensual de usuarios
-- Para cada mes de registro, muestra cuántos usuarios volvieron
-- en los siguientes 3 meses
-- 
-- Resultado esperado:
-- registration_month | month_0 | month_1 | month_2 | month_3 | retention_rate_m1

WITH monthly_cohorts AS (
    -- TODO: Identifica el mes de registro de cada usuario
    -- Pista: DATE_TRUNC('month', registration_date)
    SELECT 1
),
user_activity AS (
    -- TODO: Para cada usuario, identifica en qué meses tuvo actividad
    -- Pista: JOIN transactions con users, agrupar por user_id y mes
    SELECT 1  
),
cohort_analysis AS (
    -- TODO: Calcula cuántos usuarios de cada cohort estuvieron activos cada mes
    -- Pista: Usar CASE WHEN para contar usuarios activos por período
    SELECT 1
)
-- TU CÓDIGO AQUÍ:
SELECT 'TODO: Implementar análisis de cohort' as resultado;




-- PREGUNTA 2 (5 puntos)  
-- Análisis RFM (Recency, Frequency, Monetary): 
-- Segmenta usuarios en base a:
-- - R: Días desde última transacción
-- - F: Número total de transacciones  
-- - M: Valor monetario total
-- Asigna scores 1-5 para cada dimensión y clasifica en segmentos

WITH rfm_calculation AS (
    -- TODO: Calcula métricas RFM por usuario
    -- Recency: días desde última compra
    -- Frequency: número de transacciones
    -- Monetary: valor total gastado
    SELECT 1
),
rfm_scores AS (
    -- TODO: Asigna scores 1-5 usando NTILE o CASE WHEN
    -- Score 5 = mejor (más reciente, más frecuente, más valioso)
    SELECT 1
),
rfm_segments AS (
    -- TODO: Clasifica usuarios en segmentos de negocio:
    -- Champions (R:5, F:5, M:5), Loyal (R:4-5, F:3-5, M:3-5), etc.
    SELECT 1
)
-- TU CÓDIGO AQUÍ:
SELECT 'TODO: Implementar análisis RFM' as resultado;




-- PREGUNTA 3 (4 puntos)
-- CTE Recursiva: Crea una serie temporal de días y calcula
-- el revenue acumulativo. Para días sin ventas, muestra 0
-- pero mantén el running total
-- Período: últimos 30 días desde la transacción más reciente

WITH RECURSIVE date_series AS (
    -- Base case: fecha más reciente menos 29 días
    SELECT 
        (SELECT DATE(MAX(timestamp)) - INTERVAL '29 days' FROM transactions) as date_val
    
    UNION ALL
    
    -- Recursive case: agregar un día hasta llegar a la fecha máxima
    SELECT 
        date_val + INTERVAL '1 day'
    FROM date_series
    WHERE date_val < (SELECT DATE(MAX(timestamp)) FROM transactions)
),
daily_revenue AS (
    -- TODO: Calcula revenue diario (puede ser 0 para algunos días)
    SELECT 1
)
-- TU CÓDIGO AQUÍ:
SELECT 'TODO: Implementar serie temporal con CTE recursiva' as resultado;




-- PREGUNTA 4 (5 puntos)
-- Análisis de Market Basket: Encuentra combinaciones de productos 
-- que se compran juntos frecuentemente
-- Calcula support, confidence y lift para pares de productos

WITH transaction_products AS (
    -- TODO: Obtén todos los productos por transacción
    -- Una fila por (transaction_id, product_id)
    SELECT 1
),
product_pairs AS (
    -- TODO: Genera todos los pares de productos dentro de cada transacción
    -- Self-join para encontrar productos comprados juntos
    SELECT 1
),
pair_metrics AS (
    -- TODO: Calcula métricas de market basket:
    -- Support = freq(A,B) / total_transactions
    -- Confidence = freq(A,B) / freq(A) 
    -- Lift = confidence / support(B)
    SELECT 1
)
-- TU CÓDIGO AQUÍ:
SELECT 'TODO: Implementar análisis Market Basket' as resultado;




-- PREGUNTA BONUS (3 puntos)
-- Detección de Anomalías: Identifica días con revenue inusualmente alto o bajo
-- Usa estadísticas móviles (media y desviación estándar de 7 días)
-- para detectar valores que están >2 desviaciones estándar de la media

WITH daily_metrics AS (
    -- TODO: Calcula revenue diario
    SELECT 1
),
moving_stats AS (
    -- TODO: Calcula media y desviación estándar móvil de 7 días
    -- Usa window functions con frame specification
    SELECT 1
),
anomaly_detection AS (
    -- TODO: Identifica anomalías usando z-score > 2
    -- z_score = (valor - media) / std_dev
    SELECT 1
)
-- TU CÓDIGO AQUÍ:
SELECT 'TODO: Implementar detección de anomalías' as resultado;




-- ===============================================
-- RESULTADOS ESPERADOS
-- ===============================================
--
-- Pregunta 1: Tabla de retención mensual por cohorte
-- Pregunta 2: Usuarios segmentados con scores RFM y clasificación  
-- Pregunta 3: Serie temporal completa con revenue acumulativo
-- Pregunta 4: Pares de productos con métricas de market basket
-- Bonus: Días identificados como anómalos con z-scores
--
-- ===============================================