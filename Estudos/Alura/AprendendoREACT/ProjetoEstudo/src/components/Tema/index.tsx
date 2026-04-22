import './tema.estilos.css'

interface ITema {
    id: number;
    nome: string;
}

interface TemaProps {
    tema: ITema;
}

function Tema({ tema }: TemaProps) {
    return <h3 className='titulo-tema'>{tema.nome}</h3>;
}

export default Tema;