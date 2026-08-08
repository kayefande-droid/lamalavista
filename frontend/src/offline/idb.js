// tiny IndexedDB helper (no external libs)
export function openDB(){
  return new Promise((resolve, reject) =>{
    const req = indexedDB.open('lamalavista-idb', 1);
    req.onupgradeneeded = (e)=>{
      const db = e.target.result;
      if (!db.objectStoreNames.contains('bookings')) db.createObjectStore('bookings', { keyPath: 'id', autoIncrement: true });
      if (!db.objectStoreNames.contains('syncQueue')) db.createObjectStore('syncQueue', { keyPath: 'id', autoIncrement: true });
    };
    req.onsuccess = ()=> resolve(req.result);
    req.onerror = ()=> reject(req.error);
  });
}
