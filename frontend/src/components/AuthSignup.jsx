import React, {useState} from 'react';
import api from '../api/api';

export default function AuthSignup(){
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [msg, setMsg] = useState('');

  async function submit(e){
    e.preventDefault();
    const res = await api.postJSON('/auth/signup', { email, name });
    setMsg(res.msg || JSON.stringify(res));
  }

  return (
    <div>
      <h2>Sign up (Gmail)</h2>
      <form onSubmit={submit}>
        <input placeholder="Full name" value={name} onChange={e=>setName(e.target.value)} required />
        <input placeholder="Gmail address" type="email" value={email} onChange={e=>setEmail(e.target.value)} required />
        <button type="submit">Send OTP</button>
      </form>
      <div>{msg}</div>
    </div>
  );
}
