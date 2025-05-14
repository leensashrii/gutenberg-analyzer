export async function fetchAnalysis(bookId) {
  const res = await fetch(`https://gutenberg-analyzer.onrender.com/book/${bookId}`);
  if (!res.ok) {
    throw new Error('API error');
  }
  return res.json();
}