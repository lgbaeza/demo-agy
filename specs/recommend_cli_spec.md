# TASK SPEC: CLI Recomendador de Productos Retail (`specs/recommend_cli_spec.md`)

## 1. Meta información
- **ID de la Tarea**: `recommend_cli_spec`
- **Main file**: `src/recommend_cli_spec/recommend.py`

## 2. Objetivo
Desarrollar una aplicación de línea de comandos en Python que lea un carrito de compras desde un JSON local a partir de un parametro, invoque a Gemini para generar una recomendación de un producto adicional de venta cruzada y guarde el resultado en un archivo JSON procesado.

## 3. Contrato de Entrada y Salida (I/O)
- **Estructura Input JSON**:
    Archivos de ejemplo en folder data
- **Estructura Output JSON**
    misma estructura original. mas una propiedad anidada llamada "recommendation":
    {
        "recommended_product": "",
        "category": "",
        "reasoning": "",
        "affinity_score": 0.XX
    }