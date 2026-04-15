import "./titulo-formulario.estilos.css"
import type { ReactNode } from 'react';

// precisa declarar o que vai ter nesse objeto para poder usa-lo
interface TituloFormularioProps {
  children: ReactNode;
}

// props é um objeto
function TituloFormulario({ children }: TituloFormularioProps) {
  return (
    <h2 className="titulo-form ">
      { children }
    </h2>
  )
}

export default TituloFormulario;