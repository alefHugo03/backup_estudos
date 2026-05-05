import './App.css'
import Banner from './components/Banner/index.tsx'
import CardEvento from './components/CardEvento/index.tsx'
import FormularioDeEvento from './components/FormularioDeEvento/index.tsx'
import Tema from './components/Tema/index.tsx'

interface Tema{
    id: number;
    nome: string;
  }
interface Evento {
    id: number;
    capa: string;
    tema: Tema;
    data: Date;
    titulo: string;
  }

// noreact, componente são FUNÇÔES
function App() {  
  
  const temas = [
    {
      id: 1,
      nome: 'front-end'
    },
    {
      id: 2,
      nome: 'back-end'
    },
    {
      id: 3,
      nome: 'devops'
    },
    {
      id: 4,
      nome: 'inteligência artificial'
    },
    {
      id: 5,
      nome: 'data science'
    },
    {
      id: 6,
      nome: 'cloud'
    }
  ]
  
  const eventos: Evento[] = [
    {
      id: 1,
      capa: '',
      tema: temas[0],
      data: new Date(),
      titulo: 'Mulheres no Front'
    },
    {
      id: 1,
      capa: '',
      tema: temas[0],
      data: new Date(),
      titulo: 'Mulheres no Front'
    },
    {
      id: 1,
      capa: '',
      tema: temas[0],
      data: new Date(),
      titulo: 'Mulheres no Front'
    }
  ]

  return (
    <main>
      <header>
        <img src="/logo.png" alt="Logo" />
      </header>

      <Banner />

      <FormularioDeEvento />

      { temas.map( tema => (
        
          <section key={tema.id}>
            {eventos
              .filter(evento => evento.tema.id === tema.id)
              .map(eventoFiltrado => (
                <CardEvento key={eventoFiltrado.id} evento={eventoFiltrado}/>
              ))
            }
          </section>
        ) 
      )
      }
      
    </main>
  )
}

export default App
