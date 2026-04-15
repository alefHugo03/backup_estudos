import './label.estilos.css'
import type { ReactNode } from 'react';

interface LabelProps {
  children: ReactNode;
  htmlFor: string;
}

function Label({ children, htmlFor }: LabelProps) {
  return (
    <label htmlFor={htmlFor} className='Label'>
      {children}
    </label>
  )
}

export default Label;