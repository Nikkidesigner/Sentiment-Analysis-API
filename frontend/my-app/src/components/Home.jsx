import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./login.css";
const Home = () => {
  const [reviewText, setReviewText] = useState("");
  const [userId, setUserId] = useState(1); 
  const navigate = useNavigate();

  useEffect(() => {
   
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  const handleAnalyze = async () => {
    const token = localStorage.getItem("token");
    if (!token) {
      alert("Session expired! Please log in again.");
      navigate("/login");
      return;
    }

    try {
      const response = await fetch("https://sentiment-analysis-api-4sg4.onrender.com/analyze/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({ user_id: userId, review_text: reviewText }),
      });

      if (response.ok) {
        const result = await response.json();
        alert(
          `Sentiment: ${result.sentiment} \nConfidence: ${result.confidence.toFixed(
            2
          )}%`
        );
      } else {
        alert("Error analyzing sentiment. Please try again.");
      }
    } catch (err) {
      alert("An error occurred. Please try again.");
    }
  };

  return (
    <div className="container">
      <h2>Welcome to Sentiment Analysis</h2>
      <div className="input-group">
      <input
            type="text"
            name="reviewText"
            placeholder="Enter your review"
            value={reviewText}
            onChange={(e) => setReviewText(e.target.value)}
            required
          />
      </div>
       <div className="login-button">
      <button onClick={handleAnalyze} >Submit</button>
      </div>
    </div>
  );
};

export default Home;
