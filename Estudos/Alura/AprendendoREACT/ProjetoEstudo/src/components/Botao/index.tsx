import './botao.estilos.css'
import type { ReactNode } from 'react';

interface BotaoProps {
    children: ReactNode;
}

function Botao({ children }: BotaoProps){
    return (
        <button className='Botao'>
            { children }
        </button>
    )
}

export default Botao;