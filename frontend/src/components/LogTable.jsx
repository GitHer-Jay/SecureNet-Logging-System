import { useEffect, useState } from "react";
import { getLogs } from "../services/api";

export default function LogTable() {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    fetchLogs();
  }, []);

  const fetchLogs = async () => {
    const res = await getLogs();
    setLogs(res.data);
  };

  return (
    <div className="bg-gray-900 p-4 rounded-xl">
      <h2 className="text-xl mb-3">Logs</h2>

      <table className="w-full text-sm">
        <thead>
          <tr className="text-gray-400">
            <th>ID</th>
            <th>Event</th>
            <th>User</th>
            <th>IP</th>
          </tr>
        </thead>
        <tbody>
          {logs.map((log) => (
            <tr key={log.id} className="border-t border-gray-700">
              <td>{log.id}</td>
              <td>{log.event}</td>
              <td>{log.user}</td>
              <td>{log.ip}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}