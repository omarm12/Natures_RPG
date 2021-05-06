import './App.css';
import Mobile from './pages/Mobile';
import Desktop from './pages/Desktop';
import Welcome from './pages/Welcome';
import {Responsive} from './components/Responsive';



function App() {

  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const u_id = urlParams.get('u');

  if(!u_id){
    return <Welcome/>
  } else {
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
}

export default App;
