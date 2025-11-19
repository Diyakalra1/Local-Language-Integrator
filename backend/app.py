import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# --- Application Setup ---
app = Flask(__name__)
# Enable CORS for all routes and origins. 
# This is crucial for allowing the React frontend (running on a different port) to access the backend.
CORS(app) 

# --- Routes ---

@app.route('/', methods=['GET'])
def home():
    """A simple health check endpoint."""
    return "Local Language Integrator Backend Running!", 200

@app.route('/api/process', methods=['POST'])
def process_text():
    """
    Receives text and language from the frontend and processes it.
    
    In the final version, this is where you would integrate your actual
    language processing libraries (e.g., translation, transliteration).
    """
    try:
        # Get JSON data sent from the React frontend
        data = request.get_json()
        
        # Check if required fields are present
        if not data or 'sourceText' not in data or 'language' not in data:
            return jsonify({'error': 'Missing sourceText or language field.'}), 400

        source_text = data['sourceText']
        target_language = data['language']

        # --- MOCK PROCESSING LOGIC ---
        # For now, we just echo a processed result back to the frontend.
        # This confirms the connection is successful!
        processed_result = (
            f"Successfully received and processed text. "
            f"Source: '{source_text[:50]}...' "
            f"Target Language: {target_language}. "
            f"Your language model output would go here."
        )

        # Return the processed result as JSON
        return jsonify({
            'success': True,
            'result': processed_result,
            'metadata': {
                'language_used': target_language
            }
        })

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal server error during processing.'}), 500

# --- Run the Application ---
if __name__ == '__main__':
    # Flask typically runs on port 5000 by default.
    app.run(debug=True)