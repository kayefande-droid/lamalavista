import React from 'react';
import AuthSignup from './components/AuthSignup';
import AuthVerifyOTP from './components/AuthVerifyOTP';
import Dashboard from './components/Dashboard';

export default function App(){
  return (
    <div>
      <header style={{padding:20, background: 'linear-gradient(90deg,#ff7a18,#00b4db)'}}>
        <h1 style={{color:'#fff'}}>Lamalavista Hotel</h1>
      </header>
      <main style={{padding:20}}>
        <AuthSignup />
        <hr />
        <AuthVerifyOTP />
        <hr />
        <Dashboard />
      </main>
    </div>
  );
}
