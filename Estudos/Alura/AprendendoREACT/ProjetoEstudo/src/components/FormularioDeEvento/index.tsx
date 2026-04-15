import './formulario-de-evento.estilos.css'
import TituloFormulario from '../TituloFormulario/index.tsx';
import CampoDeFormulario from '../CampoDeFormulario/index.tsx'
import Label from '../Label/index.tsx'
import CampoDeEntrada from '../CampoDeEntrada/index.tsx'
import Botao from '../Botao/index.tsx'
import ListaSuspensa from '../ListaSuspensa/index.tsx';




function FormularioDeEvento() {
  return (
    <form className="form-evento">
      <TituloFormulario>
        Preencha para criar um evento:
      </TituloFormulario>

      <CampoDeFormulario>
        <div className="campos">
          <Label htmlFor="nome">Nome do Evento</Label>
          <CampoDeEntrada type="text" id="nome" placeholder="Summer dev hits" />

          <Label htmlFor="dataEvento">Data do Evento</Label>
          <CampoDeEntrada type="date" id="dataEvento" />

          <ListaSuspensa />
        </div>
        <div className="acoes">
          <Botao>Criar Evento</Botao>
        </div>
      </CampoDeFormulario>

    </form>
  )
}

export default FormularioDeEvento;