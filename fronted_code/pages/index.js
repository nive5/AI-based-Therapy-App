import Link from "next/link";

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
