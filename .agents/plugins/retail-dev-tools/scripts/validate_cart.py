import sys
import json

def validate_cart(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        # Validar claves requeridas por la especificación
        if "cart_id" not in data or "items" not in data:
            print("❌ Error: El JSON debe contener las llaves 'cart_id' e 'items'.")
            sys.exit(1)
            
        if not isinstance(data["items"], list):
            print("❌ Error: 'items' debe ser una lista de productos.")
            sys.exit(1)

        print("✅ Esquema válido: El carrito cumple con la estructura requerida.")
    except Exception as e:
        print(f"❌ Error al abrir o procesar el archivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python validate_cart.py <ruta_archivo_json>")
        sys.exit(1)
        
    validate_cart(sys.argv[1])