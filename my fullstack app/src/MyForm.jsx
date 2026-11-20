import { useState } from 'react';

function MyForm() {
  const [user, setUser] = useState({
    firstName: '',
    lastName: '',
    email: ''
  });

  const handleChange = (event) => {
    setUser({ ...user, [event.target.name]: event.target.value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(`Hello ${user.firstName} ${user.lastName}`);
  };

  return (
    <div style={{ margin: '20px 0', padding: '15px', border: '1px solid #ccc' }}>
      <h3>Form Component</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label>First name: </label>
          <input 
            type="text" 
            name="firstName" 
            onChange={handleChange} 
            value={user.firstName} 
          />
        </div>
        <div style={{ marginTop: '10px' }}>
          <label>Last name: </label>
          <input 
            type="text" 
            name="lastName" 
            onChange={handleChange} 
            value={user.lastName} 
          />
        </div>
        <div style={{ marginTop: '10px' }}>
          <label>Email: </label>
          <input 
            type="email" 
            name="email" 
            onChange={handleChange} 
            value={user.email} 
          />
        </div>
        <div style={{ marginTop: '10px' }}>
          <input type="submit" value="Submit" />
        </div>
      </form>
    </div>
  );
}

export default MyForm;