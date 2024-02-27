import { useState } from 'react';

import './styles.css';

// This is a warm up question to help you
// get familiar with the editor.
// Most of the code has been filled in for you.
export default function App() {
  const [count, setCount] = useState(0);
  const handleOnclick = () => {
    setCount(count => count+1)
  }

  return (
    <div>
      <button
        onClick={handleOnclick}>
        Clicks: {count}
      </button>
    </div>
  );
}