-- ===============================================
-- EJERCICIO 1: CONSULTAS BÁSICAS
-- ===============================================
-- 
-- Objetivo: Evaluar habilidades básicas en SQL
-- Tiempo estimado: 15 minutos
-- Dificultad: ⭐ Básico
--
-- ===============================================

-- PREGUNTA 1 (2 puntos)
-- Obtén todas las transacciones del país 'Spain' ordenadas por timestamp descendente
-- Muestra: transaction_id, user_id, product_name, price, timestamp

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 2 (2 puntos)  
-- Encuentra los 10 productos más caros del catálogo
-- Muestra: product_name, category, selling_price

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 3 (3 puntos)
-- Calcula el total de ingresos por categoría de producto
-- Muestra: category, total_revenue, transaction_count
-- Ordena por total_revenue descendente

-- TU CÓDIGO AQUÍ:




-- PREGUNTA 4 (3 puntos)
-- Encuentra usuarios que han hecho más de 5 transacciones
-- Muestra: user_id, nombre del usuario, total_transactions, total_spent
-- Ordena por total_spent descendente

-- TU CÓDIGO AQUÍ:




-- PREGUNTA BONUS (2 puntos)
-- Identifica el método de pago más popular por país
-- Muestra: country, payment_method, usage_count

-- TU CÓDIGO AQUÍ:




-- ===============================================
-- RESULTADOS ESPERADOS
-- ===============================================
--
-- Pregunta 1: Debería retornar transacciones de Spain ordenadas por fecha
-- Pregunta 2: Top 10 productos con mayor selling_price
-- Pregunta 3: Revenue por categoría (Electronics suele ser el mayor)
-- Pregunta 4: Usuarios con >5 transacciones y su gasto total
-- Bonus: Payment method más usado por país
--
-- ===============================================