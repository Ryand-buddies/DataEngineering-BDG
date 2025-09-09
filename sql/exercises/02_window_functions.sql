-- ===============================================
-- EJERCICIO 2: WINDOW FUNCTIONS
-- ===============================================
-- 
-- Objetivo: Evaluar conocimiento de funciones de ventana
-- Tiempo estimado: 25 minutos  
-- Dificultad: ⭐⭐ Intermedio
--
-- ===============================================

-- PREGUNTA 1 (3 puntos)
-- Asigna un ranking a los usuarios basado en su gasto total
-- Usa ROW_NUMBER, RANK y DENSE_RANK
-- Muestra: user_id, name, total_spent, row_num, rank_val, dense_rank_val

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 2 (4 puntos)
-- Para cada producto, calcula el porcentaje que representa cada transacción
-- del total de ventas de ese producto
-- Muestra: transaction_id, product_name, price, quantity, percent_of_product_sales

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 3 (4 puntos)
-- Calcula la diferencia de días entre transacciones consecutivas para cada usuario
-- Usa LAG para obtener la transacción anterior
-- Muestra: user_id, transaction_id, timestamp, days_since_last_transaction

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 4 (4 puntos)
-- Identifica las 3 transacciones más altas por categoría en cada mes
-- Muestra: year_month, category, transaction_id, price, rank_in_category_month

-- TU CÓDIGO AQUÍ:




-- PREGUNTA BONUS (3 puntos)
-- Calcula un running total del revenue por país, ordenado por fecha
-- Muestra: country, date, daily_revenue, running_total

-- TU CÓDIGO AQUÍ:




-- ===============================================
-- RESULTADOS ESPERADOS  
-- ===============================================
--
-- Pregunta 1: Rankings de usuarios por gasto con diferentes métodos
-- Pregunta 2: Porcentaje que representa cada venta del total por producto
-- Pregunta 3: Días entre transacciones consecutivas por usuario  
-- Pregunta 4: Top 3 transacciones por categoría y mes
-- Bonus: Running total de revenue por país
--
-- ===============================================