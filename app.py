from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/sumar", methods=["GET"])
def sumar():
    try:
        # Obtener los parámetros 'a' y 'b' de la URL
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        resultado = a + b
        return jsonify({"resultado": resultado})
    except ValueError:
        return jsonify({"error": "Por favor, ingrese números válidos."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
