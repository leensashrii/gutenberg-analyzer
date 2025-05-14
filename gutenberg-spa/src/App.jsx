import { useState } from 'react';
import { fetchAnalysis } from './api';
import './App.css';

function App() {
  const [bookId, setBookId] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFetch = async () => {
    if (!bookId.trim()) {
      setError('Please enter a book ID');
      return;
    }

    setLoading(true);
    setError('');
    setResult(null);

    try {
      const data = await fetchAnalysis(bookId);
      setResult(data.analysis);
    } catch (err) {
      setError('Error fetching book or analysis. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 py-6 flex flex-col justify-center sm:py-12">
      <div className="relative py-3 sm:max-w-xl sm:mx-auto">
        <div className="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
          <div className="max-w-md mx-auto">
            <div className="divide-y divide-gray-200">
              <div className="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
                <h1 className="text-3xl font-bold text-center mb-8">
                  <span className="burgundy-g">G</span>utenberg <span className="burgundy-g">B</span>ook <span className="burgundy-g">A</span>nalyzer
                </h1>
                
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={bookId}
                    onChange={(e) => setBookId(e.target.value)}
                    placeholder="Enter Gutenberg book ID"
                    className="flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                  <button
                    onClick={handleFetch}
                    disabled={loading}
                    className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50"
                  >
                    {loading ? 'Loading...' : 'Analyze'}
                  </button>
                </div>

                {error && (
                  <div className="text-red-500 mt-2">
                    {error}
                  </div>
                )}

                {result && (
                  <div className="mt-4">
                    <h2 className="text-xl font-semibold mb-2">Character Analysis</h2>
                    <div className="p-4 bg-gray-50 rounded-lg whitespace-pre-wrap">
                      {result}
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;