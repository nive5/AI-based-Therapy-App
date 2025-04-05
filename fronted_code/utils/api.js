const BASE_URL = "http://localhost:8000";

export async function loginUser(email, password) {
  try {
    const response = await fetch(`${BASE_URL}/login/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) throw new Error("Invalid login credentials");
    return { success: true };
  } catch (error) {
    return { success: false, message: error.message };
  }
}

export async function registerUser(email, password) {
  try {
    const response = await fetch(`${BASE_URL}/register/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    if (!response.ok) throw new Error("Registration failed");
    return { success: true };
  } catch (error) {
    return { success: false, message: error.message };
  }
}
