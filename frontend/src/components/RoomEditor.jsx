import React, {useEffect, useState} from 'react';

export default function RoomEditor(){
  const [rooms, setRooms] = useState([]);
  useEffect(()=>{
    // load rooms from API (stub)
  },[]);
  return (
    <div>
      <h3>Rooms</h3>
      <ul>{rooms.map(r=> <li key={r.id}>{r.name} - {r.price_xaf} XAF</li>)}</ul>
    </div>
  );
}
