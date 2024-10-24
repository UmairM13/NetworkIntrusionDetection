import React, { useState } from "react";
import { predict } from "../api/api"; // Import the predict function
import "../css/NIDS.css";

interface NIDSProps {
  token: string;
}

const NIDS: React.FC<NIDSProps> = () => {
  const [data, setData] = useState<string>(""); // Data input by the user
  const [predictions, setPredictions] = useState<string[]>([]); // Predictions returned from the API
  const [error, setError] = useState<string>(""); // Error message handling

  // Define the CSV headers and sample data rows
  const headers = `dur,proto,service,state,spkts,dpkts,sbytes,dbytes,rate,sttl,dttl,sload,dload,sloss,dloss,sinpkt,dinpkt,sjit,djit,swin,stcpb,dtcpb,dwin,tcprtt,synack,ackdat,smean,dmean,trans_depth,response_body_len,ct_srv_src,ct_state_ttl,ct_dst_ltm,ct_src_dport_ltm,ct_dst_sport_ltm,ct_dst_src_ltm,is_ftp_login,ct_ftp_cmd,ct_flw_http_mthd,ct_src_ltm,ct_srv_dst,is_sm_ips_ports`;

  const sampleDataArray = [
    `0.0,TCP,HTTP,RECV,1,1,1000,2000,0.1,64,64,0,0,0,0,0,0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,0.0,1,1,1,1,1,0,0,0,0,0,0`,
    `1.0,TCP,FTP,RECV,1,1,2000,4000,0.2,64,64,0,0,0,0,0,0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,0.0,1,1,1,1,1,0,0,0,0,0,0`,
    `0.5,TCP,HTTP,RECV,10,10,5000,10000,0.5,60,60,5,10,0,0,0.5,0.5,0,0,1000,10000,10000,1000,0,0,0,0,0,0,0.0,0.0,1,1000,1,1,1,1,1,0,0,0,0,0,0`,
    `2.0,TCP,SSH,RECV,1,1,1000,1000,0.3,60,60,0,0,0,0,0,0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,0.0,1,1,1,1,1,0,0,0,0,0,0`,
    `3.5,TCP,DDoS,RECV,100,100,50000,100000,10.0,30,30,2000,3000,0,0,5.0,5.0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0`,
    `1.5,TCP,HTTP,RECV,5,5,1500,3000,0.2,64,64,1,1,0,0,0.5,0.5,0,0,300,2000,2000,300,0,0,0,0,0,1,10,1,1,1,1,1,0,0,0,0,0,0`,
    `4.0,TCP,UDP,RECV,3,3,7000,14000,0.4,50,50,0,0,0,0,0,0,0.0,0.0,0,0,0,0,0,0,0,0,0.0,0.0,1,1,1,1,1,0,0,0,0,0,0`,
  ];

  // Function to generate random sample data by combining the headers with random data row
  const handleGenerateSampleData = () => {
    const randomSample =
      sampleDataArray[Math.floor(Math.random() * sampleDataArray.length)];
    setData(`${headers}\n${randomSample}`); // Add headers to the selected random sample
  };

  // Function to handle file uploads for custom CSV input
  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = async (event) => {
        const text = event.target?.result;
        if (typeof text === "string") {
          setData(text);
        }
      };
      reader.readAsText(file);
    }
  };

  // Function to submit the data and make predictions via the API
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError(""); // Clear previous errors
    setPredictions([]); // Clear previous predictions

    try {
      const result = await predict(data); // Call the predict function without token
      console.log("API Response:", result); // Debugging line

      if (result && Array.isArray(result.predictions)) {
        setPredictions(result.predictions);
        console.log("Updated Predictions:", result.predictions); // Debugging line
      } else {
        setError("Unexpected response structure from API.");
        console.error("Unexpected response:", result); // Log unexpected responses
      }
    } catch (error) {
      if (error instanceof Error) {
        setError(`API Error: ${error.message}`);
      } else {
        setError("An unexpected error occurred.");
      }
    }
  };

  return (
    <div className="nids-container">
      <h1>Network Intrusion Detection System</h1>
      <form onSubmit={handleSubmit} className="nids-form">
        <textarea
          placeholder="Paste your CSV data here..."
          value={data}
          onChange={(e) => setData(e.target.value)}
          rows={10}
          className="nids-textarea"
        />
        <div className="button-container">
          <button
            type="button"
            onClick={handleGenerateSampleData}
            className="nids-button"
          >
            Generate Random Sample Data
          </button>
          <input
            type="file"
            accept=".csv"
            onChange={handleFileUpload}
            className="nids-button"
          />
          <button type="submit" className="nids-button">
            Predict
          </button>
        </div>
      </form>
      {error && <div className="error-message">{error}</div>}
      {predictions.length > 0 && (
        <div className="predictions-container">
          <h2>Predictions:</h2>
          <ul>
            {predictions.map((prediction, index) => (
              <li key={index}>{prediction}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default NIDS;
