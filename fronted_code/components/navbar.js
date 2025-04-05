import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="p-4 bg-blue-600 text-white flex justify-between">
      <h1 className="text-lg font-bold">AI Therapy Assistant</h1>
      <div className="flex gap-4">
        <Link href="/">Home</Link>
        <Link href="/login">Login</Link>
        <Link href="/register">Register</Link>
      </div>
    </nav>
  );
}
