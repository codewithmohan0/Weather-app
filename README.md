# Weather Web App

This project is a web application that provides current weather information for any city using the OpenWeatherMap API. It is built with Flask and integrates weather functionality from a Python script.

## Project Structure

```
weather-web-app
├── src
│   ├── weather.py          # Contains weather functionality and API integration
│   ├── app.py              # Main entry point for the web application
│   ├── templates           # HTML templates for rendering pages
│   │   ├── base.html       # Base HTML template
│   │   ├── index.html      # Landing page with input form
│   │   └── result.html     # Page displaying weather results
│   └── static              # Static files (CSS)
│       └── styles.css      # Styles for the web application
├── requirements.txt        # Project dependencies
├── .env                    # Environment variables (e.g., API key)
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd weather-web-app
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

1. **Run the application**:
   ```
   python src/app.py
   ```

2. **Access the web application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

3. **Get weather information**:
   - Enter the name of the city you want to check the weather for.
   - Select the temperature unit (Celsius or Fahrenheit).
   - Submit the form to view the weather information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.