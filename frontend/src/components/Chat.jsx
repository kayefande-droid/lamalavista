import React, {useEffect, useState} from 'react';

export default function Chat({wsUrl, channel, userEmail}){
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState('');
  useEffect(()=>{
    const ws = new WebSocket(`${wsUrl}/ws/chat/${encodeURIComponent(channel)}?user=${encodeURIComponent(userEmail)}`);
    ws.onmessage = (ev)=>{
      try{ const data = JSON.parse(ev.data); setMessages(m=>[...m, data]); }catch(e){console.warn(e)}
    };
    ws.onopen = ()=> console.log('chat ws open');
    return ()=> ws.close();
  },[wsUrl,channel,userEmail]);

  function send(){
    const ws = new WebSocket(`${wsUrl}/ws/chat/${encodeURIComponent(channel)}?user=${encodeURIComponent(userEmail)}`);
    ws.onopen = ()=>{ ws.send(JSON.stringify({sender:userEmail, text})); ws.close(); setText(''); };
  }

  return (
    <div>
      <h4>Chat ({channel})</h4>
      <div style={{height:150,overflow:'auto',border:'1px solid #ccc',padding:10}}>
        {messages.map((m,i)=><div key={i}><b>{m.sender}</b>: {m.text}</div>)}
      </div>
      <input value={text} onChange={e=>setText(e.target.value)} placeholder="Message..." />
      <button onClick={send}>Send</button>
    </div>
  );
}
