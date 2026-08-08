import React, {useState} from 'react';
import api from '../api/api';

export default function AuthVerifyOTP(){
  const [email, setEmail] = useState('');
  const [code, setCode] = useState('');
  const [msg, setMsg] = useState('');

  async function verify(e){
    e.preventDefault();
    const res = await api.postJSON('/auth/verify', { email, code });
    setMsg(res.msg || JSON.stringify(res));
  }

  return (
    <div>
      <h2>Verify OTP</h2>
      <form onSubmit={verify}>
        <input placeholder="Gmail address" type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
        <input placeholder="6-digit code" value={code} onChange={e=>setCode(e.target.value)} required />
        <button type="submit">Verify</button>
      </form>
      <div>{msg}</div>
    </div>
  );
}
