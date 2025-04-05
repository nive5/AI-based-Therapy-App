import { useState } from "react";
import { useRouter } from "next/router";
import { loginUser } from "../utils/api";

export default function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleLogin = async () => {
    const response = await loginUser(email, password);
    if (response.success) {
      router.push("/dashboard");
    } else {
      setError(response.message);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h2 className="text-2xl font-bold">Login</h2>
      {error && <p className="text-red-500">{error}</p>}
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="mt-2 p-2 border rounded" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="mt-2 p-2 border rounded" />
      <button onClick={handleLogin} className="mt-4 px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700">Login</button>
    </div>
  );
}
