import React, {useEffect, useState} from 'react';

export default function AdminTools(){
  const [msg, setMsg] = useState('');
  useEffect(()=>{
    // stub: load admin settings
  },[]);
  return (
    <div>
      <h2>Admin Tools</h2>
      <p>Payment config, branding, room editor, invoices.</p>
      <div>{msg}</div>
    </div>
  );
}
