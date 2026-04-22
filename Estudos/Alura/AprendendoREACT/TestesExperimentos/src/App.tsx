import './App.css'
import type { ReactNode } from 'react';

// noreact, componente são FUNÇÔES

interface footerProps {
  children: ReactNode;
}

function FooterPreview({ children }: footerProps) {
  return (
  <footer>
    { children }
  </footer>
  )
}


// Pré-carregamento das label do formulario, ficando mais dinamico e reaproveitavel
// precisa declarar o que vai ter nesse objeto para poder usa-lo
interface LabelProps {
  children: ReactNode;
  htmlFor: string;
}

function Label({ children, htmlFor }: LabelProps) {
  return (
    <label htmlFor={ htmlFor }>
      { children }
    </label>
  )
}
// Pré-carregamento do campo do formulario, ficando mais dinamico e reaproveitavel
// precisa declarar o que vai ter nesse objeto para poder usa-lo

interface CampoDeFormularioProps {
  children: ReactNode;
}

function CampoDeFormulario({ children }: CampoDeFormularioProps) {
  return (
    <fieldset>
      { children }
    </fieldset>
  )
}


// Pré-carregamento do título, ficando mais dinamico e reaproveitavel
// precisa declarar o que vai ter nesse objeto para poder usa-lo
interface TituloFormularioProps {
  children: ReactNode;
}

function TituloFormulario({ children }: TituloFormularioProps) {
  return (
    <h2>
      { children }
    </h2>
  )
}

// Formulario que vai ficar dentro da Main
function FormularioDeEvento(){
  return (
    <form className="form-evento">
      <TituloFormulario>
        Preencha para criar um evento:
      </TituloFormulario>
        
      <CampoDeFormulario>
        <Label htmlFor="nome">
          Qual o nome do evento?
        </Label>
        
        <input type="text" id="nome" placeholder="Summer dev hits" />
      </CampoDeFormulario>

    </form>
  )
}


// Função principal do projeto
function App() {
  return (
    <main>
      <header>
        <img src="/logo.png" alt="Logo" />
      </header>

      <section>
        <img src="/banner.png" alt="Banner" />
      </section>
    <FormularioDeEvento />

    <FooterPreview>
      Olá amigos
    </FooterPreview>

    </main>
  )
}

export default App
