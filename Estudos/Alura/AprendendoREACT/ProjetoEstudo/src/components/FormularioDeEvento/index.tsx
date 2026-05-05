import './formulario-de-evento.estilos.css'
import TituloFormulario from '../TituloFormulario/index.tsx';
import CampoDeFormulario from '../CampoDeFormulario/index.tsx'
import Label from '../Label/index.tsx'
import CampoDeEntrada from '../CampoDeEntrada/index.tsx'
import Botao from '../Botao/index.tsx'
import ListaSuspensa from '../ListaSuspensa/index.tsx';
import Tema from '../Tema/index.tsx';

interface Tema{
    id: number;
    nome: string;
}

interface FormularioDeEventoProps {
    temas: Tema[];
    aoSubmeter: (evento: Evento) => void; 
}

interface Evento {
    id: number;
    capa: string;
    tema: Tema;
    data: Date;
    titulo: string;
}


function FormularioDeEvento({ temas , aoSubmeter }: FormularioDeEventoProps) {

  function aoFormSubmetido(formData: any) {
    console.log("Tá na hora de criar um novo evento" ,formData);
    const evento: Evento = {
      id: Date.now(),
      capa: formData.get('capa'),
      tema: temas.find(item => item.id === Number(formData.get('tema'))) as Tema,
      data: new Date(formData.get('dataEvento')),
      titulo: formData.get('nomeEvento'),
    }

    aoSubmeter(evento);
  }

  return (
    <form className="form-evento" action={aoFormSubmetido}>
      <TituloFormulario>
        Preencha para criar um evento:
      </TituloFormulario>

      <CampoDeFormulario>
        <div className="campos">
          <Label htmlFor="nomeEvento">Qual o nome do evento?</Label>
          <CampoDeEntrada type="text" id="nomeEvento" name='nomeEvento' placeholder="Summer dev hits" />

          <Label htmlFor="capa">Qual o endereço da imagem de capa?</Label>
          <CampoDeEntrada type="text" id="capa" name='capa' placeholder="htpps://..." />



          <Label htmlFor="dataEvento">Data do Evento</Label>
          <CampoDeEntrada type="date" name='dataEvento' id="dataEvento" />


          <Label htmlFor="tema">Tema do Evento</Label>
          <ListaSuspensa id="tema" name="tema" itens={ temas }/>
        </div>
        <div className="acoes">
          <Botao>Criar Evento</Botao>
        </div>

        
      </CampoDeFormulario>
    </form>
  )
}

export default FormularioDeEvento;