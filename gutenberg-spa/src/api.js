const API_BASE_URL = "https://gutenberg-analyzer.onrender.com";

export async function fetchAnalysis(bookId) {
  const res = await fetch(`${API_BASE}/book/${bookId}`);
  if (!res.ok) throw new Error('Error fetching book or analysis');
  return res.json();
} 