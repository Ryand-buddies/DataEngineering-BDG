# Guía de Contribución

¡Gracias por tu interés en mejorar este proyecto de evaluación de Data Engineering! Esta guía te ayudará a contribuir efectivamente.

## 🤝 Cómo Contribuir

### 1. Reportar Problemas
- Usa el template de issues de GitHub
- Incluye información del entorno (Python version, OS, etc.)
- Proporciona pasos para reproducir el problema
- Adjunta logs o screenshots si es relevante

### 2. Proponer Mejoras
- Abre un issue para discutir la mejora propuesta
- Explica el valor que aporta
- Considera el impacto en candidatos existentes

### 3. Agregar Ejercicios
#### Nuevos Ejercicios SQL
- Sigue el formato de ejercicios existentes
- Incluye comentarios claros y pistas
- Agrega resultados esperados
- Considera diferentes niveles de dificultad

#### Nuevos Ejercicios PySpark
- Usa las mismas estructuras de datos
- Incluye consideraciones de performance
- Documenta configuraciones específicas necesarias
- Test en diferentes versiones de Spark si es posible

#### Nuevos Ejercicios Python
- Mantén compatibilidad con pandas versión especificada
- Incluye docstrings detallados
- Agrega type hints cuando sea apropiado
- Considera memory usage y performance

### 4. Mejorar Datasets
- Los datasets deben ser sintéticos/anonymizados
- Mantén consistencia con esquemas existentes
- Documenta cualquier cambio en README.md de data/
- Considera el tamaño para tiempos de ejecución razonables

## 📝 Estándares de Código

### SQL
```sql
-- Usar comentarios descriptivos
SELECT 
    column_name,
    ANOTHER_COLUMN,
    -- Explicar lógica compleja
    CASE 
        WHEN condition THEN result
        ELSE other_result 
    END AS descriptive_alias
FROM 
    table_name t
    INNER JOIN other_table o ON t.id = o.foreign_id
WHERE 
    t.filter_column = 'value'
ORDER BY 
    column_name;
```

### Python
```python
def function_name(param: str) -> pd.DataFrame:
    """
    Descripción clara de la función.
    
    Args:
        param: Descripción del parámetro
        
    Returns:
        Descripción del retorno
    """
    # Lógica implementada aquí
    return result
```

### PySpark
```python
# Configuraciones explícitas
spark = SparkSession.builder \
    .appName("DescriptiveName") \
    .config("spark.setting", "value") \
    .getOrCreate()

# Transformaciones claras y bien documentadas
result_df = input_df \
    .filter(col("column") > threshold) \
    .groupBy("key_column") \
    .agg(sum("value").alias("total_value"))
```

## 🔄 Proceso de Desarrollo

1. **Fork** el repositorio
2. **Clone** tu fork localmente
3. **Crea** una rama para tu feature: `git checkout -b feature/nueva-caracteristica`
4. **Desarrolla** siguiendo los estándares establecidos
5. **Testa** tus cambios completamente
6. **Commit** con mensajes descriptivos
7. **Push** a tu fork: `git push origin feature/nueva-caracteristica`
8. **Abre** un Pull Request

### Mensajes de Commit
```
tipo(scope): descripción corta

Descripción más larga del cambio si es necesario.
Explica el 'por qué' no solo el 'qué'.

- Detalle importante 1
- Detalle importante 2
```

Tipos: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 🧪 Testing

### Antes de enviar PR:
- [ ] Ejecuta `python setup/test_setup.py`
- [ ] Verifica que todos los ejercicios cargan sin errores
- [ ] Test con diferentes versiones de Python (3.8, 3.9, 3.10+)
- [ ] Verifica que la documentación esté actualizada
- [ ] Test de instalación completa con `./setup/install.sh`

### Ejemplos de tests:
```python
# Test que archivos de datos existen
assert os.path.exists("data/sample_data.csv")

# Test que ejercicios cargan sin errores
exec(open("python/exercises/01_pandas_basico.py").read())

# Test que datasets tienen formato correcto  
df = pd.read_csv("data/sample_data.csv")
assert len(df) > 0
assert "transaction_id" in df.columns
```

## 📚 Documentación

### Al agregar ejercicios:
- Actualiza el README.md de la sección correspondiente
- Agrega el ejercicio a la lista de dificultades
- Documenta prerequisitos específicos
- Incluye tiempo estimado realista

### Al cambiar datasets:
- Actualiza `data/README.md`
- Documenta cambios en el schema
- Actualiza scripts de generación si es necesario
- Verifica que ejercicios existentes sigan funcionando

## 🏷️ Etiquetas de Issues

- `bug` - Algo no funciona correctamente
- `enhancement` - Nueva característica o mejora
- `documentation` - Mejoras en documentación
- `good first issue` - Bueno para nuevos contribuidores
- `help wanted` - Se necesita ayuda de la comunidad
- `sql` - Relacionado con ejercicios SQL
- `pyspark` - Relacionado con ejercicios PySpark  
- `python` - Relacionado con ejercicios Python
- `data` - Relacionado con datasets
- `setup` - Relacionado con instalación/configuración

## 💡 Ideas de Contribución

### Fácil (Good First Issue)
- Corregir typos en documentación
- Mejorar comentarios en ejercicios existentes
- Agregar más casos de test en validaciones
- Traducciones de documentación

### Intermedio  
- Nuevos ejercicios de dificultad básica/intermedia
- Mejoras en scripts de setup
- Notebooks de Jupyter con ejercicios interactivos
- Validaciones adicionales en ETL pipelines

### Avanzado
- Ejercicios de streaming en PySpark
- Integración con Docker/Kubernetes
- Ejercicios con Delta Lake/Iceberg
- Performance benchmarking automatizado
- CI/CD pipelines para testing

## 📞 Contacto y Soporte

- **Issues**: Para bugs y feature requests
- **Discussions**: Para preguntas generales y discusiones
- **Email**: Para temas sensibles (si aplica)

## 📄 Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la misma licencia que el proyecto (MIT).

---

¡Esperamos tus contribuciones! Cada mejora, por pequeña que sea, hace que este recurso sea mejor para la comunidad de Data Engineering. 🚀