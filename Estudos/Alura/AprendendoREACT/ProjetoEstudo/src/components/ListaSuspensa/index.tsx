import "./lista-suspensa.estilos.css"


interface Tema {
    id: number;
    nome: string;
}

interface ListaSuspensaProps {
    id: string;
    name: string
    itens: Tema[];
}

function ListaSuspensa({ itens, ...rest }: ListaSuspensaProps) {
    return(
        <select className="lista-suspensa-form" { ...rest }>
            <option value="" disabled>
                Selecione uma opção
            </option>
            {itens.map(function (item) {
                return(
                    // 4. Trocamos o ClipboardItem pelo 'item' correto
                    <option key={item.id} value={item.id}>
                        {item.nome}
                    </option>
                )
            })}
        </select>
    )
}

export default ListaSuspensa;