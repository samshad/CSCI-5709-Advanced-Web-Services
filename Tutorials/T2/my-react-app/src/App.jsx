import React, {useState} from 'react';
import ReactDOM from 'react-dom';

function App() {
    const [count, setCount] = useState(0);

    const handleIncrement = () => {
        setCount(count + 1);
    };

    return (
        <div>
            <h1>Name: Md Samshad Rahman</h1>
            <h2>Tutorial 2 - Working Demo!</h2>
            <p>Counter: {count}</p>
            <button onClick={handleIncrement}>Increment</button>
        </div>
    );
}

export default App;
