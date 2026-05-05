import "./campo-formulario.estilos.css"
import type { ReactNode } from 'react';

interface CampoDeFormularioProps {
  children: ReactNode;
}


function CampoDeFormulario({ children }: CampoDeFormularioProps) {
  return (
    <fieldset className="campo-form">
      { children }
    </fieldset>
  )
}

export default CampoDeFormulario;