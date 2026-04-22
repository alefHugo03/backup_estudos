import './card-evento.estilos.css'

interface Tema{
    id: number;
    nome: string;
}

interface IEvento {
    id: number;
    capa: string;
    tema: Tema;
    data: Date;
    titulo: string;
}

interface CardEventoProps {
    evento: IEvento;
}

function CardEvento ({ evento }: CardEventoProps) {
    return (
        <div className="card-evento">
            <img src={evento.capa} alt={evento.titulo}/>
            <div className="corpo">
                <p className="tag">{evento.tema.nome}</p>
                <p>
                    {evento.data.toLocaleDateString('pt-br')}
                </p>
                <h4 className="titulo">
                    {evento.titulo}
                </h4>
            </div>
        </div>
    )
}

export default CardEvento;