# TASK SPEC: CLI Recomendador de Productos Retail (`specs/recommend_cli_spec.md`)

## 1. Meta información
- **ID de la Tarea**: `TASK-RETAIL-001`
- **Archivo a Generar**: `src/recommend_cli_spec/recommend.py`
- **Skill Corporativa Aplicable**: `skills/retail-recommendation-spec/SKILL.md`

## 2. Objetivo
Desarrollar una aplicación de línea de comandos en Python que lea un carrito de compras desde un JSON local a partir de un parametro, invoque a Gemini para generar una recomendación de venta cruzada y guarde el resultado en un archivo JSON procesado.

## 3. Contrato de Entrada y Salida (I/O)
- **Entrada (CLI)**: `python recommend.py <ruta_json>`
- **Estructura Input JSON**:
  ```json
  {
    "cart_id": "cart_101",
    "items": ["Leche entera 1L", "Cereal de avena 500g"]
  }