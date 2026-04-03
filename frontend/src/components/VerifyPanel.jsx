import { useState } from "react";
import { verifyLogs } from "../services/api";

export default function VerifyPanel() {
  const [status, setStatus] = useState("");

  const handleVerify = async () => {
    const res = await verifyLogs();
    setStatus(res.data.result);
  };

  return (
    <div className="bg-gray-900 p-4 rounded-xl">
      <h2 className="text-xl mb-3">Integrity Status</h2>

      <button
        onClick={handleVerify}
        className="bg-blue-500 px-4 py-2 rounded"
      >
        Run Check
      </button>

      <p className="mt-3">{status}</p>
    </div>
  );
}