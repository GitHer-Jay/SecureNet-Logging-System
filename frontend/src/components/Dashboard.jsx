import LogTable from "./LogTable";
import VerifyPanel from "./VerifyPanel";

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-black text-white p-6">
      <h1 className="text-3xl mb-6">SecureNet System</h1>

      <div className="grid grid-cols-2 gap-6">
        <LogTable />
        <VerifyPanel />
      </div>
    </div>
  );
}