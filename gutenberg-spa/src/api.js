const API_BASE = 'http://127.0.0.1:8000';

export async function fetchAnalysis(bookId) {
  const res = await fetch(`${API_BASE}/book/${bookId}`);
  if (!res.ok) throw new Error('Error fetching book or analysis');
  return res.json();
} 