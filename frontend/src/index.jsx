import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './index.css';
import registerServiceWorker from './registerServiceWorker';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);

// Register SW for PWA offline features
registerServiceWorker();
