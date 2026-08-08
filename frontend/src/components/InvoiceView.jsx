import React from 'react';

export default function InvoiceView({invoice}){
  if(!invoice) return <div>No invoice</div>;
  return (
    <div>
      <h3>Invoice #{invoice.id}</h3>
      <div>Amount: {invoice.total_xaf} XAF</div>
      <div>Method: {invoice.method}</div>
    </div>
  );
}
