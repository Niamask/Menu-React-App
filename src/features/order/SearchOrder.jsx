import { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function SearchOrder() {
  const [query, setQuery] = useState('');
  const navigate = useNavigate();

  function handelSubmit(e) {
    e.preventDefault();
    if (!query) return;
    navigate(`/order/${query}`);
    setQuery('');
  }

  return (
    <form onSubmit={handelSubmit}>
      <input
        placeholder="Search order #"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-28 rounded-full bg-orange-50 px-4 py-2 text-sm text-stone-800 transition-all duration-300 placeholder:text-stone-400 focus:outline-none focus:ring focus:ring-orange-200 focus:ring-opacity-50 sm:w-64 sm:focus:w-72 "
      />
    </form>
  );
}

export default SearchOrder;
