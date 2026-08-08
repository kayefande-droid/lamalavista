/* Simple service worker for offline shell caching and sync stub */
const CACHE_NAME = 'lamalavista-v1';
const OFFLINE_URL = '/offline.html';

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(['/', '/index.html', '/offline.html']))
  );
  self.skipWaiting();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then(resp => resp || fetch(event.request).catch(() => caches.match(OFFLINE_URL)))
  );
});

self.addEventListener('sync', event => {
  if (event.tag === 'sync-queue') {
    event.waitUntil(processQueue());
  }
});

async function processQueue(){
  // placeholder: open IndexedDB and replay queued requests
  console.log('Processing background sync queue (stub)');
}
