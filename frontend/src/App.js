import "./App.css";
import InterestScreen from "./Components/AppScreen/InterestsScreen";
import HomeScreen from "./Components/HomeScreen/HomeScreen"
import Navbar from "./Components/Navbar/Navbar";
import PriorityPlaces from "./Components/AppScreen/PriorityPlaces";
import CreateRoute from "./Components/AppScreen/CreateRoute";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Routes>
          <Route exact path="/" element={<HomeScreen/>} />
          <Route path="/interests" element={<InterestScreen/>}/>
          <Route path="/prioritypois" element={<PriorityPlaces/>}/>
          <Route path="/routes" element={<CreateRoute/>}/>
        </Routes>
      </Router>
    </div>
  );
}

export default App;
