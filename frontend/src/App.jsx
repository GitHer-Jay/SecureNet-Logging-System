import { useEffect, useState } from "react";

function App() {
  const [logs, setLogs] = useState([]);
  const [status, setStatus] = useState("");

  // Fetch logs from backend
  const fetchLogs = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/logs");
      const data = await res.json();
      setLogs(data);
    } catch (err) {
      console.error("Error fetching logs:", err);
    }
  };

  // Run integrity check
  const runCheck = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/verify");
      const data = await res.json();
      setStatus(data.result);
    } catch (err) {
      console.error("Error verifying:", err);
    }
  };

  // Load logs on start
  useEffect(() => {
    fetchLogs();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>SecureNet System</h1>

      <h2>Logs</h2>
      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Event</th>
            <th>User</th>
            <th>IP</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log) => (
            <tr key={log[0]}>
              <td>{log[0]}</td>
              <td>{log[1]}</td>
              <td>{log[2]}</td>
              <td>{log[3]}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Integrity Status</h2>
      <button onClick={runCheck}>Run Check</button>
      <p>{status}</p>
    </div>
  );
}

export default App;