# AGENTS.md — Retail AI Workspace Manifest

## 1. Contexto del Proyecto
Este repositorio contiene aplicaciones para el sector Retail.

## 2. Inventario de Agentes Configurados
Los siguientes agentes están registrados para operar en este repositorio:

| ID Agente | Archivo de Configuración | Rol Principal |
| :--- | :--- | :--- |
| `RetailDevAssistant` | `agents/RetailDevAssistant.yaml` | Supervisor técnico y Tech Lead que audita el cumplimiento de estándares. |

## 3. Catálogo de Skills & Plugins

### Skills Disponibles (`skills/`)
- **`retail-recommendation-spec`**: Reglas obligatorias de arquitectura, manejo de JSONs, SDKs y modelos.

### Plugins y Herramientas (`plugins/`)
- **`retail-dev-tools`**:
  - Comando: `validate-cart-schema`
  - Ejecutable: `python plugins/retail-dev-tools/scripts/validate_cart.py <file>`
  - Uso: Valida la estructura de entrada de los carritos de compra.

## 4. Guía de Operación para Agentes
Cualquier Agente de IA que genere o modifique código en este repositorio DEBE seguir estas reglas:
- Escribir el codigo en el folder src/ seguido de un folder del caso de uso en desarrollo
- Interactuar unicamente con un caso de uso a la vez, siguiendo las instrucciones del spec /specs que esta siendo procesado
- Probar con base en la data del folder data con al menos 3 casos, si no hay suficiente data para cumplir con la cantidad de pruebas especificada, generar casos de prueba sintéticos, creando archivos en el folder data anteponiendo synt_ al nombre