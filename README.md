This is a simple web application built using Streamlit and PyTube. It allows users to download YouTube videos by entering a video URL and clicking a button. The downloaded video is saved in the project directory.

> ⚠️ This project is for educational purposes only. Downloading YouTube content without permission may violate YouTube's terms of service.

## Features

- Clean and interactive UI using Streamlit
- Download videos in the highest available resolution
- User feedback with success and error messages

## Getting Started

### Prerequisites

Ensure you have Python 3.7+ installed. Install the required packages:

```bash
pip install streamlit pytube
````

### Running the App

```bash
streamlit run app.py
```

Then open the local URL provided in your terminal to use the app in your browser.

## File Structure

```
main.py          # Main application file
README.md       # Project documentation
```

## How It Works

* Enter a valid YouTube video URL in the input box
* Click the "Download Video" button
* The video will be downloaded in the current directory
* The app shows a success or error message based on the outcome

## Disclaimer

This tool is meant for educational purposes. Please respect content creators and avoid using this app in ways that violate YouTube’s terms of service.

