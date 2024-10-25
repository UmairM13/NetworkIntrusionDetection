// src/components/Home.tsx
import React from "react";
import "../css/Home.css"; // Make sure to add some custom CSS for styling

const Home: React.FC = () => {
  const headers = [
    "dur",
    "proto",
    "service",
    "state",
    "spkts",
    "dpkts",
    "sbytes",
    "dbytes",
    "rate",
    "sttl",
    "dttl",
    "sload",
    "dload",
    "sloss",
    "dloss",
    "sinpkt",
    "dinpkt",
    "sjit",
    "djit",
    "swin",
    "stcpb",
    "dtcpb",
    "dwin",
    "tcprtt",
    "synack",
    "ackdat",
    "smean",
    "dmean",
    "trans_depth",
    "response_body_len",
    "ct_srv_src",
    "ct_state_ttl",
    "ct_dst_ltm",
    "ct_src_dport_ltm",
    "ct_dst_sport_ltm",
    "ct_dst_src_ltm",
    "is_ftp_login",
    "ct_ftp_cmd",
    "ct_flw_http_mthd",
    "ct_src_ltm",
    "ct_srv_dst",
    "is_sm_ips_ports",
  ];

  return (
    <div className="home-container">
      <h1>Welcome to the Network Intrusion Detection System</h1>
      <p>
        This system uses a machine learning model to analyze network traffic
        data and predict whether the behavior represents normal activity or a
        potential network intrusion.
      </p>
      <p>
        To make predictions, the system expects input data in CSV format. Below
        are the required headers that must be present in the CSV file for
        accurate predictions:
      </p>
      <div className="headers-grid">
        {headers.map((header, index) => (
          <div key={index} className="header-item">
            {header}
          </div>
        ))}
      </div>
      <p>
        Each row of data in the CSV file should contain values corresponding to
        these headers. The model will then analyze the data and provide a
        prediction indicating whether the network behavior is normal or
        suspicious.
      </p>
      <p>
        The system should work with extra headers in the CSV file, as long as
        the required headers are present.
      </p>
    </div>
  );
};

export default Home;
