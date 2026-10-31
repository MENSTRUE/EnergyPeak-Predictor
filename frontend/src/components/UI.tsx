import type {ReactNode} from 'react';
export function Panel({title,subtitle,children,aside}:{title:string;subtitle?:string;children:ReactNode;aside?:ReactNode}){return <section className="panel"><div className="panel-heading"><div><h2>{title}</h2>{subtitle&&<p>{subtitle}</p>}</div>{aside}</div>{children}</section>}
export function MetricCard({name,value,note}:{name:string;value:string;note?:string}){return <div className="metric-card"><div className="eyebrow">{name}</div><strong>{value}</strong>{note&&<small>{note}</small>}</div>}
export const fmt=(n:number|undefined,d=2)=>typeof n==='number'&&Number.isFinite(n)?new Intl.NumberFormat('en-US',{maximumFractionDigits:d}).format(n):'—';
export const pct=(n:number|undefined)=>typeof n==='number'&&Number.isFinite(n)?(n*100).toFixed(1)+'%':'—';
export const pretty=(s:string)=>s==='steel'?'Steel industry':s==='appliances'?'Residential appliances':s.replace('electricity_','Electricity · ');
export function Notice({children}:{children:ReactNode}){return <div className="notice">{children}</div>}
export function ErrorBox({message}:{message:string}){return <div className="error-box" role="alert">{message}</div>}
