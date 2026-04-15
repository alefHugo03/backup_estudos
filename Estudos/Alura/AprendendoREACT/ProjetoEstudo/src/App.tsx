import './App.css'
import FormularioDeEvento from './components/FormularioDeEvento/index.tsx'

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

  return (
    <main>
      <header>
        <img src="/logo.png" alt="Logo" />
      </header>

      <section>
        <img src="/banner.png" alt="Banner" />
      </section>
      <FormularioDeEvento />

      <section>
        <Tema temas={0}/>
      </section>
      <section>
        <Tema temas={1}/>
      </section>
      <section>
        <Tema temas={2}/>
      </section>
      <section>
        <Tema temas={3}/>
      </section>
      <section>
        <Tema temas={4}/>
      </section>
      <section>
        <Tema temas={5}/>
      </section>
      
    </main>
  )
}

export default App
