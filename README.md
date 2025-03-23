# Weather Web App

This project is a web application that provides current weather information for any city using the OpenWeatherMap API. It is built with Flask and integrates weather functionality from a Python script.


## Setup Instructions

1. **Clone the repository**:

   git clone <repository-url>
   cd weather-web-app

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   
   pip install -r requirements.txt

5. **Set up environment variables**:
   Create a `.env` file in the root directory and add your OpenWeatherMap API key:

   API_KEY=your_api_key_here

## Usage

1. **Run the application**:
   python src/app.py

3. **Get weather information**:
   - Enter the name of the city you want to check the weather for.
   - Select the temperature unit (Celsius or Fahrenheit).
   - Submit the form to view the weather information.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
