const API='/api'
export async function request<T=any>(path:string, options:RequestInit={}):Promise<T>{
  const response=await fetch(API+path,options)
  if(!response.ok){let msg=`Request failed (${response.status})`;try{const d=await response.json();msg=d.detail||msg}catch{};throw new Error(msg)}
  return response.json()
}
export const getTickets=(params='')=>request<any[]>(`/tickets${params}`)
export const getStats=()=>request<any>('/dashboard/stats')
export const getDocuments=()=>request<any[]>('/documents')
export const createTicket=(data:any)=>request('/tickets',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
export const updateTicket=(id:string,data:any)=>request(`/tickets/${id}`,{method:'PATCH',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
export const analyzeTicket=(id:string)=>request(`/tickets/${id}/analyze`,{method:'POST'})
export const draftReply=(id:string)=>request(`/tickets/${id}/draft`,{method:'POST'})
export const uploadDocument=(file:File)=>{const fd=new FormData();fd.append('file',file);return request('/documents/upload',{method:'POST',body:fd})}
export const deleteDocument=(id:string)=>request(`/documents/${id}`,{method:'DELETE'})
export const chat=(question:string)=>request('/assistant/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question})})

export const getReplies=(id:string)=>request<any[]>(`/tickets/${id}/replies`)
export const sendReply=(id:string,body:string)=>request<any>(`/tickets/${id}/replies`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({body})})

export const runSupportWorkflow=(id:string)=>request<any>(`/tickets/${id}/workflow`,{method:'POST'})

export const resumeSupportWorkflow=(ticketId:string,workflowId:string,action:'approve'|'reject',draft_reply='',feedback='')=>request<any>(`/tickets/${ticketId}/workflow/${workflowId}/approval`,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action,draft_reply,feedback})})
export const getSupportWorkflowState=(ticketId:string,workflowId:string)=>request<any>(`/tickets/${ticketId}/workflow/${workflowId}`)
