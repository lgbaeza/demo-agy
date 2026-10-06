---
name: py-cli-dev
description: Define las reglas corporativas de desarrollo para construir scripts CLI en Python.
version: 1.0.0
---
# Retail Recommendation Tooling Spec

## Reglas de Arquitectura
1. **Entrada CLI**: Aceptar la ruta de un archivo JSON desde argumentos de CLI (`sys.argv[1]`).
2. **Salida**: Generar un archivo de salida en el mismo directorio con el sujifo `_out` sobre el nombre original del archivo.
3. **Llamada a Gemini**: Usar el SDK oficial `google-genai` con modelo `gemini-3.8-flash` y forzar respuesta en JSON (`response_mime_type="application/json"`).
4. **Esquema de Salida**: Formato JSON, con el esquema que el caso de uso amerite, pero siempre un timestamp con la fecha de generación.