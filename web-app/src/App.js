import './App.css';
import Mobile from './pages/Mobile';
import Desktop from './pages/Desktop';
import {Responsive} from './components/Responsive';



function App() {
  return (

    <>
      <Responsive displayIn={["Mobile"]}>
        <Mobile/>
      </Responsive>
      {/*
      <Responsive displayIn={["Tablet"]}>
        <Tablet/>
      </Responsive>
      */}
      <Responsive displayIn={["Tablet", "Laptop"]}>
        <Desktop/>
      </Responsive>
    </>

  );
}

export default App;
