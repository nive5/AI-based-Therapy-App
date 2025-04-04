import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/router";

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-blue-600">AI Therapy Assistant</h1>
      <p className="text-lg text-gray-700 mt-2">Track your mental health and get AI-powered assistance.</p>
      
      <div className="mt-6 flex gap-4">
        <Link href="/login">
          <button className="px-6 py-2 bg-blue-500 text-white rounded-lg shadow-lg hover:bg-blue-700">
            Login
          </button>
        </Link>
        <Link href="/register">
          <button className="px-6 py-2 bg-green-500 text-white rounded-lg shadow-lg hover:bg-green-700">
            Register
          </button>
        </Link>
      </div>
    </div>
  );
}

// Login Page
export function Login() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    // Add API request here
    router.push("/dashboard");
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h2 className="text-2xl font-bold">Login</h2>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="mt-2 p-2 border rounded" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="mt-2 p-2 border rounded" />
      <button onClick={handleLogin} className="mt-4 px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-700">Login</button>
    </div>
  );
}

// Register Page
export function Register() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async () => {
    // Add API request here
    router.push("/dashboard");
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h2 className="text-2xl font-bold">Register</h2>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} className="mt-2 p-2 border rounded" />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} className="mt-2 p-2 border rounded" />
      <button onClick={handleRegister} className="mt-4 px-6 py-2 bg-green-500 text-white rounded-lg hover:bg-green-700">Register</button>
    </div>
  );
}

// Dashboard Page
export function Dashboard() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h2 className="text-3xl font-bold">Dashboard</h2>
      <p className="text-lg">Welcome to your mental health tracker!</p>
    </div>
  );
}
