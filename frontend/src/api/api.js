// minimal API helper
const API_BASE = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export async function postJSON(path, body){
  const res = await fetch(`${API_BASE}${path}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(body)
  });
  return res.json();
}

export default { postJSON };
