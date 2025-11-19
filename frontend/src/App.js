import { useState } from "react";

function App() {
  const [input, setInput] = useState("");
  const [output, setOutput] = useState("");

  const sendText = async () => {
  const res = await fetch("http://127.0.0.1:5000/api/process", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ 
      sourceText: input,
      language: "english"   // or whichever language you want
    })
  });

  

    const data = await res.json();
    setOutput(data.result);
  };

  return (
    <div style={{ padding: 40 }}>
      <h2>Local Language Integrator</h2>

      <textarea
        rows="4"
        style={{ width: "300px" }}
        placeholder="Enter text to convert"
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />

      <br /><br />

      <button onClick={sendText}>Submit</button>

      <h3>Output:</h3>
      <p>{output}</p>
    </div>
  );
}

export default App;
