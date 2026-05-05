import "./campo-entrada.estilos.css"
import type { ComponentProps } from 'react';

interface CampoDeEntrada extends ComponentProps<'input'>{
}

function CampoDeEntrada (props: CampoDeEntrada) {

    return <input { ...props } className="campo-entrada-form" />
}

export default CampoDeEntrada;