# Code Optimizer

The Code Optimizer is a web application that allows you to input a snippet of code and a desired time complexity (Big O notation). It will then attempt to optimize the code for you.

## File Structure

- **app.py** : Contains the Flask server code and the logic for the code optimization.
- **templates/index.html** : The main front-end for the code optimizer. Contains a form for user input and a display area for the optimized code.
- **static/styles.css** : Stylesheet for the frontend.

## Setup & Usage

1. Ensure you have Flask installed in your environment. If not, install it using:
   ```bash
   pip install Flask
   ```
2. Also, make sure you have the `openai` Python package installed:
   ```bash
   pip install openai
   ```
3. Set up an OpenAI API key and insert it in the `app.py` file where it says `openai.api_key = ''`.
4. Run the app using:
   ```bash
   python app.py
   ```
5. Open a web browser and navigate to `http://127.0.0.1:5000/`.
6. Input your code in the form provided and select the desired Big O notation from the dropdown.
7. Click "Optimize" and wait for the optimized code to be displayed.

## Functionality

- The front-end form accepts user code and desired Big O notation as input.
- The Flask backend communicates with the OpenAI GPT-4 API to attempt to optimize the code based on the desired time complexity.
- The response from the OpenAI API is then displayed in the frontend for the user to see.

## UI Features

- Uses Bootstrap 4 for layout and styling.
- Includes a loading spinner for user feedback during processing.
- Syntax highlighting for the optimized code using the Highlight.js library.

## Styles

- Global styles have been defined for body, headers, and the container.
- Form elements have specific styles for focus, hover, and other states.
- A transition effect has been applied to the primary button for better user feedback.

## Important

Always be cautious about security when deploying such applications. Avoid exposing API keys in public repositories or unsecured environments. 

Consider using environment variables or a configuration management tool to securely manage your API key.

## Credits

This application integrates the OpenAI GPT-4 API for code optimization.