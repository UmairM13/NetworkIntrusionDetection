# Network Intrusion Detection System (NIDS)

This project is a **Network Intrusion Detection System (NIDS)** built with a machine learning model to analyze network traffic data and predict whether the behavior represents normal activity or a potential network intrusion. The system uses the **UNSW_NB15** dataset.

## Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [API](#api)
- [Frontend](#frontend)
- [Future Improvements](#future-improvements)

## Overview

The Network Intrusion Detection System (NIDS) works by analyzing network traffic data using a machine learning model. The data should be formatted in CSV, with each row representing a network session. The model processes this data and predicts whether the session behavior is classified as **normal** or potentially **malicious**.

## Technologies Used

- **Backend**: Python (Flask)
- **Frontend**: React (TypeScript)
- **Machine Learning**: Random Forest
- **Database**: SQLite
- **Other Libraries**:
  - Pandas (for data processing)
  - joblib (for model persistence)
  - Axios (for API requests in React)

## Project Structure

```
+-- backend/
|   +-- app/
|   +-- models/
|   +-- routes/
|   +-- db.py
|   +-- server.py
|   +-- ...
+-- frontend/
|   +-- public/
|   +-- src/
|   |   +-- components/
|   |   +-- App.tsx
|   |   +-- ...
|   +-- ...
+-- models/
|   +-- random_forest_model.joblib
|   +-- knn_model.joblib
|   +-- svm_model.joblib
|   +-- ...
+-- data/
|   +-- network_traffic.csv
+-- README.md
+-- ...
```

### Key Files and Directories

- **backend/**: Contains the Flask app that serves the API and handles model predictions.
- **frontend/**: React app that serves the user interface for submitting data and displaying results.
- **models/**: Pre-trained machine learning models saved in `.joblib` format.
- **data/**: Sample data for testing predictions.

## Setup

### Prerequisites

- Python 3.x
- Node.js (v14 or higher)
- pip (Python package manager)
- npm or yarn (JavaScript package manager)

### Backend Setup

1. Clone the repository and navigate to the `backend` directory.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   cd backend
   pip install -r requirements.txt
   python db.py     # Initialize the SQLite database
   python main.py   # Retrain the model
   python server.py # Start the server

   ```

   The server should now be running on ` http//localhost:5000`

### Frontend Setup

```bash

    cd frontend
    cd nids-project
    npm run dev

```

The server should be running on http//localhost:5173/

## Usage

1. **Accessing the Application:**

   - Open your web browser and go to `http://localhost:5173` to access the frontend application.
   - Log in with your credentials or use admin for the default username and password.

2. **Input Data for Predictions:**

   - Navigate to the prediction page.
   - You can either upload a CSV file containing your network traffic data or use the "Simulate" button to autofill sample data in the input area.
   - Ensure that your input data follows the required headers format specified on the home page.
   - Input data can contain extra headers as long as the required headers are present

3. **Viewing Predictions:**

   - After inputting your data, click the "Predict" button.
   - The application will process the data and display the predictions indicating whether the network behavior is normal or suspicious.

4. **Logging Out:**
   - Use the logout button in the navigation bar to end your session.

## Required Headers

The machine learning model expects the following headers in the input CSV file for accurate predictions:

```
dur, proto, service, state, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl, sload, dload, sloss, dloss, sinpkt, dinpkt, sjit, djit, swin, stcpb, dtcpb, dwin, tcprtt, synack, ackdat, smean, dmean, trans_depth, response_body_len, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, is_ftp_login, ct_ftp_cmd, ct_flw_http_mthd, ct_src_ltm, ct_srv_dst, is_sm_ips_ports
```

## Troubleshooting

- Ensure that the backend server is running before starting the frontend application.
- Verify that your input data matches the required headers format.
- Check the console for any errors if the application does not behave as expected.

## API

The backend provides a simple API to predict network intrusions.

### POST /api/nids/predict

- **Request**: Send CSV data in plain/text format.
- **Response**: Returns predictions for each row of network traffic data.

**Example:**

```bash
POST http://localhost:5000/api/nids/predict
{
  csv text with headers
}
```

**Response:**

```json
{
  "predictions": ["normal", "DoS", "exploit"]
}
```

## Frontend

The frontend is built using React and provides a clean user interface for inputting data, uploading CSV files, and displaying predictions. It is styled to ensure user-friendly interactions and error handling.

### Features

- **Prediction Interface**: Paste data, upload CSVs, or generate sample data for prediction.
- **Real-Time Feedback**: View predictions in real-time after submission.
- **Responsive Design**: The interface adapts to different screen sizes.

## Future Improvements

- **Authentication**: Currently, the system allows predictions without requiring user authentication. In the future, we may add secure login and session management.
- **Model Expansion**: Support for additional machine learning models and attack types.
- **Performance Enhancements**: Improve model prediction speed and optimize data handling.
- **Real Time**: Improve system to link with a network to predict real traffic in real time

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
