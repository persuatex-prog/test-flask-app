"""
Simple Flask Hello API
A lightweight, stateless API that returns a greeting message.

This is the main application entry point.
"""

import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
# This allows configuration without hardcoding values
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure Flask secret key from environment variable
# Falls back to a default value if not set (not recommended for production)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')


@app.route('/hello', methods=['GET'])
def hello():
    """
    Hello endpoint that returns a greeting message.
    
    Returns:
        JSON response with message and HTTP 200 status code
    """
    try:
        response_data = {
            "message": "Hello, World!",
            "status": "success"
        }
        return jsonify(response_data), 200
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({
            "message": "An error occurred",
            "error": str(e),
            "status": "error"
        }), 500


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint for monitoring and load balancers.
    
    Returns:
        JSON response indicating service health and HTTP 200 status code
    """
    try:
        return jsonify({
            "status": "healthy",
            "service": "hello-api"
        }), 200
    except Exception as e:
        return jsonify({
            "status": "unhealthy",
            "error": str(e)
        }), 503


@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for undefined routes.
    
    Returns:
        JSON error response with HTTP 404 status code
    """
    return jsonify({
        "message": "Endpoint not found",
        "status": "error"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 internal server errors.
    
    Returns:
        JSON error response with HTTP 500 status code
    """
    return jsonify({
        "message": "Internal server error",
        "status": "error"
    }), 500


if __name__ == '__main__':
    # Get port from environment variable, default to 5000
    port = int(os.getenv('PORT', 5000))
    
    # Determine debug mode based on FLASK_ENV
    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    
    # Print startup information
    print(f"Starting Hello API on port {port}")
    print(f"Debug mode: {debug_mode}")
    print(f"Environment: {os.getenv('FLASK_ENV', 'development')}")
    
    # Run the Flask development server
    # host='0.0.0.0' allows external connections (useful for Docker/containers)
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
