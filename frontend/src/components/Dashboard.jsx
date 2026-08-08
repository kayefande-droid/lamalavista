import React from 'react';
import Chat from './Chat';
import MonitorConsent from './MonitorConsent';

export default function Dashboard(){
  const wsUrl = process.env.REACT_APP_WS_URL || 'ws://localhost:8000';
  const userEmail = 'guest@example.com';
  return (
    <div>
      <h3>Dashboard</h3>
      <p>Welcome to Lamalavista PWA demo.</p>
      <Chat wsUrl={wsUrl} channel="public" userEmail={userEmail} />
      <MonitorConsent wsUrl={wsUrl} userEmail={userEmail} />
    </div>
  );
}
