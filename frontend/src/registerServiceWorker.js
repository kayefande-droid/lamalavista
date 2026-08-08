// Simple service worker registration for CRA
export default function registerServiceWorker(){
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/service-worker.js').then(reg => {
        console.log('SW registered', reg);
      }).catch(err => console.warn('SW registration failed', err));
    });
  }
}
