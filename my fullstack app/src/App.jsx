import { useState } from 'react'
import heroImg from './assets/hero.png'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import MyTable from './MyTable'; 
import MyForm from './MyForm';   
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <section id="center">
        <div className="hero">
          <img src={heroImg} className="base" width="170" height="179" alt="" />
          <img src={reactLogo} className="logo react" alt="React logo" />
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </div>
        <div>
          <h1>Hello React - Aruzhan</h1>
        </div>
      </section>

      {/* Счетчик */}
      <div className="card" style={{ margin: '20px 0', padding: '15px', border: '1px solid #ccc' }}>
        <h3>Counter Component</h3>
        <p>Counter = {count}</p>
        <button 
          type="button" 
          onClick={() => setCount(prevCount => prevCount + 1)}
        >
          Increment
        </button>
      </div>

      
      <MyTable />
      <MyForm />
    </div>
  );
}

export default App;