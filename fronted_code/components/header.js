import Link from "next/link";

export default function Header() {
  return (
    <header className="bg-blue-600 text-white py-4 shadow-md">
      <div className="container mx-auto flex justify-between items-center px-6">
        {/* Logo */}
        <Link href="/">
          <img src="/logo.png" alt="AI Therapy Logo" className="h-10 cursor-pointer" />
        </Link>

        {/* Navigation */}
        <nav className="flex gap-6">
          <Link href="/" className="hover:underline">Home</Link>
          <Link href="/about" className="hover:underline">About</Link>
          <Link href="/dashboard" className="hover:underline">Dashboard</Link>
        </nav>

        {/* Auth Buttons */}
        <div className="flex gap-4">
          <Link href="/login">
            <button className="bg-white text-blue-600 px-4 py-2 rounded-md hover:bg-gray-200">Login</button>
          </Link>
          <Link href="/register">
            <button className="bg-green-500 text-white px-4 py-2 rounded-md hover:bg-green-700">Register</button>
          </Link>
        </div>
      </div>
    </header>
  );
}
