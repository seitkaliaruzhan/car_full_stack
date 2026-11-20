function MyTable() {
    const data = [
        {id: 1, brand: 'Ford', model: 'Mustang'},
        {id: 2, brand: 'VW', model:'Beetle'},
        {id: 3, brand: 'Tesla', model:'Model S'}
    ];
    return(
        <div style={{ margin: '20px 0', padding: '15px', border: '1px solid #ccc' }}>
      <h3>Table Component</h3>
      <table style={{ margin: '0 auto', textAlign: 'left' }}>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td style={{ paddingRight: '15px' }}>{item.brand}</td>
              <td>{item.model}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default MyTable;
    